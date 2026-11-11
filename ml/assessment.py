"""
Holland RIASEC Career Assessment Engine.
Helps students discover their vocational personality type (Realistic, Investigative,
Artistic, Social, Enterprising, Conventional) and matches them to suitable tech career paths.
"""

from typing import Dict, List, Any
from ml.career_database import get_all_careers

RIASEC_TRAITS = {
    "R": {
        "name": "Realistic (The Doer)",
        "badge_color": "emerald",
        "description": "Practical, hands-on, loves working with tools, hardware, infrastructure, and tangible systems."
    },
    "I": {
        "name": "Investigative (The Thinker)",
        "badge_color": "blue",
        "description": "Analytical, curious, enjoys solving complex algorithmic puzzles, mathematical modeling, and scientific research."
    },
    "A": {
        "name": "Artistic (The Creator)",
        "badge_color": "purple",
        "description": "Creative, imaginative, driven by aesthetics, human-computer interaction, user interface design, and novel expression."
    },
    "S": {
        "name": "Social (The Helper / Collaborator)",
        "badge_color": "amber",
        "description": "Empathetic, communicative, thrives in user interviews, mentoring, cross-functional teamwork, and customer advocacy."
    },
    "E": {
        "name": "Enterprising (The Persuader / Leader)",
        "badge_color": "rose",
        "description": "Strategic, ambitious, entrepreneurial, focused on product roadmaps, project leadership, and market growth."
    },
    "C": {
        "name": "Conventional (The Organizer)",
        "badge_color": "indigo",
        "description": "Methodical, detail-oriented, excels in structured data, cybersecurity policies, code quality, and testing standards."
    }
}

QUESTIONS = [
    {
        "id": 1,
        "question": "When starting a major new project, what part excites you the most?",
        "options": [
            {"text": "Designing the visual layout, color palette, and micro-interactions", "trait": "A"},
            {"text": "Figuring out the core algorithm and mathematical logic behind the scenes", "trait": "I"},
            {"text": "Setting up the server infrastructure, Docker containers, and database connections", "trait": "R"},
            {"text": "Organizing the task sprint board and defining the project scope and business objectives", "trait": "E"}
        ]
    },
    {
        "id": 2,
        "question": "What kind of problem do you find most satisfying to solve?",
        "options": [
            {"text": "Debugging a tricky memory leak or hardware sensor signal", "trait": "R"},
            {"text": "Analyzing large datasets to discover unexpected patterns and statistical trends", "trait": "I"},
            {"text": "Refactoring an messy UI to make it instantly clear and enjoyable for users", "trait": "A"},
            {"text": "Auditing a system's security logs to find vulnerabilities and enforce compliance", "trait": "C"}
        ]
    },
    {
        "id": 3,
        "question": "In a team hackathon, which role would you naturally pick?",
        "options": [
            {"text": "Team Lead & Pitch Presenter: Communicating our value proposition to judges", "trait": "E"},
            {"text": "UX & Frontend Designer: Crafting wireframes and presentation prototypes", "trait": "A"},
            {"text": "Backend & Cloud Engineer: Building resilient APIs and database pipelines", "trait": "R"},
            {"text": "AI & Algorithm Specialist: Training the machine learning models", "trait": "I"}
        ]
    },
    {
        "id": 4,
        "question": "How do you prefer to approach learning a new technology?",
        "options": [
            {"text": "Reading official documentation, RFC specifications, and systematic guides", "trait": "C"},
            {"text": "Immediately hacking on a hands-on sandbox project and experimenting", "trait": "R"},
            {"text": "Studying the underlying theory, academic papers, and mathematical proofs", "trait": "I"},
            {"text": "Collaborating in a study group, pair programming, and asking mentors", "trait": "S"}
        ]
    },
    {
        "id": 5,
        "question": "Which activity sounds like the most fulfilling weekend hobby?",
        "options": [
            {"text": "Building a custom mechanical keyboard or setting up a home Linux server", "trait": "R"},
            {"text": "Digital drawing, 3D modeling, or writing interactive web animations", "trait": "A"},
            {"text": "Entering a Kaggle data science competition or solving algorithmic challenges", "trait": "I"},
            {"text": "Hosting a community workshop or mentoring junior students in coding", "trait": "S"}
        ]
    },
    {
        "id": 6,
        "question": "What kind of feedback motivates you most at work or school?",
        "options": [
            {"text": "'Your presentation persuaded everyone and won over our leadership!'", "trait": "E"},
            {"text": "'Your design is so smooth and visually gorgeous!'", "trait": "A"},
            {"text": "'Your code runs with 10x faster benchmark latency and zero bugs!'", "trait": "I"},
            {"text": "'Your test suite and documentation saved our team countless hours!'", "trait": "C"}
        ]
    },
    {
        "id": 7,
        "question": "When working with data, what is your primary instinct?",
        "options": [
            {"text": "Clean it meticulously, ensure schema integrity, and eliminate anomalies", "trait": "C"},
            {"text": "Formulate hypotheses, run regression models, and test statistical significance", "trait": "I"},
            {"text": "Design engaging charts and infographics that tell an intuitive story", "trait": "A"},
            {"text": "Use the data to make strategic business decisions and optimize revenue", "trait": "E"}
        ]
    },
    {
        "id": 8,
        "question": "Which workplace environment appeals to you most?",
        "options": [
            {"text": "A fast-paced startup where I can pitch ideas and launch products quickly", "trait": "E"},
            {"text": "A research lab or R&D team tackling unsolved cutting-edge technical challenges", "trait": "I"},
            {"text": "A creative design studio focused on cutting-edge visual experiences", "trait": "A"},
            {"text": "A structured tech enterprise with clear protocols, high security, and quality standards", "trait": "C"}
        ]
    }
]

