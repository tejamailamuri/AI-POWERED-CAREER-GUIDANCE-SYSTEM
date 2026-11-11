"""
Healthcare Worker Bio-Medical Waste Guidance, Protocols & Safety Knowledge Base.
Covers WHO guidelines, Needle-Stick Injury protocols, and staff training quizzes.
"""

from typing import Dict, Any, List

SAFETY_PROTOCOLS = {
    "needle_stick_injury": {
        "title": "Needle-Stick & Sharp Injury Immediate Protocol (PEP)",
        "urgency": "CRITICAL EMERGENCY - Act within 2 Hours",
        "steps": [
            {
                "step": 1,
                "action": "Immediate Copious Washing",
                "detail": "Wash the wound immediately under running tap water with soap for at least 3-5 minutes. Do NOT scrub vigorously."
            },
            {
                "step": 2,
                "action": "DO NOT SQUEEZE OR SUCK WOUND",
                "detail": "Never squeeze or suck the puncture site, as this causes localized micro-tissue trauma and enhances viral entry into blood vessels."
            },
            {
                "step": 3,
                "action": "Apply Antiseptic",
                "detail": "Cover with a sterile waterproof dressing or apply 70% ethyl alcohol / povidone iodine."
            },
            {
                "step": 4,
                "action": "Urgent Medical Incident Report",
                "detail": "Report immediately to Hospital Infection Control Nurse or Casualty Medical Officer within 1 hour."
            },
            {
                "step": 5,
                "action": "Post-Exposure Prophylaxis (PEP)",
                "detail": "Initiate PEP for HIV within 2 hours (effective up to 72 hours max) and check Hepatitis B surface antibody (anti-HBs) titers."
            }
        ]
    },
    "color_coding_rules": [
        {
            "bin": "YELLOW",
            "rule": "Infectious & Anatomical Waste ONLY",
            "dos": "Soiled cotton, blood-soaked gauze, anatomical tissues, expired medicines, blood bags.",
            "donts": "DO NOT throw needles, syringes, metallic sharps, or clean paper in yellow bags."
        },
        {
            "bin": "RED",
            "rule": "Contaminated Recyclable Plastics ONLY",
            "dos": "IV tubing, saline bottles, catheters, syringes WITHOUT needles, gloves, plastic aprons.",
            "donts": "NEVER throw needles, scalpel blades, or glass vials in red bags."
        },
        {
            "bin": "WHITE (TRANSLUCENT)",
            "rule": "Puncture-Proof Waste Sharps ONLY",
            "dos": "Hypodermic needles, scalpel blades, suture needles, contaminated metallic sharps.",
            "donts": "DO NOT overfill past 3/4 capacity. NEVER recap needles with two hands."
        },
        {
            "bin": "BLUE",
            "rule": "Glassware & Metallic Implants ONLY",
            "dos": "Medicine vials, glass ampoules, broken test tubes, orthopedic metal implants/screws.",
            "donts": "DO NOT put cytotoxic drug bottles or contaminated plastic IV sets here."
        }
    ]
}

STAFF_QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "A nurse finishes administering an IV injection. Where should the plastic syringe barrel (without needle) be disposed?",
        "options": [
            {"text": "Red Bin (Contaminated Recyclable Plastics)", "correct": True},
            {"text": "Yellow Bin (Infectious Waste)", "correct": False},
            {"text": "White Sharps Container", "correct": False},
            {"text": "General Green Bin", "correct": False}
        ],
        "explanation": "Plastic syringes (without needles) belong in the RED bin for autoclaving and polymer recycling."
    },
    {
        "id": 2,
        "question": "Where should a used surgical scalpel blade or hypodermic needle be placed immediately?",
        "options": [
            {"text": "Yellow Biohazard Plastic Bag", "correct": False},
            {"text": "White Puncture-Proof Translucent Sharps Box", "correct": True},
            {"text": "Blue Cardboard Box", "correct": False},
            {"text": "Red Plastic Waste Bin", "correct": False}
        ],
        "explanation": "All needles, scalpels, and sharp metal instruments must be deposited directly into puncture-proof WHITE containers."
    },
    {
        "id": 3,
        "question": "A patient's abdominal dressing is soaked with purulent drainage and blood. Which bin is correct?",
        "options": [
            {"text": "Yellow Bin (Soiled Biohazard Waste)", "correct": True},
            {"text": "Red Bin (Plastics)", "correct": False},
            {"text": "Blue Bin (Glassware)", "correct": False},
            {"text": "General Municipal Bin", "correct": False}
        ],
        "explanation": "Items contaminated with blood, pus, or body fluids (gauze, swabs, dressings) must go into the YELLOW bin for incineration."
    },
    {
        "id": 4,
        "question": "Where should empty glass antibiotic vials and glass ampoules be disposed?",
        "options": [
            {"text": "Blue Cardboard / Bin (Glassware)", "correct": True},
            {"text": "Yellow Biohazard Bag", "correct": False},
            {"text": "Red Recyclable Polymer Bin", "correct": False},
            {"text": "General Municipal Trash", "correct": False}
        ],
        "explanation": "Glass medicine vials and ampoules are collected in BLUE puncture-proof boxes for chemical disinfection and glass furnace recycling."
    }
]

def get_safety_protocols():
    return SAFETY_PROTOCOLS

def get_staff_quiz():
    return STAFF_QUIZ_QUESTIONS

