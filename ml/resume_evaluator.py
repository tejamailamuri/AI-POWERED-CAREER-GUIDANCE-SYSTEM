"""
AI-Powered Resume Evaluator & ATS Scanner using Natural Language Processing.
Supports plain text, PDF, and DOCX documents.
Extracts contact info, skills, key sections, action verbs, and quantifiable metrics.
Calculates ATS Compatibility Score (0 - 100) and role-specific keyword alignment.
"""

import re
import os
from typing import Dict, List, Any
import pypdf
from docx import Document

from ml.career_database import get_all_careers, get_career_by_id

# Comprehensive skill ontology
SKILL_DICTIONARY = [
    # Programming Languages
    "Python", "JavaScript", "TypeScript", "Java", "C++", "C#", "C", "Go", "Golang", "Rust",
    "PHP", "Ruby", "Swift", "Kotlin", "Dart", "R", "SQL", "HTML", "HTML5", "CSS", "CSS3",
    "Bash", "Shell", "PowerShell", "Solidity", "Scala", "MATLAB",

    # Web & Full Stack Frameworks
    "React", "React.js", "Next.js", "Vue", "Vue.js", "Angular", "Node.js", "Express",
    "Express.js", "Django", "Flask", "FastAPI", "Spring", "Spring Boot", "ASP.NET",
    "Laravel", "Ruby on Rails", "Tailwind CSS", "Bootstrap", "Redux", "GraphQL", "REST API",
    "RESTful APIs", "WebSockets", "Microservices",

    # Databases & Caching
    "PostgreSQL", "MySQL", "MongoDB", "Redis", "SQLite", "Oracle", "Microsoft SQL Server",
    "Cassandra", "DynamoDB", "Firebase", "Firestore", "Supabase", "Elasticsearch",

    # AI / ML / Data Science
    "Machine Learning", "Deep Learning", "Artificial Intelligence", "NLP", "Natural Language Processing",
    "Computer Vision", "TensorFlow", "PyTorch", "Keras", "Scikit-Learn", "Pandas", "NumPy",
    "Matplotlib", "Seaborn", "OpenCV", "Hugging Face", "Transformers", "LLM", "Generative AI",
    "LangChain", "Vector Databases", "ChromaDB", "Pinecone", "Data Science", "Data Analysis",
    "Tableau", "Power BI", "BigQuery", "Snowflake", "Spark", "PySpark", "Hadoop",

    # Cloud, DevOps & Infrastructure
    "AWS", "Amazon Web Services", "Microsoft Azure", "Azure", "Google Cloud", "GCP",
    "Docker", "Kubernetes", "Terraform", "CI/CD", "GitHub Actions", "GitLab CI", "Jenkins",
    "Ansible", "Linux", "Unix", "Prometheus", "Grafana", "Nginx", "Apache",

    # Cybersecurity & Networking
    "Cybersecurity", "Network Security", "Ethical Hacking", "Penetration Testing",
    "Vulnerability Assessment", "Wireshark", "Metasploit", "Splunk", "SIEM", "Firewalls",
    "Cryptography", "OWASP", "Active Directory",

    # UI/UX & Design
    "Figma", "Adobe XD", "Sketch", "Wireframing", "Prototyping", "User Research",
    "Usability Testing", "Design Systems", "UI Design", "UX Design",

    # Project Management & Soft Skills
    "Agile", "Scrum", "Jira", "Kanban", "Git", "GitHub", "GitLab", "Bitbucket",
    "Leadership", "Team Collaboration", "Problem Solving", "Critical Thinking",
    "Communication", "Public Speaking", "Time Management"
]

STRONG_ACTION_VERBS = [
    "spearheaded", "architected", "engineered", "developed", "designed", "implemented",
    "optimized", "accelerated", "automated", "orchestrated", "transformed", "boosted",
    "reduced", "increased", "maximized", "minimized", "streamlined", "solved",
    "deployed", "scaled", "collaborated", "managed", "supervised", "achieved", "delivered"
]