class CareerAssessment:
    def get_questions(self) -> List[Dict[str, Any]]:
        return QUESTIONS

    def evaluate_assessment(self, answers: List[str]) -> Dict[str, Any]:
        """
        Receives array of chosen traits (e.g. ['A', 'I', 'R', ...])
        Calculates percentage scores for R, I, A, S, E, C.
        Returns personality profile, top 3 traits (Holland Code), and matching careers.
        """
        trait_counts = {"R": 0, "I": 0, "A": 0, "S": 0, "E": 0, "C": 0}

        for trait in answers:
            if trait in trait_counts:
                trait_counts[trait] += 1

        total_answers = max(1, len(answers))
        trait_percentages = {
            t: round((count / total_answers * 100), 1)
            for t, count in trait_counts.items()
        }

        # Sort traits descending
        sorted_traits = sorted(trait_counts.items(), key=lambda x: x[1], reverse=True)
        top_codes = [t[0] for t in sorted_traits[:3]]
        holland_code_str = "".join(top_codes)

        # Match careers based on Holland Code overlap
        careers = get_all_careers()
        matching_careers = []

        for career in careers:
            career_codes = career.get("holland_codes", [])
            overlap = set(top_codes).intersection(set(career_codes))
            match_score = (len(overlap) / max(1, len(career_codes))) * 100

            if match_score >= 33.0:
                matching_careers.append({
                    "id": career["id"],
                    "title": career["title"],
                    "category": career["category"],
                    "holland_overlap": list(overlap),
                    "compatibility_score": round(match_score, 1),
                    "description": career["description"],
                    "entry_salary": career["salaries"]["entry_inr"]
                })

        matching_careers.sort(key=lambda x: x["compatibility_score"], reverse=True)

        return {
            "holland_code": holland_code_str,
            "trait_breakdown": [
                {
                    "code": code,
                    "name": RIASEC_TRAITS[code]["name"],
                    "badge_color": RIASEC_TRAITS[code]["badge_color"],
                    "description": RIASEC_TRAITS[code]["description"],
                    "percentage": trait_percentages[code],
                    "raw_count": trait_counts[code]
                }
                for code in ["R", "I", "A", "S", "E", "C"]
            ],
            "top_traits": [
                {
                    "code": code,
                    "name": RIASEC_TRAITS[code]["name"],
                    "description": RIASEC_TRAITS[code]["description"]
                }
                for code in top_codes
            ],
            "matching_careers": matching_careers[:6]
        }

