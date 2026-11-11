"""
Digital Waste Manifest, Tracking Barcode & Hospital Audit Registry.
Complies with WHO and CPCB Bio-Medical Waste tracking mandates.
"""

from typing import Dict, Any, List
import datetime
import random

DEFAULT_MANIFEST_LOGS = [
    {
        "manifest_id": "BMW-2026-8901",
        "timestamp": "2026-11-01 08:35 AM",
        "department": "Operation Theatre 2 (General Surgery)",
        "item_name": "Blood-Soiled Gauze & Laparotomy Sponges",
        "category": "yellow",
        "category_label": "Yellow (Infectious)",
        "weight_kg": 2.45,
        "hazard_level": "High Biohazard",
        "treatment_facility": "Apex Eco-Care CBWTF Incineration Plant",
        "nurse_badge": "RN-4029 (Sister Anjali)",
        "barcode": "BARCODE*BMW20268901*YEL*2.45KG",
        "status": "Transferred to Central Storage"
    },
    {
        "manifest_id": "BMW-2026-8902",
        "timestamp": "2026-11-01 09:12 AM",
        "department": "Emergency Trauma Unit",
        "item_name": "Hypodermic Injection Needles & Lancets",
        "category": "white",
        "category_label": "White (Sharps Safe)",
        "weight_kg": 0.85,
        "hazard_level": "Extreme Puncture Risk",
        "treatment_facility": "Apex Eco-Care CBWTF Autoclave & Shredder",
        "nurse_badge": "RN-1184 (Nurse David)",
        "barcode": "BARCODE*BMW20268902*WHT*0.85KG",
        "status": "Sealed in Puncture-Proof Box"
    },
    {
        "manifest_id": "BMW-2026-8903",
        "timestamp": "2026-11-01 10:04 AM",
        "department": "Intensive Care Unit (ICU-A)",
        "item_name": "Saline IV Infusion Bottles & Catheters",
        "category": "red",
        "category_label": "Red (Contaminated Plastic)",
        "weight_kg": 3.10,
        "hazard_level": "Moderate Polymer Residue",
        "treatment_facility": "GreenEarth Medical Recyclers",
        "nurse_badge": "RN-3312 (Sister Priya)",
        "barcode": "BARCODE*BMW20268903*RED*3.10KG",
        "status": "Disinfected & Tagged"
    },
    {
        "manifest_id": "BMW-2026-8904",
        "timestamp": "2026-11-01 10:45 AM",
        "department": "Pathology & Blood Testing Lab",
        "item_name": "Glass Antibiotic Vials & Culture Ampoules",
        "category": "blue",
        "category_label": "Blue (Glassware)",
        "weight_kg": 1.60,
        "hazard_level": "Physical Cut / Glassware",
        "treatment_facility": "Apex Eco-Care Glass Sterilization Unit",
        "nurse_badge": "LAB-5521 (Tech Rahul)",
        "barcode": "BARCODE*BMW20268904*BLU*1.60KG",
        "status": "Box Sealed with Blue Tag"
    }
]

class ManifestManager:
    def __init__(self):
        self.logs: List[Dict[str, Any]] = list(DEFAULT_MANIFEST_LOGS)

    def add_manifest_entry(self, entry: Dict[str, Any]) -> Dict[str, Any]:
        """Creates a verified digital manifest record for a segregated item."""
        new_id = f"BMW-2026-{random.randint(1000, 9999)}"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
        category = entry.get("category", "yellow").lower()

        cat_labels = {
            "yellow": "Yellow (Infectious)",
            "red": "Red (Contaminated Plastic)",
            "white": "White (Sharps Safe)",
            "blue": "Blue (Glassware)",
            "general": "Green/Black (General)"
        }

        facilities = {
            "yellow": "Central Hospital Incinerator (Temp >1100°C)",
            "red": "Certified Polymer Autoclave & Shredder Unit",
            "white": "Dry-Heat Encapsulation & Mutilation Plant",
            "blue": "Glass Sodium Hypochlorite Neutralization Facility",
            "general": "Municipal Solid Waste Recovery"
        }

        weight = round(float(entry.get("weight_kg", 0.45)), 2)

        record = {
            "manifest_id": new_id,
            "timestamp": timestamp,
            "department": entry.get("department", "Emergency / General Ward"),
            "item_name": entry.get("item_name", "Clinical Waste Item"),
            "category": category,
            "category_label": cat_labels.get(category, "Yellow (Infectious)"),
            "weight_kg": weight,
            "hazard_level": entry.get("hazard_level", "Standard Biohazard"),
            "treatment_facility": facilities.get(category, "Central Treatment Facility"),
            "nurse_badge": entry.get("nurse_badge", "RN-AUTO (Staff)"),
            "barcode": f"BMW*{new_id}*{category.upper()}*{weight}KG",
            "status": "Logged & Chute Dispatched"
        }

        self.logs.insert(0, record)
        return record

    def get_all_manifests(self, category: str = "", query: str = "") -> List[Dict[str, Any]]:
        """Returns filtered manifest audit trail."""
        results = self.logs
        if category:
            results = [r for r in results if r["category"].lower() == category.lower()]
        if query:
            q = query.lower()
            results = [
                r for r in results
                if q in r["manifest_id"].lower() or q in r["item_name"].lower() or q in r["department"].lower()
            ]
        return results

    def get_audit_summary(self) -> Dict[str, Any]:
        """Calculates total weight disposed per color category."""
        breakdown = {"yellow": 0.0, "red": 0.0, "white": 0.0, "blue": 0.0, "general": 0.0}
        total_items = len(self.logs)

        for log in self.logs:
            cat = log["category"]
            if cat in breakdown:
                breakdown[cat] = round(breakdown[cat] + log["weight_kg"], 2)

        total_weight = round(sum(breakdown.values()), 2)

        return {
            "total_records": total_items,
            "total_weight_kg": total_weight,
            "weight_breakdown": breakdown
        }

