"""
AI-Powered Career Guidance System
Flask Application & RESTful API Server.
"""

import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename

from config import Config
from ml.career_database import get_all_careers, get_career_by_id, get_career_categories
from ml.recommender import CareerRecommender
from ml.skill_gap_analyzer import SkillGapAnalyzer
from ml.resume_evaluator import ResumeEvaluator
from ml.assessment import CareerAssessment
from ml.market_insights import MarketInsights
from ml.advisor_nlp import AIAdvisor

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.from_object(Config)
CORS(app)

# Ensure upload directory exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Initialize ML & NLP Services
recommender = CareerRecommender()
skill_analyzer = SkillGapAnalyzer()
resume_evaluator = ResumeEvaluator()
assessment = CareerAssessment()
market = MarketInsights()
advisor = AIAdvisor()

SAMPLE_PROFILES = {
    "ai_student": {
        "label": "AI & Data Science Student",
        "skills": ["Python", "Machine Learning", "Pandas & NumPy", "SQL", "Git", "Scikit-Learn", "Data Visualization"],
        "interests": ["Artificial Intelligence", "Predictive Analytics", "Deep Learning", "Robotics"],
        "degree": "Bachelor of Technology",
        "major": "Computer Science & Engineering",
        "gpa": 3.6,
        "work_style": "Remote",
        "preferred_industry": "Artificial Intelligence & Data",
        "bio": "Enthusiastic computer science student passionate about predictive analytics, transformer models, and deploying machine learning pipelines."
    },
    "web_dev_student": {
        "label": "Full-Stack Web Enthusiast",
        "skills": ["JavaScript", "React", "Node.js", "HTML5 & CSS3", "Git", "PostgreSQL", "REST APIs"],
        "interests": ["Web Development", "User Experience", "Software Architecture", "API Design"],
        "degree": "Bachelor of Science",
        "major": "Information Technology",
        "gpa": 3.3,
        "work_style": "Hybrid",
        "preferred_industry": "Software Engineering & Web",
        "bio": "Passionate developer who loves crafting interactive frontend interfaces and robust backend microservices."
    },
    "cyber_student": {
        "label": "Cybersecurity & Networks Aspirant",
        "skills": ["Linux & Bash", "Computer Networking (TCP/IP, DNS)", "Network Security", "Git", "Python"],
        "interests": ["Cyber Defense", "Ethical Hacking", "Cryptography", "Network Architecture"],
        "degree": "Bachelor of Science",
        "major": "Cybersecurity / Computer Systems",
        "gpa": 3.2,
        "work_style": "Any",
        "preferred_industry": "Cybersecurity & Infrastructure",
        "bio": "Aspiring security analyst fascinated by threat modeling, packet analysis, penetration testing, and digital forensics."
    },
    "undecided_student": {
        "label": "Undecided Tech Freshman",
        "skills": ["Python", "Git", "HTML5 & CSS3"],
        "interests": ["Problem Solving", "Technology", "Automation"],
        "degree": "Bachelor of Science",
        "major": "Undeclared Engineering",
        "gpa": 3.1,
        "work_style": "Any",
        "preferred_industry": "",
        "bio": "First-year engineering student exploring whether to specialize in Software Engineering, AI, Cloud, or Design."
    }
}

# --- WEB PAGES ---
@app.route("/")
def index():
    return render_template("index.html")

# --- API ENDPOINTS ---

@app.route("/api/sample-profiles", methods=["GET"])
def get_sample_profiles():
    return jsonify(SAMPLE_PROFILES)

@app.route("/api/careers", methods=["GET"])
def list_careers():
    category = request.args.get("category", "").strip()
    search = request.args.get("search", "").strip().lower()

    careers = get_all_careers()
    if category:
        careers = [c for c in careers if c["category"].lower() == category.lower()]
    if search:
        careers = [
            c for c in careers
            if search in c["title"].lower() or search in c["description"].lower() or any(search in s.lower() for s in c["required_skills"])
        ]
    return jsonify({
        "total": len(careers),
        "categories": get_career_categories(),
        "careers": careers
    })

