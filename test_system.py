"""
Comprehensive Automated Unit & Integration Tests for AI Career Guidance System.
Verifies all ML algorithms, NLP parsing, scoring engines, and REST API endpoints.
"""

import sys
import unittest
import json

from app import app
from ml.career_database import get_all_careers, get_career_by_id
from ml.recommender import CareerRecommender
from ml.skill_gap_analyzer import SkillGapAnalyzer
from ml.resume_evaluator import ResumeEvaluator
from ml.assessment import CareerAssessment
from ml.market_insights import MarketInsights
from ml.advisor_nlp import AIAdvisor

class TestCareerGuidanceSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.recommender = CareerRecommender()
        cls.gap_analyzer = SkillGapAnalyzer()
        cls.resume_eval = ResumeEvaluator()
        cls.assessment = CareerAssessment()
        cls.market = MarketInsights()
        cls.advisor = AIAdvisor()

    def test_01_career_database(self):
        careers = get_all_careers()
        self.assertGreaterEqual(len(careers), 10, "Career database must have at least 10 detailed profiles")
        
        ml_eng = get_career_by_id("machine-learning-engineer")
        self.assertIsNotNone(ml_eng)
        self.assertEqual(ml_eng["title"], "Machine Learning Engineer")
        self.assertIn("Python", ml_eng["required_skills"])
        self.assertIn("salaries", ml_eng)
        self.assertIn("learning_roadmap", ml_eng)

    def test_02_recommender_engine(self):
        profile = {
            "skills": ["Python", "Machine Learning", "PyTorch", "SQL", "Pandas & NumPy"],
            "interests": ["Artificial Intelligence", "Deep Learning"],
            "degree": "Bachelor's",
            "major": "Computer Science",
            "gpa": 3.7,
            "work_style": "Remote",
            "preferred_industry": "Artificial Intelligence & Data"
        }
        recs = self.recommender.recommend(profile, top_n=5)
        self.assertGreater(len(recs), 0)
        top_rec = recs[0]
        # Top recommendation should be Machine Learning Engineer or Data Scientist
        self.assertIn(top_rec["career_id"], ["machine-learning-engineer", "data-scientist"])
        self.assertGreaterEqual(top_rec["overall_match"], 70.0)
        self.assertIn("score_breakdown", top_rec)
        self.assertIn("reasons", top_rec)

    def test_03_skill_gap_analysis(self):
        user_skills = ["Python", "SQL", "Git"]
        gap = self.gap_analyzer.analyze_gap(user_skills, "machine-learning-engineer")
        self.assertIn("readiness_score", gap)
        self.assertIn("high_priority_gaps", gap)
        self.assertIn("custom_action_steps", gap)
        # Python, Git are possessed, Deep Learning/PyTorch/TensorFlow should be missing
        missing_names = [g["name"] for g in gap["high_priority_gaps"]]
        self.assertTrue(any("TensorFlow" in m or "PyTorch" in m or "Deep Learning" in m for m in missing_names))

    def test_04_resume_evaluation(self):
        with open("static/sample_resumes/sample_software_engineer.txt", "r", encoding="utf-8") as f:
            sample_text = f.read()

        eval_result = self.resume_eval.evaluate_resume(sample_text, target_career_id="full-stack-developer")
        self.assertIn("ats_score", eval_result)
        self.assertGreaterEqual(eval_result["ats_score"], 70.0)
        self.assertTrue(eval_result["sections_detected"]["Skills"])
        self.assertTrue(eval_result["sections_detected"]["Experience / Work History"])
        self.assertGreater(len(eval_result["skills_extracted"]), 5)
        self.assertIsNotNone(eval_result["role_alignment"])

    def test_05_assessment_quiz(self):
        questions = self.assessment.get_questions()
        self.assertGreaterEqual(len(questions), 6)
        
        # Test all 'I' (Investigative) choices
        answers = ["I"] * len(questions)
        result = self.assessment.evaluate_assessment(answers)
        self.assertIn("holland_code", result)
        self.assertTrue(result["holland_code"].startswith("I"))
        self.assertGreater(len(result["matching_careers"]), 0)

    def test_06_market_insights_and_jobs(self):
        overview = self.market.get_market_overview()
        self.assertIn("top_in_demand_skills", overview)
        self.assertIn("salary_benchmarks", overview)

        user_skills = ["Python", "PyTorch", "Docker"]
        jobs = self.market.get_job_postings(user_skills)
        self.assertGreater(len(jobs), 0)
        self.assertIsNotNone(jobs[0]["match_percentage"])

    def test_07_advisor_nlp(self):
        response = self.advisor.answer_query("How can I prepare for coding interviews and DSA?")
        self.assertIn("title", response)
        self.assertIn("Interview", response["title"])
        self.assertIn("STAR", response["reply"])

    def test_08_flask_api_endpoints(self):
        # 1. Careers
        res = self.client.get("/api/careers")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn("careers", data)

        # 2. Recommend
        res = self.client.post("/api/recommend", json={
            "skills": ["JavaScript", "React", "Node.js", "SQL"],
            "interests": ["Web Development"],
            "degree": "Bachelor's",
            "major": "Computer Science"
        })
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data["success"])
        self.assertEqual(data["recommendations"][0]["career_id"], "full-stack-developer")

        # 3. Skill Gap
        res = self.client.post("/api/skill-gap", json={
            "user_skills": ["JavaScript", "React"],
            "target_career_id": "full-stack-developer"
        })
        self.assertEqual(res.status_code, 200)

        # 4. Assessment Submit
        res = self.client.post("/api/assessment/submit", json={
            "answers": ["A", "I", "R", "I", "A", "I", "A", "I"]
        })
        self.assertEqual(res.status_code, 200)

        # 5. Advisor Chat
        res = self.client.post("/api/advisor/chat", json={
            "message": "What is the salary for machine learning engineers?"
        })
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()

