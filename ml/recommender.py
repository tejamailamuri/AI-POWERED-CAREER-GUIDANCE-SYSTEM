"""
Hybrid Recommendation Engine combining:
1. TF-IDF + Cosine Similarity (NLP Text Matching)
2. Multi-Factor Weighted Scoring (Skills, Interests, Education, Preferences)
3. Machine Learning Category Classifier (RandomForest / LogisticRegression)
4. Explainable AI (XAI) transparent reasoning engine.
"""

import re
from typing import Dict, List, Any
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.ensemble import RandomForestClassifier

from ml.career_database import CAREERS, get_all_careers, get_career_by_id

class CareerRecommender:
    def __init__(self):
        self.careers = get_all_careers()
        self.vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
        self._build_career_corpus()
        self._train_ml_classifier()

    def _build_career_corpus(self):
        """Constructs rich text representations for each career for TF-IDF NLP matching."""
        self.career_documents = []
        for c in self.careers:
            doc = " ".join([
                c["title"],
                c["category"] * 2,
                c["description"],
                c["overview"],
                " ".join(c["required_skills"]) * 3,
                " ".join(c["secondary_skills"]),
                " ".join(c["interests"]) * 2,
                " ".join(c["education"]["majors"])
            ])
            self.career_documents.append(doc)

        self.tfidf_matrix = self.vectorizer.fit_transform(self.career_documents)

    def _train_ml_classifier(self):
        """Trains an ML classifier on career skill-sets to predict domain category probabilities."""
        training_texts = []
        training_labels = []

        # Synthetic augmented training data based on career profiles
        for idx, c in enumerate(self.careers):
            category = c["category"]
            # Sample permutations
            for skill in c["required_skills"]:
                training_texts.append(f"{skill} {c['category']} {c['title']}")
                training_labels.append(idx)
            for interest in c["interests"]:
                training_texts.append(f"{interest} {c['category']}")
                training_labels.append(idx)
            # Full career text
            training_texts.append(self.career_documents[idx])
            training_labels.append(idx)

        self.ml_vectorizer = TfidfVectorizer(stop_words='english', min_df=1)
        X = self.ml_vectorizer.fit_transform(training_texts)
        y = np.array(training_labels)

        self.ml_model = RandomForestClassifier(n_estimators=50, random_state=42)
        self.ml_model.fit(X, y)

    @staticmethod
    def _normalize_string(text: str) -> str:
        return re.sub(r'[^a-zA-Z0-9\+\#]', '', text).lower()

    def _match_skills(self, user_skills: List[str], target_skills: List[str]) -> List[str]:
        """Fuzzy/normalized skill matcher."""
        matched = []
        normalized_user = {self._normalize_string(s): s for s in user_skills if s.strip()}
        
        for req in target_skills:
            req_norm = self._normalize_string(req)
            for u_norm, original_u in normalized_user.items():
                if req_norm == u_norm or req_norm in u_norm or u_norm in req_norm:
                    if original_u not in matched:
                        matched.append(original_u)
                    break
        return matched

    def compute_skill_score(self, user_skills: List[str], career: Dict[str, Any]) -> tuple:
        """Calculates weighted skill overlap score and returns matched / missing lists."""
        req_skills = career["required_skills"]
        sec_skills = career.get("secondary_skills", [])

        req_matched = self._match_skills(user_skills, req_skills)
        sec_matched = self._match_skills(user_skills, sec_skills)

        # Required skills form primary baseline, secondary skills provide booster
        req_ratio = (len(req_matched) / len(req_skills)) if req_skills else 1.0
        sec_ratio = (len(sec_matched) / len(sec_skills)) if sec_skills else 0.0

        score = (req_ratio * 80.0) + (sec_ratio * 20.0)
        if len(req_matched) >= 3:
            score = max(score, min(95.0, (req_ratio * 100.0) + 10.0))

        score = min(100.0, max(10.0, round(score, 1)))

        # Missing lists
        req_norm_matched = [self._normalize_string(s) for s in req_matched]
        missing_required = [s for s in req_skills if not any(self._normalize_string(s) in m or m in self._normalize_string(s) for m in req_norm_matched)]

        return score, req_matched, sec_matched, missing_required

    def compute_interest_score(self, user_interests: List[str], career: Dict[str, Any]) -> float:
        """Calculates semantic and keyword overlap between student interests and career domain."""
        if not user_interests:
            return 50.0  # Neutral baseline if unprovided

        career_interests = [self._normalize_string(i) for i in career["interests"]]
        career_cat = self._normalize_string(career["category"])

        matches = 0
        for ui in user_interests:
            ui_norm = self._normalize_string(ui)
            if any(ui_norm in ci or ci in ui_norm for ci in career_interests) or (ui_norm in career_cat or career_cat in ui_norm):
                matches += 1

        score = (matches / len(user_interests)) * 100
        return min(100.0, round(max(20.0, score), 1))

    def compute_education_score(self, degree: str, major: str, gpa: float, career: Dict[str, Any]) -> float:
        """Evaluates degree level, major alignment, and GPA qualification."""
        edu = career["education"]
        score = 70.0  # Default base

        # Degree check
        if degree:
            degree_lower = degree.lower()
            if any(d.lower() in degree_lower for d in edu["degrees"]):
                score += 15.0

        # Major check
        if major:
            major_lower = major.lower()
            if any(m.lower() in major_lower or major_lower in m.lower() for m in edu["majors"]):
                score += 10.0
            elif "computer" in major_lower or "engineering" in major_lower or "science" in major_lower or "data" in major_lower:
                score += 5.0

        # GPA check
        if gpa and gpa > 0:
            min_gpa = edu.get("min_gpa", 2.8)
            if gpa >= min_gpa:
                score += 5.0
            else:
                score -= 10.0

        return min(100.0, max(30.0, round(score, 1)))

    def compute_preference_score(self, preferred_work_style: str, preferred_industry: str, career: Dict[str, Any]) -> float:
        """Evaluates alignment with work style (remote/hybrid/onsite) and target industries."""
        score = 80.0
        if preferred_work_style:
            if preferred_work_style.lower() in [w.lower() for w in career["work_style"]]:
                score += 10.0
            else:
                score -= 15.0

        if preferred_industry:
            if preferred_industry.lower() in career["category"].lower() or preferred_industry.lower() in career["title"].lower():
                score += 10.0

        return min(100.0, max(40.0, round(score, 1)))

    def recommend(self, profile: Dict[str, Any], top_n: int = 5) -> List[Dict[str, Any]]:
        """
        Generates personalized career recommendations based on student profile.
        Profile keys:
        - skills: List[str]
        - interests: List[str]
        - degree: str (e.g. "Bachelor of Technology", "BS in Computer Science")
        - major: str (e.g. "Computer Science", "Information Technology", "Business")
        - gpa: float (e.g. 3.4)
        - work_style: str ("Remote", "Hybrid", "On-site", "Any")
        - preferred_industry: str
        - bio: str (optional freeform student statement)
        """
        user_skills = profile.get("skills", [])
        user_interests = profile.get("interests", [])
        degree = profile.get("degree", "")
        major = profile.get("major", "")
        try:
            gpa = float(profile.get("gpa", 0.0))
        except (ValueError, TypeError):
            gpa = 0.0
        work_style = profile.get("work_style", "Any")
        preferred_industry = profile.get("preferred_industry", "")
        bio = profile.get("bio", "")

        # 1. NLP Content-based Cosine Similarity
        user_text = " ".join([
            " ".join(user_skills) * 3,
            " ".join(user_interests) * 2,
            degree,
            major,
            preferred_industry,
            bio
        ])
        user_vector = self.vectorizer.transform([user_text])
        nlp_similarities = cosine_similarity(user_vector, self.tfidf_matrix)[0]

        # 2. ML Classifier Prediction
        ml_input = self.ml_vectorizer.transform([user_text])
        ml_probs = self.ml_model.predict_proba(ml_input)[0]

        recommendations = []

        for idx, career in enumerate(self.careers):
            # Calculate multi-factor scores
            skill_score, matched_req, matched_sec, missing_req = self.compute_skill_score(user_skills, career)
            interest_score = self.compute_interest_score(user_interests, career)
            edu_score = self.compute_education_score(degree, major, gpa, career)
            pref_score = self.compute_preference_score(work_style, preferred_industry, career)
            
            # Calibrate TF-IDF Cosine Similarity (maps typical 0.0 - 0.6 range into 10 - 100)
            raw_sim = float(nlp_similarities[idx])
            nlp_score = min(100.0, max(15.0, round(raw_sim * 160.0 + 10.0, 1))) if raw_sim > 0.05 else 20.0
            ml_prob_score = round(float(ml_probs[idx]) * 100, 1)

            # Composite weighted formula
            # Skill Match (40%), NLP Semantic Match (20%), Interest (20%), Education (10%), Preference (10%)
            overall_match = (
                (skill_score * 0.40) +
                (nlp_score * 0.20) +
                (interest_score * 0.20) +
                (edu_score * 0.10) +
                (pref_score * 0.10)
            )

            # Bonus for high ML classifier affinity
            if ml_prob_score > 15.0:
                overall_match += min(6.0, ml_prob_score * 0.25)

            overall_match = min(98.5, max(15.0, round(overall_match, 1)))

            # Explainable AI (XAI) reason generator
            reasons = []
            if len(matched_req) >= 3:
                reasons.append(f"Strong skill alignment in core tools: {', '.join(matched_req[:3])}.")
            elif len(matched_req) > 0:
                reasons.append(f"Matches foundational skills: {', '.join(matched_req)}.")

            if interest_score >= 70:
                reasons.append(f"High affinity with your expressed interest in {career['category']}.")

            if edu_score >= 80 and major:
                reasons.append(f"Your educational background in {major} directly supports this career track.")

            if overall_match > 75:
                match_level = "High Match"
                badge_class = "success"
            elif overall_match >= 55:
                match_level = "Moderate Match"
                badge_class = "warning"
            else:
                match_level = "Potential Growth Path"
                badge_class = "info"

            recommendations.append({
                "career_id": career["id"],
                "title": career["title"],
                "category": career["category"],
                "description": career["description"],
                "overall_match": overall_match,
                "match_level": match_level,
                "badge_class": badge_class,
                "score_breakdown": {
                    "skill_match": skill_score,
                    "nlp_match": nlp_score,
                    "interest_alignment": interest_score,
                    "education_fit": edu_score,
                    "preference_fit": pref_score
                },
                "skills_matched": matched_req + matched_sec,
                "missing_skills": missing_req,
                "reasons": reasons,
                "salary_entry": career["salaries"]["entry_inr"],
                "growth_rate": career["market_outlook"]["growth_rate"],
                "demand": career["market_outlook"]["demand"],
                "top_companies": career["top_companies"][:4]
            })

        # Sort descending by overall match
        recommendations.sort(key=lambda x: x["overall_match"], reverse=True)
        return recommendations[:top_n]