@app.route("/api/careers/<career_id>", methods=["GET"])
def get_career_details(career_id):
    career = get_career_by_id(career_id)
    if not career:
        return jsonify({"error": f"Career with ID '{career_id}' not found."}), 404
    return jsonify(career)

@app.route("/api/recommend", methods=["POST"])
def get_recommendations():
    data = request.get_json(force=True, silent=True) or {}
    recommendations = recommender.recommend(data, top_n=6)
    return jsonify({
        "success": True,
        "total_results": len(recommendations),
        "recommendations": recommendations
    })

@app.route("/api/skill-gap", methods=["POST"])
def evaluate_skill_gap():
    data = request.get_json(force=True, silent=True) or {}
    user_skills = data.get("user_skills", [])
    target_career_id = data.get("target_career_id", "")

    if not target_career_id:
        return jsonify({"error": "target_career_id is required"}), 400

    result = skill_analyzer.analyze_gap(user_skills, target_career_id)
    return jsonify(result)

@app.route("/api/resume/evaluate", methods=["POST"])
def evaluate_resume():
    target_career_id = request.form.get("target_career_id")
    resume_text = ""

    # Check for file upload
    if "file" in request.files:
        file = request.files["file"]
        if file and file.filename:
            filename = secure_filename(file.filename)
            ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
            if ext not in app.config["ALLOWED_EXTENSIONS"]:
                return jsonify({"error": f"Invalid file format. Allowed: {', '.join(app.config['ALLOWED_EXTENSIONS'])}"}), 400

            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)

            try:
                if ext == "pdf":
                    resume_text = resume_evaluator.extract_text_from_pdf(file_path)
                elif ext == "docx":
                    resume_text = resume_evaluator.extract_text_from_docx(file_path)
                else:  # txt
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        resume_text = f.read()
            finally:
                if os.path.exists(file_path):
                    os.remove(file_path)

    # Check for direct text payload (JSON or Form)
    if not resume_text:
        if request.is_json:
            json_data = request.get_json(silent=True) or {}
            resume_text = json_data.get("resume_text", "")
            target_career_id = json_data.get("target_career_id", target_career_id)
        else:
            resume_text = request.form.get("resume_text", "")

    if not resume_text or len(resume_text.strip()) < 50:
        return jsonify({"error": "Please provide your resume content (paste text or upload a PDF/DOCX file)."}), 400

    evaluation = resume_evaluator.evaluate_resume(resume_text, target_career_id)
    return jsonify(evaluation)

@app.route("/api/assessment/questions", methods=["GET"])
def get_assessment_questions():
    questions = assessment.get_questions()
    return jsonify({"questions": questions})

@app.route("/api/assessment/submit", methods=["POST"])
def submit_assessment():
    data = request.get_json(force=True, silent=True) or {}
    answers = data.get("answers", [])
    if not answers:
        return jsonify({"error": "No answers provided"}), 400

    result = assessment.evaluate_assessment(answers)
    return jsonify(result)

@app.route("/api/market-insights", methods=["GET"])
def get_market_insights():
    return jsonify(market.get_market_overview())

@app.route("/api/jobs", methods=["GET"])
def get_jobs():
    skills_param = request.args.get("skills", "")
    skills_list = [s.strip() for s in skills_param.split(",") if s.strip()] if skills_param else []
    jobs = market.get_job_postings(skills_list)
    return jsonify({"total": len(jobs), "jobs": jobs})

@app.route("/api/advisor/chat", methods=["POST"])
def advisor_chat():
    data = request.get_json(force=True, silent=True) or {}
    message = data.get("message", "").strip()
    profile = data.get("profile", {})

    if not message:
        return jsonify({"error": "Message cannot be empty"}), 400

    reply = advisor.answer_query(message, profile)
    return jsonify(reply)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

