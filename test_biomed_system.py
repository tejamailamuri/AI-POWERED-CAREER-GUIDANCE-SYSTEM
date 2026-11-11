"""
Comprehensive Automated Test Suite for Bio-Medical Waste Segregation System.
Verifies Computer Vision classification, IoT smart bin telemetry, and REST endpoints.
"""

import unittest
import io
import json
from PIL import Image

from biomed_app import app
from core.biomed_dataset import get_all_waste_items, get_bin_specs
from core.classifier import BioWasteClassifier
from core.iot_simulator import SmartBinMonitor
from core.manifest_manager import ManifestManager
from core.guidance_engine import get_safety_protocols, get_staff_quiz

class TestBioMedicalWasteSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.classifier = BioWasteClassifier()
        cls.iot = SmartBinMonitor()
        cls.manifest = ManifestManager()

    def test_01_dataset_integrity(self):
        items = get_all_waste_items()
        self.assertGreaterEqual(len(items), 10, "Biomedical waste catalog must contain at least 10 items")
        specs = get_bin_specs()
        for expected_color in ["yellow", "red", "white", "blue", "general"]:
            self.assertIn(expected_color, specs)

    def test_02_nlp_query_classification(self):
        # Sharps
        res_needle = self.classifier.classify_text_query("hypodermic needle and surgical blade")
        self.assertEqual(res_needle["category"], "white")
        self.assertEqual(res_needle["servo_actuator"]["angle"], 90)

        # Contaminated Plastics
        res_glove = self.classifier.classify_text_query("used plastic surgical gloves and IV tubing")
        self.assertEqual(res_glove["category"], "red")
        self.assertEqual(res_glove["servo_actuator"]["angle"], 45)

        # Infectious / Soiled
        res_cotton = self.classifier.classify_text_query("blood soaked cotton swab and wound dressing")
        self.assertEqual(res_cotton["category"], "yellow")
        self.assertEqual(res_cotton["servo_actuator"]["angle"], 0)

        # Glassware
        res_vial = self.classifier.classify_text_query("glass antibiotic vial and ampoule")
        self.assertEqual(res_vial["category"], "blue")
        self.assertEqual(res_vial["servo_actuator"]["angle"], 135)

    def test_03_computer_vision_image_classification(self):
        # Create synthetic test image
        img = Image.new("RGB", (128, 128), color=(220, 30, 30))
        img_bytes = io.BytesIO()
        img.save(img_bytes, format="JPEG")
        raw_bytes = img_bytes.getvalue()

        result = self.classifier.classify_image(raw_bytes, "test.jpg")
        self.assertTrue(result["success"])
        self.assertIn("category", result)
        self.assertIn("confidence", result)
        self.assertIn("servo_actuator", result)
        self.assertIn(result["category"], ["yellow", "red", "white", "blue", "general"])

    def test_04_iot_telemetry_and_disposal(self):
        bins = self.iot.get_all_bins()
        self.assertIn("bins", bins)
        self.assertIn("yellow", bins["bins"])

        initial_items = bins["bins"]["yellow"]["items_count"]
        initial_weight = bins["bins"]["yellow"]["weight_kg"]

        # Simulate disposal into yellow bin
        disp_res = self.iot.record_disposal("yellow", item_weight_kg=0.5)
        self.assertTrue(disp_res["success"])

        updated_bins = self.iot.get_all_bins()["bins"]
        self.assertEqual(updated_bins["yellow"]["items_count"], initial_items + 1)
        self.assertGreater(updated_bins["yellow"]["weight_kg"], initial_weight)

    def test_05_digital_manifest_and_audit(self):
        record = self.manifest.add_manifest_entry({
            "category": "red",
            "item_name": "Surgical Nitrile Gloves",
            "department": "Emergency Trauma Unit",
            "weight_kg": 0.75,
            "hazard_level": "Level 3"
        })
        self.assertIn("manifest_id", record)
        self.assertTrue(record["manifest_id"].startswith("BMW-2026-"))
        self.assertIn("barcode", record)

        audit = self.manifest.get_audit_summary()
        self.assertIn("total_weight_kg", audit)
        self.assertGreater(audit["total_weight_kg"], 0)

    def test_06_flask_api_endpoints(self):
        # 1. Bins
        res = self.client.get("/api/biomed/bins")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn("bins", data)

        # 2. Text Query Classification API
        res = self.client.post("/api/biomed/classify-query", json={
            "query": "injection needles",
            "department": "ICU",
            "weight_kg": 0.2
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["classification"]["category"], "white")

        # 3. Protocols
        res = self.client.get("/api/biomed/protocols")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn("safety_protocols", data)
        self.assertIn("staff_quiz", data)

        # 4. Manifests
        res = self.client.get("/api/biomed/manifests")
        self.assertEqual(res.status_code, 200)

        # 5. Audit Summary
        res = self.client.get("/api/biomed/audit-summary")
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()

