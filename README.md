# AI-Powered Career Guidance System 🚀

An intelligent full-stack web application designed to guide students and professionals toward optimal career pathways. The system leverages **Machine Learning**, **Natural Language Processing (NLP)**, and **Multi-Factor Weighted Scoring** to provide personalized career recommendations, identify skill deficiencies, generate step-by-step learning roadmaps, evaluate resumes against ATS criteria, and deliver job market intelligence.

---

## 🌟 Core Features & Modules

### 1. 🎯 Personalized Career Recommender
- **Multi-Factor Weighted Matching:**
  - **Skill Overlap (40%):** Evaluates required and secondary competencies with weighted importance.
  - **NLP Semantic Similarity (20%):** Vectorizes student profile and career corpus via **TF-IDF + Cosine Similarity**.
  - **Interest Affinity (20%):** Analyzes domain interest alignments.
  - **Academic & Education Fit (10%):** Evaluates degree levels, majors, and GPA benchmarks.
  - **Preference Alignment (10%):** Matches remote/hybrid/onsite styles and industry preferences.
- **Machine Learning Category Classifier:** Random Forest model predicts category probabilities based on skill embeddings.
- **Explainable AI (XAI):** Generates transparent reasoning for each match ("Why this matched you").
- **Sample Profile Loader:** 1-click loading for AI, Web Development, Cybersecurity, and Undecided students.

### 2. 📊 Skill Gap Analyzer & Learning Roadmap
- **Critical vs. Secondary Gaps:** Categorizes missing skills into High Priority (core blockers) and Medium Priority (competitive edge).
- **Skill Readiness Index:** Computes a 0–100% readiness score.
- **Custom Action Plan:** Generates timeline-based milestones with recommended free resources (Coursera, Kaggle, Fast.ai, MIT OpenCourseWare) and standout portfolio project blueprints.

### 3. 📄 AI Resume Evaluator & ATS Scanner
- **Multi-Format Ingestion:** Supports plain text paste, **PDF** (via `pypdf`), and **DOCX** (via `python-docx`).
- **ATS Scoring Engine (0–100):** Evaluates section completeness, contact links (LinkedIn, GitHub), keyword richness, and readability.
- **Impact & Action Verb Analysis:** Detects strong verbs (*spearheaded, architected, automated*) and quantified metrics (*percentages, throughput, latency reductions*).
- **Target Role Keyword Optimization:** Compares the resume directly against target tech roles and pinpoints exact missing keywords to beat ATS screeners.

### 4. 🧩 Holland RIASEC Career Personality Assessment
- **Vocational Psychology Model:** Diagnoses student traits across **R**ealistic, **I**nvestigative, **A**rtistic, **S**ocial, **E**nterprising, and **C**onventional themes.
- Generates a primary 3-letter **Holland Code** (e.g., `IRC`, `AIR`) and maps directly to compatible careers.

### 5. 🔍 Career Explorer & Knowledge Base
- Browse comprehensive career pathways with entry, mid, and senior salary projections in both USD and INR.
- Deep dive modal with 3-phase structured roadmaps, core interview questions, and recommended certifications.

### 6. 💼 Market Trends & Live Job Board
- 2026 tech skill velocity and growth rates.
- Curated job and internship postings with dynamic, real-time profile compatibility match scoring.

### 7. 💬 AI Career Advisor Chat
- Interactive guidance counselor for interview preparation (STAR method, DSA strategies), resume optimization, career transitions, and salary negotiation.

---

## 🛠️ Technology Stack

- **Backend:** Python 3.13, Flask 3.1, Flask-CORS
- **Machine Learning & NLP:** Scikit-Learn (TF-IDF Vectorizer, Cosine Similarity, Random Forest), NumPy, Pandas
- **Document Parsers:** PyPDF, Python-docx
- **Frontend:** Responsive Glassmorphic Single-Page Application (HTML5, Tailwind CSS, FontAwesome 6, Chart.js)
- **Database / Data Models:** Structured JSON-based career ontology with extensible schema

---

## 🚀 Quick Start Guide

### 1. Requirements
Ensure Python 3.10+ is installed. Dependencies are listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 2. Run the Application
You can start the server with the included batch script:
- Double-click `run.bat`

Or run directly via command line:
```bash
python app.py
```

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

### 3. Run Automated Tests
```bash
python test_system.py
```

---

## 📂 Project Directory Structure

```
AI Powered Career Guidance System/
├── app.py                      # Flask REST API server & web routes
├── config.py                   # Application configuration
├── requirements.txt            # Python dependencies
├── run.bat                     # Windows one-click start script
├── test_system.py              # Automated test suite (8 unit & integration tests)
├── ml/
│   ├── __init__.py
│   ├── career_database.py      # Rich database of tech & engineering pathways
│   ├── recommender.py          # TF-IDF, Cosine Sim, ML classifier, XAI engine
│   ├── skill_gap_analyzer.py   # Gap detection, priority ranking & action plans
│   ├── resume_evaluator.py     # NLP ATS resume scanner & keyword parser
│   ├── assessment.py           # Holland RIASEC personality assessment
│   ├── market_insights.py      # Salary statistics, trend data & job aggregator
│   └── advisor_nlp.py          # AI Career Counselor & guidance assistant
├── static/
│   ├── css/
│   │   └── style.css           # Custom styles, transitions & glassmorphism
│   ├── js/
│   │   └── app.js              # State management, API controller & UI rendering
│   └── sample_resumes/
│       ├── sample_software_engineer.txt
│       └── sample_data_scientist.txt
└── templates/
    └── index.html              # Sleek, responsive web dashboard
```

---

## 🎯 Project Aim Alignment

| Stated Project Aim Requirement | Implementation in System |
| :--- | :--- |
| **Personalized Career Recommendations** | Hybrid recommender combining TF-IDF NLP semantic matching, multi-factor scoring (skills, interests, degree, GPA, work style), and ML Random Forest classification. |
| **Machine Learning & NLP** | Scikit-Learn TF-IDF vectorizer, cosine similarity matrix, Random Forest classifier, and regex NLP parsers. |
| **Skill Gap Identification** | Compares student skills to career requirements, categorizes high vs. medium gaps, and computes Skill Readiness Index. |
| **Career Guidance & Roadmaps** | 3-phase structured roadmaps (Beginner to Production), curated free resources, project blueprints, and Holland RIASEC quiz. |
| **Resume Evaluation & ATS** | NLP resume parser supporting PDF, DOCX, and text; generates 0–100 ATS score, detects sections, action verbs, and role keyword gaps. |
| **Job-Related Insights** | 2026 market growth rates, salary benchmarks across experience levels, and live job/internship board with personal match scoring. |

