"""
AI Career Advisor & Intelligent Guidance Assistant.
Uses pattern matching, intent classification, and career context to provide
expert career advice, interview strategies, learning paths, and portfolio tips.
"""

import re
from typing import Dict, Any, List
from ml.career_database import get_all_careers

KNOWLEDGE_BASE = {
    "interview": {
        "patterns": [r"interview", r"coding round", r"technical interview", r"behavioral", r"prep", r"system design"],
        "title": "Technical & Behavioral Interview Preparation Guide",
        "response": (
            "Here is the proven framework to ace tech interviews:\n\n"
            "1. **Data Structures & Algorithms (DSA):** Master patterns (Sliding Window, Two Pointers, BFS/DFS, Dynamic Programming) on LeetCode/NeetCode rather than memorizing individual solutions.\n"
            "2. **System Design (for Full Stack & Cloud):** Practice designing Twitter, URL Shorteners, or WhatsApp. Focus on scalability, database indexing, caching (Redis), and load balancers.\n"
            "3. **Behavioral Questions (The STAR Method):** Prepare 4-5 stories using **S**ituation, **T**ask, **A**ction, **R**esult. Emphasize teamwork, conflict resolution, and times you overcame technical blockers.\n"
            "4. **Live Coding Mindset:** Always communicate your thought process out loud before typing any code. Write test cases for edge conditions (empty inputs, large values, duplicates)."
        ),
        "actions": ["Practice LeetCode 75", "Study NeetCode Roadmaps", "Do Mock Interviews on Pramp"]
    },
    "resume": {
        "patterns": [r"resume", r"cv", r"ats", r"bullet point", r"formatting", r"score"],
        "title": "High-Impact Resume & ATS Optimization",
        "response": (
            "To get past automated ATS filters and catch a recruiter's eye:\n\n"
            "1. **Use the XYZ Formula (Google Standard):** 'Accomplished [X], as measured by [Y], by doing [Z]'. Example: *'Optimized database queries by 45% by introducing Redis caching layer and compound indexes.'*\n"
            "2. **ATS Formatting Rules:** Stick to a clean single-column layout. Avoid tables, images, or graphical skill rating bars (ATS cannot parse them reliably).\n"
            "3. **Keywords & Skills:** Include exact technologies mentioned in the job description in a dedicated 'Skills' section (Languages, Frameworks, Cloud, Databases).\n"
            "4. **Links:** Always include live hyperlinks to your GitHub profile, LinkedIn, and deployed web app demos."
        ),
        "actions": ["Use our Resume Evaluator Tab", "Quantify bullet points with percentages", "Keep within 1 page"]
    },
    "ai_ml": {
        "patterns": [r"machine learning", r"ai", r"artificial intelligence", r"deep learning", r"data science", r"nlp", r"llm"],
        "title": "Roadmap to Break into Machine Learning & AI",
        "response": (
            "Breaking into Machine Learning as a student in 2026 requires practical engineering skills:\n\n"
            "1. **Mathematics Foundation:** Linear algebra (matrix multiplication, eigenvectors), multivariable calculus (gradients), and probability distributions.\n"
            "2. **Frameworks:** Python, NumPy, Pandas, Scikit-Learn, and PyTorch (the dominant research & industry framework).\n"
            "3. **MLOps & Deployment:** Knowing how to train a model is only 20% of the job. Learn how to wrap models in FastAPI, containerize with Docker, and deploy to AWS/GCP.\n"
            "4. **Standout Portfolio Project:** Don't just submit Titanic or Iris datasets. Build an end-to-end LLM application, semantic document search, or computer vision pipeline with a live UI."
        ),
        "actions": ["Check ML Engineer Roadmap in Career Explorer", "Take Fast.ai Practical Deep Learning", "Publish on Hugging Face Spaces"]
    },
    "web_dev": {
        "patterns": [r"web dev", r"full stack", r"frontend", r"backend", r"react", r"node", r"javascript"],
        "title": "Full-Stack Development Mastery Path",
        "response": (
            "To stand out as a Full-Stack Engineer today:\n\n"
            "1. **Master the Foundation:** Deeply understand JavaScript (closures, promises, event loop, prototypes) and TypeScript.\n"
            "2. **Modern Stack:** React / Next.js on the frontend with Tailwind CSS; Node.js, Express, or Python (FastAPI/Django) on the backend.\n"
            "3. **Database Proficiency:** Write production SQL (PostgreSQL joins, indexing, transactions) and manage ORMs like Prisma or SQLAlchemy.\n"
            "4. **Authentication & Security:** Understand JWTs, OAuth2, session cookies, and protect against OWASP Top 10 vulnerabilities.\n"
            "5. **Production Deployment:** Host on Vercel or AWS, set up automated CI/CD with GitHub Actions, and write unit/integration tests."
        ),
        "actions": ["View Full-Stack Career Profile", "Build a Full-Stack SaaS MVP", "Deploy with CI/CD"]
    },
    "cybersecurity": {
        "patterns": [r"cyber", r"security", r"hacking", r"ethical hacking", r"pentest", r"soc", r"network"],
        "title": "How to Enter Cybersecurity & Ethical Hacking",
        "response": (
            "Cybersecurity demands strong networking and operating system fundamentals:\n\n"
            "1. **Networking Core:** Understand TCP/IP, DNS, DHCP, subnetting, and analyze packet captures using Wireshark.\n"
            "2. **Operating Systems:** Master Linux commands, file permissions, shell scripting, and Windows Active Directory administration.\n"
            "3. **Hands-On Practice:** Don't just read books. Spend time solving challenges on TryHackMe, HackTheBox, and OverTheWire Bandit.\n"
            "4. **Certifications:** CompTIA Security+ is the industry gold standard for entry-level roles, followed by CEH or OSCP."
        ),
        "actions": ["Start TryHackMe Pre-Security Path", "Study CompTIA Security+", "Set up a Home Lab VM"]
    },
    "portfolio": {
        "patterns": [r"portfolio", r"github", r"projects", r"stand out", r"showcase"],
        "title": "Building a Recruiter-Winning Tech Portfolio",
        "response": (
            "A portfolio should prove you can ship real software:\n\n"
            "1. **Quality Over Quantity:** 3 well-documented, full-featured projects beat 10 half-finished tutorial clones.\n"
            "2. **README Excellence:** Every repo must have a GIF demo, architecture diagram, setup instructions, and a live hosted link.\n"
            "3. **Show Real Problem Solving:** Highlight challenges you faced (e.g. *'How I cut API response latency by 60%'* or *'How I handled state sync across tabs'*).\n"
            "4. **Clean Code & Commits:** Use descriptive git commit messages, branch workflows, and clean modular code structure."
        ),
        "actions": ["Pin top 3 repos on GitHub", "Add README GIFs with LICEcap/ScreenToGif", "Deploy live versions on Vercel/Render"]
    },
    "salary": {
        "patterns": [r"salary", r"package", r"lpa", r"ctc", r"negotiate", r"offer"],
        "title": "Salary Insights & Negotiation for College Graduates",
        "response": (
            "Navigating offers and compensation packages:\n\n"
            "1. **Understand CTC vs Base:** Always differentiate between fixed base pay, performance bonuses, joining bonuses, and stock options (ESOPs/RSUs).\n"
            "2. **Research Benchmarks:** Check levels.fyi, Glassdoor, and AmbitionBox for role and location-specific ranges.\n"
            "3. **Always Negotiate Politeness & Data:** Even entry-level offers often have flexibility in joining bonuses or relocation allowances. Base your ask on market data and competing offers.\n"
            "4. **Consider Growth Potential:** In your first 2-3 years, working with exceptional mentors and high-scale technologies provides more career equity than a marginally higher initial stipend."
        ),
        "actions": ["Check Market Insights Tab for 2026 Salary Data", "Explore Levels.fyi", "Focus on Tech Stack Growth"]
    }
}

