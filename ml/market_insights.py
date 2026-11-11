"""
Market Insights and Job Trend Intelligence Module.
Provides salary benchmarks, in-demand technical skills, hiring market velocity,
and live job/internship listings with profile compatibility scoring.
"""

from typing import Dict, List, Any
import re

MARKET_STATS = {
    "year": 2026,
    "top_in_demand_skills": [
        {"skill": "Python & PyTorch", "growth": "+42%", "demand_score": 98, "domain": "AI / ML"},
        {"skill": "Docker & Kubernetes", "growth": "+36%", "demand_score": 94, "domain": "DevOps / Cloud"},
        {"skill": "React & Next.js", "growth": "+31%", "demand_score": 92, "domain": "Web Development"},
        {"skill": "Cloud Architecture (AWS/Azure)", "growth": "+34%", "demand_score": 95, "domain": "Cloud"},
        {"skill": "SQL & Vector Databases", "growth": "+29%", "demand_score": 90, "domain": "Data Engineering"},
        {"skill": "Network Security & SIEM", "growth": "+38%", "demand_score": 93, "domain": "Cybersecurity"},
        {"skill": "TypeScript", "growth": "+28%", "demand_score": 88, "domain": "Software Engineering"},
        {"skill": "Large Language Models & MLOps", "growth": "+49%", "demand_score": 97, "domain": "Generative AI"}
    ],
    "work_distribution": {
        "remote": 38,
        "hybrid": 45,
        "onsite": 17
    },
    "salary_benchmarks": [
        {"role": "Machine Learning Engineer", "entry": 98000, "mid": 145000, "senior": 195000, "inr_entry": "14 LPA", "inr_senior": "55 LPA"},
        {"role": "Cloud & DevOps Architect", "entry": 90000, "mid": 135000, "senior": 178000, "inr_entry": "12 LPA", "inr_senior": "45 LPA"},
        {"role": "Data Scientist", "entry": 92000, "mid": 138000, "senior": 182000, "inr_entry": "13 LPA", "inr_senior": "48 LPA"},
        {"role": "Full-Stack Software Engineer", "entry": 85000, "mid": 128000, "senior": 170000, "inr_entry": "10 LPA", "inr_senior": "42 LPA"},
        {"role": "Cybersecurity Engineer", "entry": 82000, "mid": 122000, "senior": 165000, "inr_entry": "9 LPA", "inr_senior": "38 LPA"},
        {"role": "UI/UX Product Designer", "entry": 76000, "mid": 115000, "senior": 155000, "inr_entry": "8 LPA", "inr_senior": "32 LPA"}
    ]
}

JOB_POSTINGS = [
    {
        "id": "job-1",
        "title": "Junior Machine Learning Engineer",
        "company": "DeepMind Innovations",
        "location": "Bangalore / Remote",
        "type": "Full-Time",
        "work_style": "Hybrid",
        "salary": "₹14 - ₹20 LPA",
        "experience": "0-2 years",
        "skills_required": ["Python", "PyTorch", "Scikit-Learn", "Docker", "Git"],
        "description": "Collaborate with senior researchers to train and evaluate transformer models and deploy neural endpoints via FastAPI."
    },
    {
        "id": "job-2",
        "title": "Graduate Full-Stack Developer",
        "company": "Stripe",
        "location": "Hyderabad / Remote",
        "type": "Full-Time",
        "work_style": "Remote",
        "salary": "₹16 - ₹24 LPA",
        "experience": "0-1 years",
        "skills_required": ["React", "TypeScript", "Node.js", "SQL", "Git"],
        "description": "Build high-throughput payment flow interfaces and develop resilient webhook notification services."
    },
    {
        "id": "job-3",
        "title": "Cybersecurity Associate Analyst",
        "company": "CrowdStrike Security Lab",
        "location": "Pune / On-site",
        "type": "Full-Time",
        "work_style": "On-site",
        "salary": "₹9 - ₹15 LPA",
        "experience": "0-2 years",
        "skills_required": ["Linux & Bash", "Network Security", "Wireshark", "Python"],
        "description": "Monitor Security Operations Center (SOC) telemetry, investigate alerts, and draft incident response mitigation reports."
    },
    {
        "id": "job-4",
        "title": "Cloud & DevOps Intern",
        "company": "CloudNative Systems",
        "location": "Remote",
        "type": "Internship (6 Months)",
        "work_style": "Remote",
        "salary": "₹45,000 / month Stipend",
        "experience": "Student / Fresh Graduate",
        "skills_required": ["Linux & Bash", "Docker", "Git", "AWS / Azure / GCP"],
        "description": "Automate deployment pipelines using GitHub Actions and learn container orchestration with Kubernetes."
    },
    {
        "id": "job-5",
        "title": "Data Analyst - Business Intelligence",
        "company": "Deloitte Digital",
        "location": "Gurgaon / Hybrid",
        "type": "Full-Time",
        "work_style": "Hybrid",
        "salary": "₹8 - ₹13 LPA",
        "experience": "0-2 years",
        "skills_required": ["SQL", "Power BI / Tableau", "Excel", "Data Visualization"],
        "description": "Partner with supply chain clients to design interactive executive dashboards and automate data ingestion pipelines."
    },
    {
        "id": "job-6",
        "title": "Associate UI/UX Designer",
        "company": "Canva Creative Labs",
        "location": "Remote",
        "type": "Full-Time",
        "work_style": "Remote",
        "salary": "₹10 - ₹16 LPA",
        "experience": "1-3 years",
        "skills_required": ["Figma", "User Research & Usability Testing", "Wireframing & Prototyping"],
        "description": "Conduct qualitative user research and create pixel-perfect Figma components for our creative suite."
    }
]

class MarketInsights:
    def get_market_overview(self) -> Dict[str, Any]:
        return MARKET_STATS

    def get_job_postings(self, user_skills: List[str] = None) -> List[Dict[str, Any]]:
        """Returns job listings with compatibility score if user skills provided."""
        results = []
        user_skills_clean = [re.sub(r'[^a-zA-Z0-9]', '', s).lower() for s in (user_skills or []) if s]

        for job in JOB_POSTINGS:
            job_copy = dict(job)
            if user_skills_clean:
                matched = []
                for req in job["skills_required"]:
                    clean_req = re.sub(r'[^a-zA-Z0-9]', '', req).lower()
                    if any(clean_req in u or u in clean_req for u in user_skills_clean):
                        matched.append(req)
                
                match_pct = round((len(matched) / len(job["skills_required"]) * 100), 1) if job["skills_required"] else 0
                job_copy["match_percentage"] = match_pct
                job_copy["matched_skills"] = matched
                job_copy["missing_skills"] = [s for s in job["skills_required"] if s not in matched]
            else:
                job_copy["match_percentage"] = None
                job_copy["matched_skills"] = []
                job_copy["missing_skills"] = []

            results.append(job_copy)

        if user_skills_clean:
            results.sort(key=lambda x: x["match_percentage"], reverse=True)

        return results

