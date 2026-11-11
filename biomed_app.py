"""
AI-Powered Bio-Medical Waste Segregation & IoT Smart Bin Monitoring System.
Flask Application & Hospital Command Center API Server.
"""

import os
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename

from core.classifier import BioWasteClassifier
from core.iot_simulator import SmartBinMonitor
from core.manifest_manager import ManifestManager
from core.guidance_engine import get_safety_protocols, get_staff_quiz
from core.biomed_dataset import get_all_waste_items, get_bin_specs

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

UPLOAD_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "uploads", "waste_scans")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Initialize Core Services
classifier = BioWasteClassifier()
iot_bins = SmartBinMonitor()
manifests = ManifestManager()

# --- WEB DASHBOARD ROUTE ---
@app.route("/")
def index():
    return render_template("biomed_index.html")

# --- API ENDPOINTS ---

@app.route("/api/biomed/bins", methods=["GET"])
def get_bins_telemetry():
    return jsonify(iot_bins.get_all_bins())

@app.route("/api/biomed/bins/update", methods=["POST"])
def update_bin_telemetry():
    data = request.get_json(silent=True) or {}
    category = data.get("category", "")
    fill = data.get("fill")
    weight = data.get("weight")
    gas = data.get("gas")

    result = iot_bins.update_bin_telemetry(category, fill, weight, gas)
    return jsonify(result)

@app.route("/api/biomed/bins/empty", methods=["POST"])
def empty_bin():
    data = request.get_json(silent=True) or {}
    category = data.get("category", "")
    result = iot_bins.empty_bin(category)
    return jsonify(result)

@app.route("/api/biomed/classify-image", methods=["POST"])
def classify_waste_image():
    if "image" not in request.files:
        return jsonify({"error": "No image file provided in upload."}), 400

    file = request.files["image"]
    if not file or not file.filename:
        return jsonify({"error": "Empty filename."}), 400

    filename = secure_filename(file.filename)
    image_bytes = file.read()

    # Computer Vision classification
    classification = classifier.classify_image(image_bytes, filename)
    if "error" in classification:
        return jsonify(classification), 400

    category = classification["category"]
    department = request.form.get("department", "Emergency / Surgery Ward")
    weight_kg = float(request.form.get("weight_kg", 0.45))

    # Update IoT bin
    iot_result = iot_bins.record_disposal(category, item_weight_kg=weight_kg)

    # Log in digital manifest
    manifest_record = manifests.add_manifest_entry({
        "category": category,
        "item_name": classification["item_name"],
        "department": department,
        "weight_kg": weight_kg,
        "hazard_level": classification["hazard_rating"]
    })

    return jsonify({
        "classification": classification,
        "iot_bin_status": iot_result,
        "manifest": manifest_record,
        "all_bins": iot_bins.get_all_bins()["bins"]
    })

@app.route("/api/biomed/classify-query", methods=["POST"])
def classify_text_query():
    data = request.get_json(silent=True) or {}
    query = data.get("query", "").strip()
    department = data.get("department", "Inpatient Clinical Ward")
    weight_kg = float(data.get("weight_kg", 0.35))

    if not query:
        return jsonify({"error": "Query string is required."}), 400

    classification = classifier.classify_text_query(query)
    if "error" in classification:
        return jsonify(classification), 400

    category = classification["category"]

    # Dispatch disposal simulation
    iot_result = iot_bins.record_disposal(category, item_weight_kg=weight_kg)
    manifest_record = manifests.add_manifest_entry({
        "category": category,
        "item_name": classification["item_name"],
        "department": department,
        "weight_kg": weight_kg,
        "hazard_level": classification["hazard_rating"]
    })

    return jsonify({
        "classification": classification,
        "iot_bin_status": iot_result,
        "manifest": manifest_record,
        "all_bins": iot_bins.get_all_bins()["bins"]
    })

@app.route("/api/biomed/manifests", methods=["GET"])
def list_manifests():
    cat = request.args.get("category", "").strip()
    q = request.args.get("query", "").strip()
    logs = manifests.get_all_manifests(category=cat, query=q)
    return jsonify({"total": len(logs), "manifests": logs})

@app.route("/api/biomed/audit-summary", methods=["GET"])
def audit_summary():
    return jsonify(manifests.get_audit_summary())

@app.route("/api/biomed/protocols", methods=["GET"])
def get_protocols():
    return jsonify({
        "safety_protocols": get_safety_protocols(),
        "staff_quiz": get_staff_quiz(),
        "bin_specs": get_bin_specs()
    })

@app.route("/api/biomed/sample-items", methods=["GET"])
def list_sample_items():
    return jsonify({"items": get_all_waste_items()})

if __name__ == "__main__":
    print("==================================================================")
    print("  AI-Powered Bio-Medical Waste Segregation & IoT Monitoring System")
    print("  Hospital Command Center Running on: http://127.0.0.1:5000")
    print("==================================================================")
    app.run(host="127.0.0.1", port=5000, debug=True)

