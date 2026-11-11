"""
Comprehensive Career Database for the AI Career Guidance System.
Contains 30+ detailed career pathways across Technology, AI, Data Science, Cybersecurity,
Cloud, Product, Design, Engineering, and Business Analytics.
"""

CAREERS = [
    {
        "id": "machine-learning-engineer",
        "title": "Machine Learning Engineer",
        "category": "Artificial Intelligence & Data",
        "description": "Design, build, and deploy self-learning models and neural networks into scalable production environments.",
        "overview": "Machine Learning Engineers sit at the intersection of software engineering and data science. They leverage machine learning frameworks, big data pipelines, and cloud computing to create AI products such as recommendation systems, computer vision apps, and generative AI agents.",
        "holland_codes": ["I", "R", "C"],  # Investigative, Realistic, Conventional
        "required_skills": [
            "Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch",
            "Scikit-Learn", "Data Structures & Algorithms", "Mathematics & Linear Algebra",
            "Git", "Docker"
        ],
        "secondary_skills": [
            "MLOps", "Kubernetes", "SQL", "Cloud Computing (AWS/GCP)", "NLP",
            "Computer Vision", "REST APIs", "C++"
        ],
        "interests": [
            "Artificial Intelligence", "Predictive Analytics", "Deep Learning",
            "Mathematical Modeling", "Algorithmic Research", "Automation", "Robotics"
        ],
        "education": {
            "degrees": ["Bachelor's", "Master's", "Ph.D."],
            "majors": ["Computer Science", "Data Science", "Artificial Intelligence", "Mathematics", "Statistics"],
            "min_gpa": 3.0
        },
        "work_style": ["Remote", "Hybrid", "On-site"],
        "salaries": {
            "entry_usd": 98000,
            "mid_usd": 145000,
            "senior_usd": 195000,
            "entry_inr": "₹10 - ₹18 LPA",
            "mid_inr": "₹22 - ₹40 LPA",
            "senior_inr": "₹45 - ₹85 LPA"
        },
        "market_outlook": {
            "growth_rate": "38% (Extremely Fast)",
            "demand": "Very High",
            "openings": "180,000+ globally"
        },
        "top_companies": ["Google", "Microsoft", "Meta", "NVIDIA", "Amazon", "OpenAI", "Adobe"],
        "certifications": [
            "AWS Certified Machine Learning - Specialty",
            "Google Professional Machine Learning Engineer",
            "DeepLearning.AI TensorFlow Developer"
        ],
        "learning_roadmap": [
            {
                "phase": "Phase 1: Foundations (Months 1-3)",
                "focus": "Core Programming & Mathematics",
                "topics": ["Python proficiency, NumPy, Pandas, Linear Algebra, Multivariate Calculus, Probability & Statistics"],
                "free_resources": ["Coursera Mathematics for Machine Learning", "CS50P (Harvard)", "Kaggle Python Course"]
            },
            {
                "phase": "Phase 2: Core ML & Deep Learning (Months 4-6)",
                "focus": "Algorithms & Frameworks",
                "topics": ["Supervised/Unsupervised Learning, Neural Networks, PyTorch, Scikit-Learn, Hyperparameter Tuning"],
                "free_resources": ["Fast.ai Practical Deep Learning", "Andrew Ng Machine Learning Specialization", "Hugging Face Course"]
            },
            {
                "phase": "Phase 3: Production & MLOps (Months 7-9)",
                "focus": "Deployment, Monitoring & Architecture",
                "topics": ["FastAPI deployment, Docker containerization, MLflow, CI/CD for ML, Vector Databases"],
                "free_resources": ["Made With ML (Goku Mohandas)", "Full Stack Deep Learning", "AWS Free Tier Workshops"]
            }
        ],
        "project_ideas": [
            "End-to-End Predictive Maintenance API with MLflow and Streamlit UI",
            "Semantic Document Search Engine using Vector Embeddings & PyTorch",
            "Real-time Object Detection Pipeline deployed on Docker & FastAPI"
        ],
        "interview_topics": [
            "Bias-variance tradeoff and regularization techniques",
            "Gradient descent variants, backpropagation mathematics",
            "Serving latency optimization and distributed model training"
        ]
    },
    {
        "id": "full-stack-developer",
        "title": "Full-Stack Software Engineer",
        "category": "Software Engineering & Web",
        "description": "Architect and develop modern web applications, from responsive user interfaces to resilient backend APIs and databases.",
        "overview": "Full-Stack Engineers build entire digital experiences. They craft seamless frontends using React, Vue, or Next.js and build scalable backends with Node.js, Python, or Go, managing relational and NoSQL databases.",
        "holland_codes": ["R", "I", "A"],
        "required_skills": [
            "JavaScript", "TypeScript", "React", "Node.js", "HTML5 & CSS3",
            "SQL", "Git", "REST APIs", "Data Structures & Algorithms"
        ],
        "secondary_skills": [
            "Next.js", "Docker", "MongoDB", "PostgreSQL", "Tailwind CSS",
            "GraphQL", "Redis", "Cloud (AWS/Vercel)", "CI/CD"
        ],
        "interests": [
            "Web Development", "Software Architecture", "User Experience",
            "API Design", "Cloud Systems", "Open Source", "Interactive Apps"
        ],
        "education": {
            "degrees": ["Bachelor's", "Associate's", "Self-Taught / Bootcamp"],
            "majors": ["Computer Science", "Information Technology", "Software Engineering"],
            "min_gpa": 2.8
        },
        "work_style": ["Remote", "Hybrid", "On-site"],
        "salaries": {
            "entry_usd": 85000,
            "mid_usd": 128000,
            "senior_usd": 170000,
            "entry_inr": "₹7 - ₹14 LPA",
            "mid_inr": "₹16 - ₹32 LPA",
            "senior_inr": "₹35 - ₹65 LPA"
        },
        "market_outlook": {
            "growth_rate": "25% (Much faster than average)",
            "demand": "Very High",
            "openings": "350,000+ globally"
        },
        "top_companies": ["Stripe", "Airbnb", "Uber", "Microsoft", "Salesforce", "Atlassian", "Shopify"],
        "certifications": [
            "AWS Certified Developer - Associate",
            "Meta Front-End & Back-End Professional Certificates",
            "MongoDB Certified Developer"
        ],
        "learning_roadmap": [
            {
                "phase": "Phase 1: Frontend Mastery (Months 1-3)",
                "focus": "HTML5, CSS3, Modern JavaScript (ES6+) & React",
                "topics": ["DOM manipulation, Flexbox/Grid, Component lifecycles, Hooks, State management"],
                "free_resources": ["The Odin Project", "MDN Web Docs", "FreeCodeCamp Responsive Web Design"]
            },
            {
                "phase": "Phase 2: Backend Architecture & Databases (Months 4-6)",
                "focus": "Node.js/Express, Python/Flask, PostgreSQL & Auth",
                "topics": ["RESTful endpoints, JWT/OAuth, Relational database modeling, Prisma/SQLAlchemy"],
                "free_resources": ["FullStackOpen (University of Helsinki)", "Node.js official guides", "PostgreSQL Tutorial"]
            },
            {
                "phase": "Phase 3: Full Stack Systems & DevOps (Months 7-9)",
                "focus": "Testing, Deployment, Performance & Security",
                "topics": ["Jest/Vitest, Docker, Redis caching, AWS/Vercel deployment, WebSockets"],
                "free_resources": ["roadmap.sh/full-stack", "Docker Curriculum", "AWS Skill Builder"]
            }
        ],
        "project_ideas": [
            "Collaborative Real-time Kanban Workspace with WebSockets and Role-based Auth",
            "SaaS Subscription Platform with Stripe Integration and Analytics Dashboard",
            "Developer Portfolio CMS with Markdown Support and PostgreSQL backend"
        ],
        "interview_topics": [
            "Event loop, asynchronous programming, and microtask queue",
            "Database normalization vs indexing strategies for query performance",
            "Web security: CSRF, XSS, CORS, and SQL injection mitigations"
        ]
    },
    {
        "id": "data-scientist",
        "title": "Data Scientist",
        "category": "Artificial Intelligence & Data",
        "description": "Extract actionable business insights, uncover hidden trends, and build statistical predictive models from complex datasets.",
        "overview": "Data Scientists combine domain expertise, statistics, programming, and storytelling. They transform unstructured data into strategic insights and deploy predictive models that drive decision-making.",
        "holland_codes": ["I", "C", "A"],
        "required_skills": [
            "Python", "SQL", "Pandas & NumPy", "Statistical Analysis", "Data Visualization",
            "Machine Learning", "Exploratory Data Analysis", "Scikit-Learn"
        ],
        "secondary_skills": [
            "R", "Tableau", "Power BI", "A/B Testing", "BigQuery",
            "Spark", "Data Storytelling", "Deep Learning"
        ],
        "interests": [
            "Data Analysis", "Statistical Modeling", "Business Intelligence",
            "Data Storytelling", "Predictive Analytics", "A/B Testing"
        ],
        "education": {
            "degrees": ["Bachelor's", "Master's", "Ph.D."],
            "majors": ["Data Science", "Statistics", "Computer Science", "Economics", "Applied Mathematics"],
            "min_gpa": 3.2
        },
        "work_style": ["Remote", "Hybrid", "On-site"],
        "salaries": {
            "entry_usd": 92000,
            "mid_usd": 138000,
            "senior_usd": 182000,
            "entry_inr": "₹9 - ₹16 LPA",
            "mid_inr": "₹20 - ₹38 LPA",
            "senior_inr": "₹42 - ₹75 LPA"
        },
        "market_outlook": {
            "growth_rate": "35% (Extremely Fast)",
            "demand": "Very High",
            "openings": "210,000+ globally"
        },
        "top_companies": ["Netflix", "Spotify", "Amazon", "JPMorgan Chase", "Google", "McKinsey"],
        "certifications": [
            "IBM Data Science Professional Certificate",
            "Google Data Analytics Professional Certificate",
            "Microsoft Certified: Azure Data Scientist Associate"
        ],
        "learning_roadmap": [
            {
                "phase": "Phase 1: Statistical Foundations & Python (Months 1-3)",
                "focus": "Descriptive Statistics, Probability, Pandas & SQL",
                "topics": ["Hypothesis testing, distributions, complex SQL joins, data cleaning pipelines"],
                "free_resources": ["StatQuest with Josh Starmer", "Khan Academy Statistics", "Mode Analytics SQL Tutorial"]
            },
            {
                "phase": "Phase 2: Applied Machine Learning & Viz (Months 4-6)",
                "focus": "Regression, Classification, Clustering & Tableau",
                "topics": ["Feature engineering, dimension reduction (PCA), interactive dashboards"],
                "free_resources": ["Kaggle Competitions & Micro-courses", "Coursera Applied Data Science with Python"]
            },
            {
                "phase": "Phase 3: Production Analytics & Experimentation (Months 7-9)",
                "focus": "A/B Testing, Causal Inference & Big Data",
                "topics": ["Experiment design, sample sizing, PySpark, model drift monitoring"],
                "free_resources": ["Udacity A/B Testing by Google", "Spark by Examples"]
            }
        ],
        "project_ideas": [
            "Customer Churn Prediction Engine with Feature Importance Breakdown",
            "E-Commerce Pricing Optimization and Elasticity Analysis Model",
            "Interactive Covid-19 or Healthcare Epidemiological Visualization Suite"
        ],
        "interview_topics": [
            "Formulating and interpreting A/B test results with statistical significance",
            "Handling imbalanced datasets (SMOTE, precision-recall AUC)",
            "Explaining complex machine learning outputs to non-technical stakeholders"
        ]
    },
    {
        "id": "cybersecurity-analyst",
        "title": "Cybersecurity Analyst / Security Engineer",
        "category": "Cybersecurity & Infrastructure",
        "description": "Protect digital infrastructure, networks, and sensitive data against cyber threats, intrusion, and ransomware attacks.",
        "overview": "Cybersecurity Analysts monitor networks, identify vulnerabilities, perform penetration testing, and respond to incidents. With rising ransomware threats and privacy laws, cybersecurity experts are among the most critical tech roles globally.",
        "holland_codes": ["R", "I", "C"],
        "required_skills": [
            "Computer Networking (TCP/IP, DNS)", "Linux & Bash", "Network Security",
            "Vulnerability Assessment", "SIEM Tools (Splunk/ELK)", "Firewalls & VPNs",
            "Security Information & Event Management"
        ],
        "secondary_skills": [
            "Python / Scripting", "Ethical Hacking (Kali Linux)", "Cloud Security (AWS/Azure)",
            "Cryptography", "Wireshark", "Incident Response", "OWASP Top 10"
        ],
        "interests": [
            "Cyber Defense", "Ethical Hacking", "Forensics",
            "Cryptography", "Network Architecture", "Information Privacy"
        ],
        "education": {
            "degrees": ["Bachelor's", "Associate's", "Industry Certifications"],
            "majors": ["Cybersecurity", "Computer Science", "Information Systems"],
            "min_gpa": 2.8
        },
        "work_style": ["Remote", "Hybrid", "On-site"],
        "salaries": {
            "entry_usd": 82000,
            "mid_usd": 122000,
            "senior_usd": 165000,
            "entry_inr": "₹6 - ₹13 LPA",
            "mid_inr": "₹15 - ₹30 LPA",
            "senior_inr": "₹32 - ₹60 LPA"
        },
        "market_outlook": {
            "growth_rate": "32% (Much faster than average)",
            "demand": "Extremely High",
            "openings": "750,000+ unfilled positions globally"
        },
        "top_companies": ["Palo Alto Networks", "CrowdStrike", "Cisco", "Mandiant", "Deloitte", "Microsoft"],
        "certifications": [
            "CompTIA Security+",
            "Certified Ethical Hacker (CEH)",
            "Certified Information Systems Security Professional (CISSP)",
            "Offensive Security Certified Professional (OSCP)"
        ],
        "learning_roadmap": [
            {
                "phase": "Phase 1: Networking & Operating Systems (Months 1-3)",
                "focus": "TCP/IP, OSI Model, Linux Administration, Command Line",
                "topics": ["Subnetting, packet routing, permissions, system logs, Wireshark packet analysis"],
                "free_resources": ["Professor Messer CompTIA Network+ & Security+", "OverTheWire Bandit Wargames"]
            },
            {
                "phase": "Phase 2: Defensive & Offensive Operations (Months 4-6)",
                "focus": "Vulnerability Scanning, OWASP, Kali Linux, SIEM",
                "topics": ["Web app vulnerabilities (SQLi, XSS, CSRF), Splunk log analysis, Metasploit basics"],
                "free_resources": ["TryHackMe (Pre-Security & Jr Penetration Tester tracks)", "HackTheBox Academy"]
            },
            {
                "phase": "Phase 3: Threat Hunting & Cloud Security (Months 7-9)",
                "focus": "Incident response, Cloud IAM, Compliance (NIST, ISO 27001)",
                "topics": ["AWS Security Hub, Malware triage, Incident response playbooks"],
                "free_resources": ["SANS Cyber Aces Online", "Cybrary Security Operations"]
            }
        ],
        "project_ideas": [
            "Home Lab SIEM: Deploy Splunk on Linux VM to monitor Windows Active Directory brute force attacks",
            "Automated Vulnerability Scanner Script using Python and Nmap API",
            "Web Security Hardening Guide & Pentest Audit for an open-source web application"
        ],
        "interview_topics": [
            "Explaining the 3-way handshake and SSL/TLS certificate negotiation",
            "Incident response phases: Preparation, Detection, Containment, Eradication, Recovery",
            "Defending against privilege escalation in enterprise Linux and Active Directory"
        ]
    },
    {
        "id": "cloud-devops-engineer",
        "title": "Cloud & DevOps Architect",
        "category": "Cloud & Infrastructure",
        "description": "Design resilient cloud infrastructure, automate deployment pipelines, and guarantee high availability and scale.",
        "overview": "DevOps and Cloud Engineers bridge code development and system operations. Using Infrastructure-as-Code (Terraform), container orchestration (Kubernetes), and continuous delivery pipelines, they enable high-velocity software releases.",
        "holland_codes": ["R", "C", "I"],
        "required_skills": [
            "Linux Administration", "Docker", "Kubernetes", "AWS / Azure / GCP",
            "CI/CD Pipelines (GitHub Actions/Jenkins)", "Infrastructure as Code (Terraform)",
            "Bash / Python Scripting", "Git"
        ],
        "secondary_skills": [
            "Ansible", "Prometheus & Grafana", "Microservices", "Networking & DNS",
            "Serverless (AWS Lambda)", "Cloud Security"
        ],
        "interests": [
            "Cloud Infrastructure", "Automation", "Site Reliability",
            "Distributed Systems", "Containerization", "System Monitoring"
        ],
        "education": {
            "degrees": ["Bachelor's", "Associate's", "Certifications"],
            "majors": ["Computer Science", "Information Technology", "Cloud Computing"],
            "min_gpa": 2.8
        },
        "work_style": ["Remote", "Hybrid", "On-site"],
        "salaries": {
            "entry_usd": 90000,
            "mid_usd": 135000,
            "senior_usd": 178000,
            "entry_inr": "₹8 - ₹15 LPA",
            "mid_inr": "₹18 - ₹35 LPA",
            "senior_inr": "₹38 - ₹70 LPA"
        },
        "market_outlook": {
            "growth_rate": "28% (Much faster than average)",
            "demand": "Very High",
            "openings": "240,000+ globally"
        },
        "top_companies": ["Amazon Web Services", "Microsoft Azure", "Google Cloud", "Red Hat", "HashiCorp", "Datadog"],
        "certifications": [
            "AWS Certified Solutions Architect - Associate",
            "Certified Kubernetes Administrator (CKA)",
            "HashiCorp Certified: Terraform Associate"
        ],
        "learning_roadmap": [
            {
                "phase": "Phase 1: Linux & Containers (Months 1-3)",
                "focus": "Linux Shell, Networking & Docker Mastery",
                "topics": ["File systems, systemd, multi-stage Docker builds, compose stacks, container networking"],
                "free_resources": ["Docker Docs & Tutorials", "Linux Journey (linuxjourney.com)"]
            },
            {
                "phase": "Phase 2: Cloud & CI/CD Pipelines (Months 4-6)",
                "focus": "AWS Architecture, GitHub Actions & Terraform",
                "topics": ["VPC, EC2, S3, IAM, automated test/deploy workflows, declarative cloud provisioning"],
                "free_resources": ["AWS Free Tier Labs", "GitHub Actions Documentation", "Terraform Up & Running tutorials"]
            },
            {
                "phase": "Phase 3: Kubernetes & Observability (Months 7-9)",
                "focus": "Cluster Orchestration, Prometheus, Grafana & Helm",
                "topics": ["Pods, Deployments, Ingress controllers, Helm charts, alerting, SLOs/SLAs"],
                "free_resources": ["Kubernetes The Hard Way (Kelsey Hightower)", "Grafana Community Labs"]
            }
        ],
        "project_ideas": [
            "Multi-Environment Infrastructure on AWS provisioned entirely with Terraform & Remote State",
            "Zero-Downtime Microservices Deployment Pipeline with GitHub Actions and Kubernetes Canary Rollouts",
            "Full Observability Stack: Prometheus, Grafana, and Alertmanager monitoring distributed services"
        ],
        "interview_topics": [
            "Blue-green vs Canary deployment strategies",
            "Troubleshooting CrashLoopBackOff and OOMKilled states in Kubernetes pods",
            "Designing a highly available, multi-region failover architecture on AWS"
        ]
    },
    {
        "id": "ui-ux-designer",
        "title": "UI/UX Product Designer",
        "category": "Design & Product",
        "description": "Craft intuitive, accessible, and aesthetically pleasing human-computer experiences through research and prototyping.",
        "overview": "UI/UX Designers solve user problems through intuitive interfaces, user research, wireframing, and interactive design systems. They turn complex technical capabilities into friction-free digital apps that users love.",
        "holland_codes": ["A", "I", "S"],
        "required_skills": [
            "Figma", "User Research & Usability Testing", "Wireframing & Prototyping",
            "Design Systems & Component Libraries", "Information Architecture",
            "Accessibility (WCAG)", "Visual Design & Typography"
        ],
        "secondary_skills": [
            "HTML & CSS Basics", "Interaction Design (Principle/Framer)",
            "Design Sprints", "Micro-copywriting", "User Journey Mapping"
        ],
        "interests": [
            "Visual Aesthetics", "User Psychology", "Human-Centered Design",
            "Creative Typography", "Product Innovation", "Accessibility"
        ],
        "education": {
            "degrees": ["Bachelor's", "Bootcamp / Design Portfolio"],
            "majors": ["HCI (Human-Computer Interaction)", "Graphic Design", "Interaction Design", "Psychology"],
            "min_gpa": 2.7
        },
        "work_style": ["Remote", "Hybrid", "On-site"],
        "salaries": {
            "entry_usd": 76000,
            "mid_usd": 115000,
            "senior_usd": 155000,
            "entry_inr": "₹6 - ₹12 LPA",
            "mid_inr": "₹14 - ₹28 LPA",
            "senior_inr": "₹30 - ₹55 LPA"
        },
        "market_outlook": {
            "growth_rate": "20% (Faster than average)",
            "demand": "High",
            "openings": "140,000+ globally"
        },
        "top_companies": ["Apple", "Airbnb", "Spotify", "Figma", "Google", "Canva", "Notion"],
        "certifications": [
            "Google UX Design Professional Certificate",
            "Nielsen Norman Group UX Master Certified",
            "Interaction Design Foundation (IxDF) Certification"
        ],
        "learning_roadmap": [
            {
                "phase": "Phase 1: Design Fundamentals & Figma (Months 1-3)",
                "focus": "Visual Hierarchy, Color Theory, Typography & Figma Tooling",
                "topics": ["Auto-layout, responsive constraints, Figma components, interactive variants"],
                "free_resources": ["Figma for Beginners (Official)", "Refactoring UI (Tips & Principles)"]
            },
            {
                "phase": "Phase 2: UX Research & Information Architecture (Months 4-6)",
                "focus": "User Interviews, Persona Building & Journey Mapping",
                "topics": ["Qualitative user testing, card sorting, low-fidelity wireframing, UX heuristics"],
                "free_resources": ["Nielsen Norman Group articles", "Coursera Interaction Design Specialization (Audit)"]
            },
            {
                "phase": "Phase 3: Design Systems & High-Fidelity Prototypes (Months 7-9)",
                "focus": "Tokens, WCAG Accessibility, Micro-interactions & Case Studies",
                "topics": ["Building end-to-end multi-platform design systems, documenting design decisions"],
                "free_resources": ["Material Design Guidelines", "Apple Human Interface Guidelines"]
            }
        ],
        "project_ideas": [
            "Fintech Mobile App redesign: Case study identifying conversion drop-offs and redesigning the checkout flow",
            "Multi-theme Web Design System with documented design tokens and accessibility compliance audit",
            "AI-Powered Student Productivity App: From user empathy interviews to clickable high-fidelity Figma prototype"
        ],
        "interview_topics": [
            "Walking through a design case study and defending trade-offs",
            "How to prioritize user needs when technical feasibility is constrained",
            "Conducting remote usability tests and deriving actionable product improvements"
        ]
    },
    {
        "id": "product-manager",
        "title": "Product Manager / Tech PM",
        "category": "Design & Product",
        "description": "Define product vision, align cross-functional teams, and guide innovative digital products from concept to launch.",
        "overview": "Product Managers operate at the intersection of business, technology, and user experience. They discover market opportunities, define roadmaps, write product specifications (PRDs), and partner with engineers and designers to deliver high-impact software.",
        "holland_codes": ["E", "S", "I"],
        "required_skills": [
            "Product Strategy & Vision", "Agile & Scrum Methodologies", "User Story & PRD Writing",
            "Data Analytics (SQL/Mixpanel)", "Prioritization Frameworks (RICE, MoSCoW)",
            "Cross-functional Leadership", "Market & Competitor Research"
        ],
        "secondary_skills": [
            "A/B Testing", "Figma Basics", "Technical Fluency", "Go-To-Market (GTM) Strategy",
            "Customer Discovery Interviews", "Financial Modeling"
        ],
        "interests": [
            "Product Innovation", "Business Strategy", "Leadership",
            "Market Trends", "Problem Solving", "Entrepreneurship"
        ],
        "education": {
            "degrees": ["Bachelor's", "MBA / Master's"],
            "majors": ["Computer Science", "Business Administration", "Engineering", "Economics"],
            "min_gpa": 3.0
        },
        "work_style": ["Remote", "Hybrid", "On-site"],
        "salaries": {
            "entry_usd": 95000,
            "mid_usd": 142000,
            "senior_usd": 190000,
            "entry_inr": "₹12 - ₹22 LPA",
            "mid_inr": "₹25 - ₹48 LPA",
            "senior_inr": "₹50 - ₹90 LPA"
        },
        "market_outlook": {
            "growth_rate": "22% (Faster than average)",
            "demand": "High",
            "openings": "110,000+ globally"
        },
        "top_companies": ["Google", "Meta", "Microsoft", "Uber", "Spotify", "Amazon", "Coinbase"],
        "certifications": [
            "Certified Scrum Product Owner (CSPO)",
            "Product School: Product Manager Certificate (PMC)",
            "Pragmatic Institute Certified"
        ],
        "learning_roadmap": [
            {
                "phase": "Phase 1: Product Mindset & Customer Discovery (Months 1-3)",
                "focus": "Problem Identification, User Personas & Competitive Analysis",
                "topics": ["Lean startup principles, opportunity solution trees, interviewing customers"],
                "free_resources": ["Inspired by Marty Cagan (Summary/Talks)", "Reforge Blog", "Lenny's Newsletter"]
            },
            {
                "phase": "Phase 2: Execution & Product Metrics (Months 4-6)",
                "focus": "PRD Writing, Agile Sprints, North Star Metrics",
                "topics": ["Acquisition, Activation, Retention metrics (AARRR), running sprint planning, Jira"],
                "free_resources": ["Atlassian Agile Coach", "Amplitude Product Analytics Certification (Free)"]
            },
            {
                "phase": "Phase 3: Strategy & GTM Launch (Months 7-9)",
                "focus": "Product-Market Fit, Pricing, Stakeholder Management",
                "topics": ["Building multi-quarter product roadmaps, cross-functional conflict resolution, feature rollouts"],
                "free_resources": ["Product Coalition", "HBS Working Knowledge Case Studies"]
            }
        ],
        "project_ideas": [
            "Full Product Requirement Document (PRD) and Roadmap for a hypothetical Spotify Feature",
            "Reverse engineering an onboarding funnel for Duolingo with teardown metrics and improvement proposals",
            "Launching an MVP micro-SaaS or campus app and tracking retention through Amplitude analytics"
        ],
        "interview_topics": [
            "Product design questions ('How would you design an ATM for children?')",
            "Analytical trade-offs ('Metrics show feature X increased engagement by 5% but lowered retention by 2%, what do you do?')",
            "Behavioral conflict resolution between engineering leads and marketing directors"
        ]
    },
    {
        "id": "data-analyst",
        "title": "Business & Data Analyst",
        "category": "Artificial Intelligence & Data",
        "description": "Transform raw numbers and database queries into executive dashboards, KPIs, and operational business intelligence.",
        "overview": "Data Analysts make enterprise data understandable and actionable. They write complex SQL queries, build interactive dashboards using Power BI or Tableau, and collaborate with business leaders to evaluate performance, revenue, and customer behavior.",
        "holland_codes": ["C", "I", "E"],
        "required_skills": [
            "SQL (PostgreSQL/MySQL)", "Power BI / Tableau", "Excel (Advanced Pivot, VLOOKUP)",
            "Data Cleaning", "Data Visualization", "Business Metrics (KPIs, ROI)",
            "Python (Pandas) Basics"
        ],
        "secondary_skills": [
            "Statistics Basics", "Data Warehousing (Snowflake/BigQuery)",
            "Storytelling with Data", "ETL Pipelines", "Google Analytics"
        ],
        "interests": [
            "Data Visualization", "Business Intelligence", "Market Trends",
            "Financial Reporting", "Process Optimization"
        ],
        "education": {
            "degrees": ["Bachelor's", "Associate's"],
            "majors": ["Information Systems", "Economics", "Business Analytics", "Mathematics", "Computer Science"],
            "min_gpa": 2.7
        },
        "work_style": ["Remote", "Hybrid", "On-site"],
        "salaries": {
            "entry_usd": 68000,
            "mid_usd": 98000,
            "senior_usd": 132000,
            "entry_inr": "₹5 - ₹10 LPA",
            "mid_inr": "₹12 - ₹22 LPA",
            "senior_inr": "₹24 - ₹42 LPA"
        },
        "market_outlook": {
            "growth_rate": "25% (Much faster than average)",
            "demand": "Very High",
            "openings": "300,000+ globally"
        },
        "top_companies": ["Deloitte", "Accenture", "EY", "KPMG", "Amazon", "Target", "Capital One"],
        "certifications": [
            "Microsoft Certified: Power BI Data Analyst Associate (PL-300)",
            "Google Data Analytics Professional Certificate",
            "Tableau Desktop Specialist"
        ],
        "learning_roadmap": [
            {
                "phase": "Phase 1: Advanced Excel & SQL Foundations (Months 1-3)",
                "focus": "Data manipulation, Pivot tables, JOINS, GROUP BY, CTEs, Window Functions",
                "topics": ["Complex relational querying, data aggregation, data formatting"],
                "free_resources": ["SQLZoo", "Alex The Analyst YouTube series", "Excel Easy"]
            },
            {
                "phase": "Phase 2: BI Dashboards & Visualization (Months 4-6)",
                "focus": "Power BI / Tableau DAX, visual storytelling, drill-down reports",
                "topics": ["Data modeling, relationships, star schema, DAX measures, automated refreshes"],
                "free_resources": ["Microsoft Learn Power BI Track", "Tableau Public Community Projects"]
            },
            {
                "phase": "Phase 3: Python for Analytics & Business Cases (Months 7-9)",
                "focus": "Automating reports with Pandas, communicating findings to executives",
                "topics": ["Jupyter notebooks, Seaborn graphs, executive presentation slide decks"],
                "free_resources": ["Kaggle Data Analytics track", "DataCamp open tutorials"]
            }
        ],
        "project_ideas": [
            "Executive Sales & Profitability Dashboard in Power BI with interactive regional drilldowns",
            "Retail Customer Cohort & RFM (Recency, Frequency, Monetary) Segmentation using SQL & Python",
            "HR Attrition and Compensation Analysis Report with actionable retention recommendations"
        ],
        "interview_topics": [
            "Live SQL challenge: writing window functions (`ROW_NUMBER()`, `RANK()`, `LEAD/LAG`)",
            "Explaining the difference between Star Schema and Snowflake Schema in data modeling",
            "How would you communicate a decline in quarter-over-quarter customer retention to non-technical managers"
        ]
    },
    {
        "id": "mobile-app-developer",
        "title": "Mobile Application Developer (iOS / Android / Flutter)",
        "category": "Software Engineering & Web",
        "description": "Design and engineer responsive, high-performance mobile apps for millions of smartphone users worldwide.",
        "overview": "Mobile Developers build native or cross-platform apps using Flutter, React Native, Swift (iOS), or Kotlin (Android). They ensure smooth gestures, offline data caching, camera and hardware integration, and store publishing.",
        "holland_codes": ["R", "A", "I"],
        "required_skills": [
            "Flutter / React Native", "Dart / TypeScript / Kotlin / Swift",
            "Mobile UI Design & Guidelines (Material / HIG)", "RESTful APIs Integration",
            "State Management (Bloc/Provider/Redux)", "Git", "Local Storage (SQLite/Room/Hive)"
        ],
        "secondary_skills": [
            "Push Notifications (FCM)", "App Store & Play Store Deployment",
            "Performance Optimization", "Firebase", "Offline Sync"
        ],
        "interests": [
            "Mobile Technology", "App Design", "User Interface Motion",
            "Hardware Sensors", "Cross-Platform Ecosystems"
        ],
        "education": {
            "degrees": ["Bachelor's", "Bootcamp / Self-Taught"],
            "majors": ["Computer Science", "Software Engineering", "Information Technology"],
            "min_gpa": 2.7
        },
        "work_style": ["Remote", "Hybrid", "On-site"],
        "salaries": {
            "entry_usd": 82000,
            "mid_usd": 124000,
            "senior_usd": 165000,
            "entry_inr": "₹6 - ₹13 LPA",
            "mid_inr": "₹15 - ₹30 LPA",
            "senior_inr": "₹32 - ₹60 LPA"
        },
        "market_outlook": {
            "growth_rate": "23% (Much faster than average)",
            "demand": "High",
            "openings": "160,000+ globally"
        },
        "top_companies": ["Uber", "Instagram", "Duolingo", "DoorDash", "Spotify", "Snapchat"],
        "certifications": [
            "Google Associate Android Developer",
            "Meta React Native Specialization",
            "App Development with Swift Certified User"
        ],
        "learning_roadmap": [
            {
                "phase": "Phase 1: Language & Core Mobile Concepts (Months 1-3)",
                "focus": "Dart/Kotlin/Swift syntax, View lifecycles, Responsive mobile layouts",
                "topics": ["Widget trees, event handlers, navigation stacks, device permissions"],
                "free_resources": ["Flutter Official Codelabs", "Android Basics with Compose", "Apple Developer Tutorials"]
            },
            {
                "phase": "Phase 2: State Management & API Networking (Months 4-6)",
                "focus": "Bloc/Provider/Riverpod, Async HTTP calls, JSON deserialization",
                "topics": ["Clean architecture, caching layers, offline-first mobile apps"],
                "free_resources": ["Reso Coder Flutter clean architecture", "Philipp Lackner Android Architecture"]
            },
            {
                "phase": "Phase 3: Production, Hardware & App Stores (Months 7-9)",
                "focus": "Camera, GPS geolocation, in-app purchases, CI/CD with Fastlane",
                "topics": ["App Store Review Guidelines, memory leak profiling, animations"],
                "free_resources": ["Fastlane docs", "Google Play Academy"]
            }
        ],
        "project_ideas": [
            "Offline-First Personal Finance & Expense Tracker with Biometric Auth and Chart Visuals",
            "Social Fitness Tracking App with GPS Map Routes and Community Leaderboards",
            "Real-Time Chat & Media Sharing Mobile App with Firebase Firestore and Push Notifications"
        ],
        "interview_topics": [
            "Deep dive into mobile app lifecycles (onCreate, onResume, onPause, onDestroy)",
            "Handling race conditions in asynchronous network requests on mobile devices",
            "Cross-platform performance optimization: minimizing re-renders and memory footprints"
        ]
    },
    {
        "id": "blockchain-developer",
        "title": "Blockchain & Web3 Engineer",
        "category": "Emerging Technologies",
        "description": "Architect decentralized applications (dApps), smart contracts, and cryptographic protocols for secure peer-to-peer systems.",
        "overview": "Blockchain Developers create smart contracts using Solidity or Rust and integrate Web3 applications with Ethereum, Solana, and Layer 2 rollups. They specialize in decentralized finance (DeFi), tokenomics, and zero-knowledge cryptography.",
        "holland_codes": ["I", "R", "C"],
        "required_skills": [
            "Solidity / Rust", "Smart Contract Development", "Ethereum / EVM Architecture",
            "Ethers.js / Web3.js", "Hardhat / Foundry", "Cryptography Basics", "Git"
        ],
        "secondary_skills": [
            "React / Next.js", "Smart Contract Auditing & Security", "Zero Knowledge Proofs",
            "IPFS", "DeFi Protocols", "Layer 2 Scaling"
        ],
        "interests": [
            "Decentralization", "Cryptocurrency", "Cryptography",
            "Smart Contracts", "Financial Sovereignty", "Peer-to-Peer Networks"
        ],
        "education": {
            "degrees": ["Bachelor's", "Self-Taught / Open Source Contributor"],
            "majors": ["Computer Science", "Cryptography", "Software Engineering"],
            "min_gpa": 2.9
        },
        "work_style": ["Remote", "Hybrid"],
        "salaries": {
            "entry_usd": 95000,
            "mid_usd": 150000,
            "senior_usd": 205000,
            "entry_inr": "₹10 - ₹18 LPA",
            "mid_inr": "₹22 - ₹45 LPA",
            "senior_inr": "₹48 - ₹90 LPA"
        },
        "market_outlook": {
            "growth_rate": "27% (High volatility, strong specialty demand)",
            "demand": "High",
            "openings": "45,000+ globally"
        },
        "top_companies": ["Consensys", "Chainlink", "Polygon", "Solana Foundation", "Coinbase", "Uniswap"],
        "certifications": [
            "Certified Blockchain Developer (Ethereum)",
            "Chainlink Developer Certification",
            "Blockchain Council Certified Solidity Developer"
        ],
        "learning_roadmap": [
            {
                "phase": "Phase 1: Cryptography & EVM Fundamentals (Months 1-3)",
                "focus": "SHA-256, Public/Private keys, Merkle trees, Consensus mechanisms (PoS)",
                "topics": ["How Ethereum works under the hood, gas mechanics, account types"],
                "free_resources": ["Mastering Ethereum (Andreas Antonopoulos)", "Ethereum.org Developer docs"]
            },
            {
                "phase": "Phase 2: Solidity & Smart Contract Security (Months 4-6)",
                "focus": "Foundry, Hardhat, ERC-20, ERC-721, Reentrancy attacks",
                "topics": ["Writing secure smart contracts, unit testing with Foundry, OpenZeppelin standards"],
                "free_resources": ["CryptoZombies", "SpeedRunEthereum (Austin Griffith)", "Damn Vulnerable DeFi"]
            },
            {
                "phase": "Phase 3: Full Stack dApp & DeFi Protocols (Months 7-9)",
                "focus": "Next.js frontend + Wagmi / Viem hooks, smart contract auditing",
                "topics": ["Automated market makers (AMM), staking pools, decentralized storage with IPFS"],
                "free_resources": ["Patrick Collins Foundry & Solidity Course (32 hours)", "RareSkills blog"]
            }
        ],
        "project_ideas": [
            "Decentralized Crowdfunding Platform with automated escrow and milestone payout voting",
            "Automated Liquidity Pool & Token Swap dApp with real-time price feeds via Chainlink oracles",
            "NFT Ticketing dApp with fraud prevention and dynamic metadata updates"
        ],
        "interview_topics": [
            "Deep dive into reentrancy attacks, frontrunning, and how to implement ReentrancyGuard",
            "Gas optimization strategies: storage packing, custom errors, immutable variables",
            "The trade-offs between Optimistic Rollups and ZK-Rollups for Layer 2 scaling"
        ]
    },
    {
        "id": "embedded-iot-engineer",
        "title": "Embedded Systems & IoT Engineer",
        "category": "Hardware & Systems Engineering",
        "description": "Develop firmware and software that bridges microcontrollers, sensors, connected IoT devices, and cloud backends.",
        "overview": "Embedded Systems Engineers program microcontrollers (ARM, ESP32, STM32) using C and C++. They interface with sensors, actuators, and communication protocols (MQTT, BLE, I2C) to build smart automotive systems, wearables, and industrial robots.",
        "holland_codes": ["R", "I", "C"],
        "required_skills": [
            "Embedded C / C++", "Microcontrollers (STM32, ESP32, Arduino)",
            "Communication Protocols (UART, SPI, I2C, CAN)", "RTOS (FreeRTOS)",
            "Circuit Debugging & Oscilloscopes", "Git", "Linux Kernel / Device Drivers"
        ],
        "secondary_skills": [
            "Python", "MQTT / BLE / Wi-Fi Protocols", "PCB Design (KiCad)",
            "IoT Cloud Platforms (AWS IoT)", "Low-power Optimization"
        ],
        "interests": [
            "Hardware Hacking", "Robotics", "Connected Devices",
            "Automotive Tech", "Smart Home Automation", "Low-Level Programming"
        ],
        "education": {
            "degrees": ["Bachelor's", "Master's"],
            "majors": ["Electrical Engineering", "Electronics & Communication", "Computer Engineering"],
            "min_gpa": 3.0
        },
        "work_style": ["On-site", "Hybrid"],
        "salaries": {
            "entry_usd": 85000,
            "mid_usd": 125000,
            "senior_usd": 168000,
            "entry_inr": "₹7 - ₹14 LPA",
            "mid_inr": "₹16 - ₹32 LPA",
            "senior_inr": "₹34 - ₹62 LPA"
        },
        "market_outlook": {
            "growth_rate": "21% (Faster than average)",
            "demand": "High",
            "openings": "120,000+ globally"
        },
        "top_companies": ["Tesla", "Bosch", "Texas Instruments", "Qualcomm", "Intel", "Apple", "NXP Semiconductors"],
        "certifications": [
            "Arm Certified Engineer",
            "AWS Certified IoT Core Specialty",
            "Embedded Systems Professional Certificate"
        ],
        "learning_roadmap": [
            {
                "phase": "Phase 1: C Programming & Bare Metal Registers (Months 1-3)",
                "focus": "Pointers, memory management, bitwise operations, GPIO manipulation",
                "topics": ["Memory mapping, interrupts, timer modules, ADC/DAC conversions"],
                "free_resources": ["FastBit Embedded Brain Academy", "Embedded Systems by edX (UT Austin)"]
            },
            {
                "phase": "Phase 2: Communication Protocols & RTOS (Months 4-6)",
                "focus": "I2C, SPI, UART, FreeRTOS tasks, semaphores, queues",
                "topics": ["Priority inversion, task synchronization, multi-threaded firmware"],
                "free_resources": ["FreeRTOS official book & documentation", "ESP-IDF guides"]
            },
            {
                "phase": "Phase 3: IoT Connectivity & Low-Power Design (Months 7-9)",
                "focus": "MQTT, BLE mesh, sleep modes, AWS IoT Greengrass",
                "topics": ["Battery life optimization, Over-The-Air (OTA) firmware updates, hardware encryption"],
                "free_resources": ["AWS IoT Core tutorials", "KiCad PCB Design tutorials"]
            }
        ],
        "project_ideas": [
            "Smart Environmental Monitoring Station with ESP32 transmitting telemetry via MQTT to Cloud",
            "Real-Time FreeRTOS Sensor Hub with I2C OLED display, BLE sync and low-power deep sleep",
            "CAN Bus Automotive Diagnostic Scanner using Arduino and ELM327 protocol"
        ],
        "interview_topics": [
            "Volatile keyword in C and race condition avoidance in interrupt service routines (ISR)",
            "Debugging I2C bus collision, pull-up resistor calculation, and baud rate drift",
            "Memory constraints: stack vs heap allocation in safety-critical firmware"
        ]
    },
    {
        "id": "bioinformatics-scientist",
        "title": "Bioinformatics & Health Data Scientist",
        "category": "Healthcare & Biotechnology",
        "description": "Analyze genomic sequences, molecular data, and clinical datasets using computational algorithms to accelerate drug discovery.",
        "overview": "Bioinformaticians apply machine learning and computational statistics to massive biological data. They analyze DNA/RNA sequencing data, model protein structures (AlphaFold), and help medical teams deliver precision medicine.",
        "holland_codes": ["I", "R", "C"],
        "required_skills": [
            "Python / Biopython", "R (Bioconductor)", "Next-Generation Sequencing (NGS) Analysis",
            "Linux / High Performance Computing (HPC)", "Statistical Genetics",
            "SQL & Biological Databases (NCBI, Ensembl)", "Git"
        ],
        "secondary_skills": [
            "Machine Learning / Deep Learning", "Molecular Dynamics", "Docker / Nextflow",
            "Protein Structure Modeling (AlphaFold)", "Bash Scripting"
        ],
        "interests": [
            "Genomics", "Biotechnology", "Precision Medicine",
            "Computational Biology", "Drug Discovery", "Genetics"
        ],
        "education": {
            "degrees": ["Master's", "Ph.D.", "Bachelor's"],
            "majors": ["Bioinformatics", "Computational Biology", "Biomedical Engineering", "Biotechnology"],
            "min_gpa": 3.2
        },
        "work_style": ["Hybrid", "Remote", "On-site"],
        "salaries": {
            "entry_usd": 88000,
            "mid_usd": 132000,
            "senior_usd": 172000,
            "entry_inr": "₹7 - ₹15 LPA",
            "mid_inr": "₹16 - ₹32 LPA",
            "senior_inr": "₹35 - ₹65 LPA"
        },
        "market_outlook": {
            "growth_rate": "29% (Much faster than average)",
            "demand": "High",
            "openings": "65,000+ globally"
        },
        "top_companies": ["Illumina", "Genentech", "Pfizer", "Broad Institute", "AstraZeneca", "Moderna"],
        "certifications": [
            "Bioinformatics Specialization (UC San Diego / Coursera)",
            "Genomic Data Science Specialization (Johns Hopkins)",
            "Nextflow Certified Pipeline Developer"
        ],
        "learning_roadmap": [
            {
                "phase": "Phase 1: Molecular Biology & Biopython (Months 1-3)",
                "focus": "Central dogma, FASTA/FASTQ file parsing, Biopython, sequence alignment",
                "topics": ["Smith-Waterman algorithm, BLAST, manipulating DNA/Protein sequences with code"],
                "free_resources": ["Rosalind.info (Bioinformatics problem sets)", "Biopython Tutorial & Cookbook"]
            },
            {
                "phase": "Phase 2: NGS Pipelines & R Bioconductor (Months 4-6)",
                "focus": "RNA-seq differential gene expression, variant calling, GATK",
                "topics": ["Quality control with FastQC, alignment with Bowtie/BWA, DESeq2 in R"],
                "free_resources": ["Harvard Chan Bioinformatics Core training modules", "Bioconductor tutorials"]
            },
            {
                "phase": "Phase 3: Machine Learning in Genomics & Nextflow (Months 7-9)",
                "focus": "Predictive models on clinical datasets, reproducible pipelines with Nextflow/Docker",
                "topics": ["DeepChem, AlphaFold structural analysis, biomarker classification"],
                "free_resources": ["Nextflow Carpentry training", "DeepLearning in Genomics open lectures"]
            }
        ],
        "project_ideas": [
            "Automated RNA-Seq Differential Expression Pipeline packaged with Nextflow & Docker",
            "Cancer Subtype Classification using Machine Learning on TCGA (The Cancer Genome Atlas) datasets",
            "CRISPR On-Target Efficiency Prediction Model trained on genomic features"
        ],
        "interview_topics": [
            "Explaining read mapping and how to handle multi-mapping reads in NGS data",
            "Normalizing RNA-seq counts: TPM vs RPKM vs DESeq2 median of ratios",
            "How to detect and control for batch effects in multi-center clinical trials"
        ]
    },
    {
        "id": "game-developer",
        "title": "Game Programmer (Unity / Unreal Engine)",
        "category": "Game Development & Graphics",
        "description": "Program real-time physics, graphics rendering, multiplayer networking, and gameplay mechanics for 3D/2D games.",
        "overview": "Game Developers combine computer graphics, linear algebra, performance optimization, and creative gameplay mechanics using C++ or C# with Unreal Engine or Unity.",
        "holland_codes": ["A", "R", "I"],
        "required_skills": [
            "C++ / C#", "Unity / Unreal Engine", "3D Math & Linear Algebra",
            "Game Physics & Collisions", "Data Structures & Algorithms", "Git"
        ],
        "secondary_skills": [
            "Shaders (GLSL/HLSL)", "Multiplayer Networking (Photon/WebSockets)",
            "Blender Basics", "Memory Optimization", "AI Behaviors (Behavior Trees)"
        ],
        "interests": [
            "Video Games", "Interactive 3D Graphics", "Virtual Reality (VR/AR)",
            "Creative Coding", "Physics Simulation"
        ],
        "education": {
            "degrees": ["Bachelor's", "Game Development Degree / Portfolio"],
            "majors": ["Computer Science", "Game Design & Development", "Software Engineering"],
            "min_gpa": 2.8
        },
        "work_style": ["Hybrid", "On-site", "Remote"],
        "salaries": {
            "entry_usd": 78000,
            "mid_usd": 118000,
            "senior_usd": 160000,
            "entry_inr": "₹6 - ₹12 LPA",
            "mid_inr": "₹14 - ₹28 LPA",
            "senior_inr": "₹30 - ₹55 LPA"
        },
        "market_outlook": {
            "growth_rate": "18% (Steady Growth)",
            "demand": "High",
            "openings": "85,000+ globally"
        },
        "top_companies": ["Epic Games", "Electronic Arts (EA)", "Ubisoft", "Riot Games", "Sony PlayStation", "Unity Technologies"],
        "certifications": [
            "Unity Certified Associate: Game Developer",
            "Unreal Engine Certified Creator"
        ],
        "learning_roadmap": [
            {
                "phase": "Phase 1: C++ / C# Foundations & Vectors (Months 1-3)",
                "focus": "Object-oriented programming, memory pointers, vector math, quaternions",
                "topics": ["Dot/cross products, collision detection geometry, game loop architecture"],
                "free_resources": ["GameDev.tv C# & Unity courses", "Learn C++ (learncpp.com)"]
            },
            {
                "phase": "Phase 2: Gameplay Systems & AI (Months 4-6)",
                "focus": "State machines, behavior trees, particle systems, pathfinding (A*)",
                "topics": ["Animation blending, sound integration, inventory and quest systems"],
                "free_resources": ["Brackeys Unity Archives", "Unreal Engine Online Learning Portal"]
            },
            {
                "phase": "Phase 3: Multiplayer Networking & Optimization (Months 7-9)",
                "focus": "Client-server prediction, lag compensation, draw call batching, memory profiling",
                "topics": ["Photon PUN/Mirror, GPU profiling, publish game build on Steam or Itch.io"],
                "free_resources": ["Valve Developer Community Wiki", "Gabriel Gambetta Fast-Paced Multiplayer guides"]
            }
        ],
        "project_ideas": [
            "Multiplayer 3D Arena Brawler with rollback netcode and server authoritative physics",
            "Procedural Dungeon Crawler with custom room generation algorithms and enemy AI",
            "Custom Shader Pack with real-time water refraction, stylized cel-shading, and volumetric fog"
        ],
        "interview_topics": [
            "Garbage collection spikes in Unity/C# and how to use object pooling",
            "Explaining the dot product and cross product in game engine raycasting",
            "Client prediction vs server reconciliation in competitive multiplayer games"
        ]
    },
    {
        "id": "qa-automation-engineer",
        "title": "QA Automation & Test Architect (SDET)",
        "category": "Software Engineering & Web",
        "description": "Design automated end-to-end testing frameworks, load simulations, and CI/CD test gates to guarantee bug-free software.",
        "overview": "Software Development Engineers in Test (SDETs) build automated test suites using Selenium, Cypress, Playwright, and PyTest. They stress test enterprise backends, validate UI regressions, and ensure defect-free production deployments.",
        "holland_codes": ["C", "R", "I"],
        "required_skills": [
            "Python / Java / JavaScript", "Playwright / Cypress / Selenium",
            "API Testing (Postman / REST Assured)", "CI/CD Integration (GitHub Actions)",
            "Git", "Test Automation Frameworks (PyTest / JUnit)"
        ],
        "secondary_skills": [
            "Performance & Load Testing (JMeter / k6)", "Docker", "SQL",
            "Mobile Testing (Appium)", "Security Testing (OWASP ZAP)"
        ],
        "interests": [
            "Software Quality", "Bug Hunting", "Automation Pipelines",
            "Performance Benchmarking", "Code Reliability"
        ],
        "education": {
            "degrees": ["Bachelor's", "Associate's"],
            "majors": ["Computer Science", "Information Technology", "Software Engineering"],
            "min_gpa": 2.7
        },
        "work_style": ["Remote", "Hybrid", "On-site"],
        "salaries": {
            "entry_usd": 75000,
            "mid_usd": 112000,
            "senior_usd": 150000,
            "entry_inr": "₹6 - ₹12 LPA",
            "mid_inr": "₹14 - ₹26 LPA",
            "senior_inr": "₹28 - ₹50 LPA"
        },
        "market_outlook": {
            "growth_rate": "22% (Faster than average)",
            "demand": "High",
            "openings": "140,000+ globally"
        },
        "top_companies": ["Amazon", "Microsoft", "Salesforce", "Cisco", "PayPal", "Wipro"],
        "certifications": [
            "ISTQB Certified Tester Foundation Level (CTFL)",
            "Playwright Automation Professional",
            "AWS Certified Developer"
        ],
        "learning_roadmap": [
            {
                "phase": "Phase 1: Testing Fundamentals & Playwright (Months 1-3)",
                "focus": "Test pyramids, unit vs integration vs E2E, Playwright locators, assertions",
                "topics": ["Page Object Model (POM), handling dynamic elements, parallel test execution"],
                "free_resources": ["Playwright Official Documentation & Guides", "Test Automation University"]
            },
            {
                "phase": "Phase 2: API & Load Testing (Months 4-6)",
                "focus": "Postman collections, automated API regression with PyTest, k6 performance scripts",
                "topics": ["Status codes, payload schema validation, virtual user load spikes, latency SLOs"],
                "free_resources": ["k6.io Documentation", "Postman Student Expert Program"]
            },
            {
                "phase": "Phase 3: CI/CD Gates & Cloud Test Grids (Months 7-9)",
                "focus": "Dockerized test execution, GitHub Actions matrix builds, Allure reports",
                "topics": ["Automated test reporting, headless browser clusters, cross-browser grid"],
                "free_resources": ["GitHub Actions for QA course", "Docker for Automation"]
            }
        ],
        "project_ideas": [
            "Enterprise E2E Playwright Framework with Page Object Model and Allure HTML Reports",
            "Automated REST API Test Suite with PyTest validating 50+ endpoints with schema assertions",
            "Continuous Performance & Stress Testing Pipeline running k6 on PR commits"
        ],
        "interview_topics": [
            "Strategies for mitigating flaky automated tests in continuous integration pipelines",
            "Page Object Model architecture and maintainability trade-offs",
            "How to structure an automated regression test suite for microservices"
        ]
    },
    {
        "id": "nlp-genai-engineer",
        "title": "Generative AI & LLM Engineer",
        "category": "Artificial Intelligence & Data",
        "description": "Build intelligent autonomous agents, Retrieval-Augmented Generation (RAG) pipelines, and fine-tune foundation models.",
        "overview": "Generative AI Engineers specialize in state-of-the-art Large Language Models. They construct multi-agent reasoning systems, vector database search pipelines, prompt evaluation harnesses, and fine-tune open weights models (Llama, Mistral) for enterprise workflows.",
        "holland_codes": ["I", "R", "A"],
        "required_skills": [
            "Python", "LangChain / LlamaIndex", "Vector Databases (Chroma/Pinecone)",
            "Transformers / Hugging Face", "PyTorch", "Prompt Engineering & Evaluation",
            "FastAPI / REST APIs", "Git"
        ],
        "secondary_skills": [
            "Fine-Tuning (LoRA / QLoRA)", "Docker", "MLOps / vLLM",
            "Multi-Agent Frameworks (AutoGen / CrewAI)", "Deep Learning"
        ],
        "interests": [
            "Generative AI", "Large Language Models", "Autonomous Agents",
            "Natural Language Processing", "Vector Search"
        ],
        "education": {
            "degrees": ["Bachelor's", "Master's"],
            "majors": ["Computer Science", "Artificial Intelligence", "Data Science"],
            "min_gpa": 3.2
        },
        "work_style": ["Remote", "Hybrid"],
        "salaries": {
            "entry_usd": 105000,
            "mid_usd": 160000,
            "senior_usd": 215000,
            "entry_inr": "₹14 - ₹24 LPA",
            "mid_inr": "₹28 - ₹55 LPA",
            "senior_inr": "₹60 - ₹110 LPA"
        },
        "market_outlook": {
            "growth_rate": "48% (Explosive Growth)",
            "demand": "Extremely High",
            "openings": "120,000+ globally"
        },
        "top_companies": ["OpenAI", "Anthropic", "Google DeepMind", "Meta AI", "Microsoft", "Mistral AI", "Cohere"],
        "certifications": [
            "DeepLearning.AI Generative AI with LLMs",
            "Hugging Face NLP Course Certification",
            "AWS Certified Machine Learning"
        ],
        "learning_roadmap": [
            {
                "phase": "Phase 1: Embeddings & Vector Search (Months 1-3)",
                "focus": "Dense representations, cosine similarity, semantic chunking, ChromaDB",
                "topics": ["Hugging Face Transformers pipeline, tokenization, OpenAI API integration"],
                "free_resources": ["DeepLearning.AI Short Courses (Andrew Ng)", "Hugging Face NLP Course"]
            },
            {
                "phase": "Phase 2: Advanced RAG & Multi-Agent Systems (Months 4-6)",
                "focus": "Hybrid search (BM25 + Dense), re-ranking, LangChain, CrewAI multi-agent swarms",
                "topics": ["Prompt evaluation metrics (RAGAS), hallucination detection, function calling"],
                "free_resources": ["LangChain Academy", "LlamaIndex official tutorials"]
            },
            {
                "phase": "Phase 3: Fine-Tuning & High-Throughput Serving (Months 7-9)",
                "focus": "LoRA, QLoRA, vLLM / Ollama deployment, quantization (GGUF, AWQ)",
                "topics": ["Instruction fine-tuning datasets, GPU memory budgeting, deployment on AWS/RunPod"],
                "free_resources": ["Axolotl / Unsloth fine-tuning guides", "Full Stack LLM Bootcamp"]
            }
        ],
        "project_ideas": [
            "Production RAG Knowledge Assistant with Hybrid Search, Cohere Re-Ranking, and Streaming UI",
            "Autonomous Research Agent Swarm that synthesizes arXiv papers into executive briefings",
            "Domain-Adapted Specialized Medical/Legal LLM fine-tuned using QLoRA and evaluated with RAGAS"
        ],
        "interview_topics": [
            "Comparing RAG vs Fine-Tuning: Cost, latency, hallucination rate, and freshness tradeoffs",
            "Mathematical mechanics of FlashAttention and KV-Cache in transformer inference",
            "Optimizing token throughput using continuous batching and PagedAttention in vLLM"
        ]
    }
]

# Helper lookup dictionary
CAREER_MAP = {c["id"]: c for c in CAREERS}

def get_all_careers():
    return CAREERS

def get_career_by_id(career_id):
    return CAREER_MAP.get(career_id)

def get_career_categories():
    categories = sorted(list(set(c["category"] for c in CAREERS)))
    return categories