class ResumeEvaluator:
    def __init__(self):
        self.skill_set = sorted(SKILL_DICTIONARY, key=lambda s: len(s), reverse=True)

    @staticmethod
    def extract_text_from_pdf(file_path: str) -> str:
        """Extracts plain text from PDF using pypdf."""
        text = ""
        try:
            reader = pypdf.PdfReader(file_path)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        except Exception as e:
            text = f"Error reading PDF: {str(e)}"
        return text

    @staticmethod
    def extract_text_from_docx(file_path: str) -> str:
        """Extracts text from DOCX document."""
        text = ""
        try:
            doc = Document(file_path)
            for para in doc.paragraphs:
                text += para.text + "\n"
        except Exception as e:
            text = f"Error reading DOCX: {str(e)}"
        return text

    def extract_contact_info(self, text: str) -> Dict[str, Any]:
        """Extracts email, phone, LinkedIn, and GitHub links."""
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        phone_pattern = r'(\+?\d{1,3}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}'
        linkedin_pattern = r'linkedin\.com/in/[a-zA-Z0-9_-]+'
        github_pattern = r'github\.com/[a-zA-Z0-9_-]+'

        emails = re.findall(email_pattern, text)
        phones = re.findall(phone_pattern, text)
        linkedin = re.findall(linkedin_pattern, text, re.IGNORECASE)
        github = re.findall(github_pattern, text, re.IGNORECASE)

        return {
            "email": emails[0] if emails else None,
            "phone": "Found" if phones else None,
            "linkedin": f"https://{linkedin[0]}" if linkedin else None,
            "github": f"https://{github[0]}" if github else None
        }

    def detect_sections(self, text: str) -> Dict[str, bool]:
        """Detects presence of essential resume sections."""
        text_lower = text.lower()
        return {
            "Contact Information": bool(re.search(r'(email|phone|contact|linkedin|github)', text_lower)),
            "Summary / Objective": bool(re.search(r'(summary|objective|profile|about me)', text_lower)),
            "Experience / Work History": bool(re.search(r'(experience|work history|employment|internship)', text_lower)),
            "Education": bool(re.search(r'(education|degree|university|college|academic|bachelor|master|b\.tech|bs)', text_lower)),
            "Skills": bool(re.search(r'(skills|technical skills|competencies|technologies)', text_lower)),
            "Projects": bool(re.search(r'(projects|academic projects|personal projects)', text_lower)),
            "Certifications": bool(re.search(r'(certifications|certificates|licenses|courses)', text_lower))
        }

    def extract_skills(self, text: str) -> List[str]:
        """Finds skills mentioned in the resume using word boundary regex."""
        detected = []
        text_lower = f" {text.lower()} "
        
        for skill in self.skill_set:
            escaped = re.escape(skill.lower())
            # Match standalone terms
            pattern = rf'(?:^|[\s,;./\(\)\[\]])({escaped})(?:$|[\s,;./\(\)\[\]])'
            if re.search(pattern, text_lower):
                if skill not in detected:
                    detected.append(skill)
        return detected

    def analyze_action_verbs_and_metrics(self, text: str) -> Dict[str, Any]:
        """Counts impactful action verbs and quantifiable metrics."""
        text_lower = text.lower()
        verbs_found = []
        for verb in STRONG_ACTION_VERBS:
            if re.search(rf'\b{verb}\b', text_lower):
                verbs_found.append(verb)

        # Detect percentages, dollar amounts, metrics like 10+, 5x, 30%
        metric_matches = re.findall(r'(\d+%\s*|\$\d+[\d,]*\s*|\d+x\s*|\b\d{2,}\+\s*)', text)

        return {
            "action_verbs": verbs_found,
            "action_verb_count": len(verbs_found),
            "metrics_detected": metric_matches[:6],
            "metrics_count": len(metric_matches)
        }

    def evaluate_resume(self, text: str, target_career_id: str = None) -> Dict[str, Any]:
        """Comprehensive resume scoring and evaluation."""
        if not text or len(text.strip()) < 50:
            return {"error": "Resume content is too short or empty to analyze properly."}

        words = text.split()
        word_count = len(words)

        contact = self.extract_contact_info(text)
        sections = self.detect_sections(text)
        skills = self.extract_skills(text)
        action_analysis = self.analyze_action_verbs_and_metrics(text)

        # 1. Section Completeness (Max 25 pts)
        sec_points = sum(3.5 for present in sections.values() if present)
        sec_score = min(25.0, round(sec_points, 1))

        # 2. Contact Completeness (Max 15 pts)
        contact_points = 0
        if contact["email"]: contact_points += 5
        if contact["phone"]: contact_points += 4
        if contact["linkedin"]: contact_points += 3
        if contact["github"]: contact_points += 3
        contact_score = min(15.0, float(contact_points))

        # 3. Skill Breadth & Depth (Max 25 pts)
        skill_count = len(skills)
        if skill_count >= 15:
            skill_score = 25.0
        elif skill_count >= 10:
            skill_score = 20.0
        elif skill_count >= 5:
            skill_score = 15.0
        else:
            skill_score = max(5.0, skill_count * 2.5)

        # 4. Impact & Action Verbs (Max 20 pts)
        verb_pts = min(10.0, action_analysis["action_verb_count"] * 1.5)
        metric_pts = min(10.0, action_analysis["metrics_count"] * 2.5)
        impact_score = round(verb_pts + metric_pts, 1)

        # 5. Length & Readability (Max 15 pts)
        if 350 <= word_count <= 850:
            length_score = 15.0
            length_feedback = "Optimal length for a 1-page modern ATS resume."
        elif 200 <= word_count < 350:
            length_score = 10.0
            length_feedback = "Slightly brief. Consider adding more project details and quantifiable outcomes."
        elif word_count > 850:
            length_score = 11.0
            length_feedback = "Longer than typical 1-page standard. Ensure concise bullet points."
        else:
            length_score = 6.0
            length_feedback = "Resume is very short. Expand on experience, skills, and projects."

        total_ats_score = round(sec_score + contact_score + skill_score + impact_score + length_score, 1)
        total_ats_score = min(98.0, max(25.0, total_ats_score))

        # Suggestions for improvement
        suggestions = []
        if not contact["linkedin"]:
            suggestions.append("Add your clickable LinkedIn profile URL in the header.")
        if not contact["github"]:
            suggestions.append("Include your GitHub or portfolio link to showcase code repositories.")
        if not sections["Summary / Objective"]:
            suggestions.append("Add a concise 2-3 sentence Professional Summary highlighting your specialization.")
        if action_analysis["metrics_count"] < 3:
            suggestions.append("Quantify your achievements! (e.g., 'Optimized query latency by 35%', 'Built app used by 500+ students').")
        if action_analysis["action_verb_count"] < 5:
            suggestions.append("Begin every bullet point with strong action verbs (e.g. Architected, Spearheaded, Automated).")
        if skill_count < 8:
            suggestions.append("Enrich your Skills section with modern frameworks, databases, and developer tools.")

        # Role-specific alignment if target career specified
        role_alignment = None
        if target_career_id:
            career = get_career_by_id(target_career_id)
            if career:
                req = career["required_skills"]
                user_skills_lower = [s.lower() for s in skills]
                matched_role_skills = [s for s in req if s.lower() in user_skills_lower]
                missing_role_skills = [s for s in req if s.lower() not in user_skills_lower]
                role_match_pct = round((len(matched_role_skills) / len(req) * 100), 1) if req else 0

                role_alignment = {
                    "target_career": career["title"],
                    "role_match_pct": role_match_pct,
                    "matched_role_skills": matched_role_skills,
                    "missing_keywords_to_add": missing_role_skills[:5],
                    "advice": f"To optimize your resume for {career['title']}, incorporate these critical ATS keywords: {', '.join(missing_role_skills[:4])} into your experience bullet points."
                }

        return {
            "ats_score": total_ats_score,
            "word_count": word_count,
            "length_feedback": length_feedback,
            "score_breakdown": {
                "section_completeness": sec_score,
                "contact_info": contact_score,
                "skill_richness": skill_score,
                "action_and_metrics": impact_score,
                "formatting_readability": length_score
            },
            "contact_details": contact,
            "sections_detected": sections,
            "skills_extracted": skills,
            "action_analysis": action_analysis,
            "improvement_suggestions": suggestions,
            "role_alignment": role_alignment
        }