class AIAdvisor:
    def answer_query(self, user_message: str, user_profile: Dict[str, Any] = None) -> Dict[str, Any]:
        """Provides context-aware career guidance response."""
        message_lower = user_message.lower()

        # Check knowledge base intents
        matched_category = None
        for category, data in KNOWLEDGE_BASE.items():
            for pattern in data["patterns"]:
                if re.search(pattern, message_lower):
                    matched_category = data
                    break
            if matched_category:
                break

        if matched_category:
            return {
                "title": matched_category["title"],
                "reply": matched_category["response"],
                "suggested_actions": matched_category["actions"],
                "category": "targeted_guidance"
            }

        # Fallback intelligent contextual response
        careers = get_all_careers()
        mentioned_career = None
        for c in careers:
            if c["title"].lower() in message_lower or c["id"] in message_lower:
                mentioned_career = c
                break

        if mentioned_career:
            return {
                "title": f"Career Guidance for {mentioned_career['title']}",
                "reply": (
                    f"**{mentioned_career['title']}** is currently experiencing **{mentioned_career['market_outlook']['growth_rate']}** growth with **{mentioned_career['market_outlook']['demand']}** demand.\n\n"
                    f"**Core skills required:** {', '.join(mentioned_career['required_skills'][:6])}.\n\n"
                    f"**Top Hiring Companies:** {', '.join(mentioned_career['top_companies'][:5])}.\n\n"
                    f"**Recommended Project to Build:** {mentioned_career['project_ideas'][0]}.\n\n"
                    f"You can explore the complete step-by-step 3-phase roadmap and evaluate your skill gap directly in our **Skill Gap** and **Career Explorer** tabs!"
                ),
                "suggested_actions": [f"View {mentioned_career['title']} in Explorer", "Run Skill Gap Analysis", "Scan Resume against this Role"],
                "category": "career_specific"
            }

        # General helpful counseling
        return {
            "title": "AI Career Guidance Counselor",
            "reply": (
                "I am here to guide you toward your ideal career in technology! You can ask me about:\n\n"
                "• **Career Transitions:** 'How do I transition from Web Development to Machine Learning?'\n"
                "• **Interview Prep:** 'How should I prepare for DSA and technical interviews?'\n"
                "• **Resume Optimization:** 'How can I make my resume pass ATS filters?'\n"
                "• **Specific Roles:** 'What does a Cloud & DevOps Architect do and what skills do I need?'\n"
                "• **Portfolio & Projects:** 'What kind of projects impress tech hiring managers?'\n\n"
                "Tell me about your current goals, major, or the tech stack you're most excited about!"
            ),
            "suggested_actions": [
                "Take the Holland RIASEC Assessment",
                "Generate Personalized Career Recommendations",
                "Evaluate Resume ATS Score"
            ],
            "category": "general"
        }

