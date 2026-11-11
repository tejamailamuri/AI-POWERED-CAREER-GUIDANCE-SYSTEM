"""
Skill Gap Analysis Module.
Analyzes differences between a student's current skill repertoire and the target career requirements.
Classifies missing skills by priority (High / Medium / Low), calculates Skill Gap Index,
and generates customized learning milestones with recommended courses and project blueprints.
"""

from typing import Dict, List, Any
import re
from ml.career_database import get_career_by_id

class SkillGapAnalyzer:
    @staticmethod
    def _normalize(text: str) -> str:
        return re.sub(r'[^a-zA-Z0-9\+\#]', '', text).lower()

    def analyze_gap(self, user_skills: List[str], target_career_id: str) -> Dict[str, Any]:
        """
        Analyzes the skill gap for a target career given the student's current skills.
        """
        career = get_career_by_id(target_career_id)
        if not career:
            return {"error": f"Career with ID '{target_career_id}' not found."}

        req_skills = career["required_skills"]
        sec_skills = career.get("secondary_skills", [])

        normalized_user = {self._normalize(s): s for s in user_skills if s.strip()}

        matched_skills = []
        high_priority_gaps = []
        medium_priority_gaps = []

        # Check required skills (High Priority)
        for skill in req_skills:
            skill_norm = self._normalize(skill)
            match_found = False
            for u_norm, original_u in normalized_user.items():
                if skill_norm == u_norm or skill_norm in u_norm or u_norm in skill_norm:
                    matched_skills.append({
                        "name": skill,
                        "user_skill": original_u,
                        "type": "Required",
                        "status": "Acquired"
                    })
                    match_found = True
                    break
            if not match_found:
                high_priority_gaps.append({
                    "name": skill,
                    "priority": "High Priority",
                    "type": "Core Requirement",
                    "impact": "Crucial for interviews and daily technical execution",
                    "time_to_learn": "3-6 weeks"
                })

        # Check secondary skills (Medium Priority)
        for skill in sec_skills:
            skill_norm = self._normalize(skill)
            match_found = False
            for u_norm, original_u in normalized_user.items():
                if skill_norm == u_norm or skill_norm in u_norm or u_norm in skill_norm:
                    matched_skills.append({
                        "name": skill,
                        "user_skill": original_u,
                        "type": "Secondary",
                        "status": "Acquired"
                    })
                    match_found = True
                    break
            if not match_found:
                medium_priority_gaps.append({
                    "name": skill,
                    "priority": "Medium Priority",
                    "type": "Competitive Advantage",
                    "impact": "Differentiates candidate in portfolio & senior evaluations",
                    "time_to_learn": "2-4 weeks"
                })

        total_critical = len(req_skills)
        matched_critical = len([s for s in matched_skills if s["type"] == "Required"])
        
        # Skill Readiness Index (0 - 100%)
        readiness_score = round((matched_critical / total_critical * 100), 1) if total_critical > 0 else 100
        gap_score = round(100.0 - readiness_score, 1)

        # Categorize readiness
        if readiness_score >= 80:
            readiness_level = "Job-Ready / Interview Prepared"
            readiness_badge = "success"
        elif readiness_score >= 50:
            readiness_level = "Intermediate Readiness (Minor Gaps)"
            readiness_badge = "warning"
        else:
            readiness_level = "Foundational Stage (Action Plan Needed)"
            readiness_badge = "danger"

        # Generate custom learning roadmap targeting the missing skills
        learning_roadmap = career.get("learning_roadmap", [])
        custom_action_steps = []

        if high_priority_gaps:
            missing_names = [g["name"] for g in high_priority_gaps[:3]]
            custom_action_steps.append({
                "step": 1,
                "title": "Master Core Deficiencies",
                "focus": f"Focus immediately on high-priority tools: {', '.join(missing_names)}",
                "recommended_action": "Complete structured courses, build 2 mini-projects, and practice coding problem sets.",
                "estimated_timeline": "4 - 8 Weeks"
            })

        if medium_priority_gaps:
            med_names = [g["name"] for g in medium_priority_gaps[:3]]
            custom_action_steps.append({
                "step": 2,
                "title": "Acquire Differentiator Skills",
                "focus": f"Add secondary competitive tools: {', '.join(med_names)}",
                "recommended_action": "Incorporate these technologies into full-stack or end-to-end portfolio projects.",
                "estimated_timeline": "3 - 5 Weeks"
            })

        custom_action_steps.append({
            "step": len(custom_action_steps) + 1,
            "title": "Portfolio & Certification Validation",
            "focus": f"Pursue target certification: {career.get('certifications', ['Industry Credential'])[0]}",
            "recommended_action": "Deploy production-grade projects on GitHub with comprehensive documentation and live demos.",
            "estimated_timeline": "2 - 4 Weeks"
        })

        return {
            "career_id": career["id"],
            "career_title": career["title"],
            "category": career["category"],
            "readiness_score": readiness_score,
            "gap_score": gap_score,
            "readiness_level": readiness_level,
            "readiness_badge": readiness_badge,
            "matched_skills": matched_skills,
            "high_priority_gaps": high_priority_gaps,
            "medium_priority_gaps": medium_priority_gaps,
            "custom_action_steps": custom_action_steps,
            "full_roadmap": learning_roadmap,
            "recommended_certifications": career.get("certifications", []),
            "portfolio_projects": career.get("project_ideas", [])
        }

