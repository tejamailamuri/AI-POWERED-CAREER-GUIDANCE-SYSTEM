"""
Bio-Medical Waste Knowledge Base and Item Database.
Categorized strictly according to WHO (World Health Organization) and 
CPCB (Central Pollution Control Board) Bio-Medical Waste Management Rules.
"""

# Color-Coded Bin Specifications
BIN_SPECIFICATIONS = {
    "yellow": {
        "bin_name": "Yellow Bin (Infectious & Anatomical Waste)",
        "color_hex": "#eab308",
        "bg_class": "bg-yellow-500",
        "text_class": "text-yellow-700",
        "border_class": "border-yellow-400",
        "hazard_type": "Pathogenic / Highly Infectious / Biohazard",
        "treatment_method": "Incineration / Plasma Pyrolysis / Deep Burial",
        "description": "Human anatomical waste, soiled cotton, bandages, expired pharmaceuticals, chemical waste, and cytotoxic drugs.",
        "container_type": "Non-chlorinated yellow plastic bags with biohazard symbol"
    },
    "red": {
        "bin_name": "Red Bin (Contaminated Recyclable Plastics)",
        "color_hex": "#ef4444",
        "bg_class": "bg-red-500",
        "text_class": "text-red-700",
        "border_class": "border-red-400",
        "hazard_type": "Moderate Contamination / Recyclable Polymers",
        "treatment_method": "Autoclaving / Microwaving followed by Shredding & Plastic Recycling",
        "description": "Plastic disposable items like IV bottles, tubes, catheters, syringes without needles, surgical gloves, urine bags.",
        "container_type": "Non-chlorinated red plastic bags with biohazard symbol"
    },
    "white": {
        "bin_name": "White Translucent Container (Waste Sharps & Metals)",
        "color_hex": "#94a3b8",
        "bg_class": "bg-slate-400",
        "text_class": "text-slate-800",
        "border_class": "border-slate-400",
        "hazard_type": "Severe Physical Puncture / Blood-Borne Pathogen Transmission",
        "treatment_method": "Autoclaving / Dry Heat Sterilization followed by Shredding / Mutilation / Encapsulation",
        "description": "Needles, scalpels, surgical blades, contaminated needles with fixed syringes, metallic suture needles.",
        "container_type": "Puncture-proof, leak-proof, tamper-proof translucent white rigid containers"
    },
    "blue": {
        "bin_name": "Blue Cardboard / Bin (Glassware & Metal Implants)",
        "color_hex": "#3b82f6",
        "bg_class": "bg-blue-500",
        "text_class": "text-blue-700",
        "border_class": "border-blue-400",
        "hazard_type": "Physical Cut Hazard / Residual Chemical Contamination",
        "treatment_method": "Disinfection (Sodium Hypochlorite soaking) / Autoclaving & Glass Recycling",
        "description": "Medicine vials, ampoules (non-cytotoxic), glass slides, broken test tubes, metallic orthopedic implants.",
        "container_type": "Puncture-proof cardboard box / blue container with blue markings"
    },
    "general": {
        "bin_name": "Green / Black Bin (General Non-Infectious Municipal Waste)",
        "color_hex": "#22c55e",
        "bg_class": "bg-green-500",
        "text_class": "text-green-700",
        "border_class": "border-green-400",
        "hazard_type": "Non-Hazardous / Municipal Solid Waste",
        "treatment_method": "Municipal Composting / Sanitary Landfill / Material Recovery",
        "description": "Paper waste, sterile packaging boxes, food remnants, fruit peels, empty non-chemical plastic bottles.",
        "container_type": "Black or green garbage bag"
    }
}

# Extensive catalog of hospital items with category, description, physical traits, and risk
WASTE_ITEMS_CATALOG = [
    # YELLOW BIN ITEMS (Infectious, Soiled, Anatomical, Expired Meds)
    {
        "id": "item-y-01",
        "name": "Blood-Soiled Cotton Swabs & Gauze",
        "category": "yellow",
        "item_type": "Soiled Waste",
        "department": "Operation Theatre / Emergency",
        "hazard_rating": "High (Level 4)",
        "infection_risk": "Severe (Blood-borne pathogens)",
        "features": {
            "primary_color": "yellow_red_stain",
            "texture": "fibrous_soft",
            "aspect_ratio": "compact",
            "metallic": False
        },
        "handling_instructions": "Wear protective gloves; place immediately in yellow biohazard bag; do not touch with bare hands.",
        "treatment": "Incineration at >1100°C in certified central biomedical waste facility."
    },
    {
        "id": "item-y-02",
        "name": "Used Post-Op Surgical Bandages & Dressings",
        "category": "yellow",
        "item_type": "Soiled Waste",
        "department": "Surgical Ward / Wound Care",
        "hazard_rating": "High (Level 4)",
        "infection_risk": "High (Purulent discharge / blood)",
        "features": {
            "primary_color": "yellow_white_brown",
            "texture": "woven_fabric",
            "aspect_ratio": "elongated_strip",
            "metallic": False
        },
        "handling_instructions": "Fold inward to contain discharge; discard in yellow bag.",
        "treatment": "High-temperature incineration."
    },
    {
        "id": "item-y-03",
        "name": "Human Anatomical Tissue & Biopsy Specimens",
        "category": "yellow",
        "item_type": "Anatomical Waste",
        "department": "Pathology / Surgery",
        "hazard_rating": "Severe (Level 5)",
        "infection_risk": "Critical (Potential viral/bacterial vectors)",
        "features": {
            "primary_color": "red_pink",
            "texture": "organic_flesh",
            "aspect_ratio": "irregular",
            "metallic": False
        },
        "handling_instructions": "Preserve in formalin if required for histology; discard directly in yellow biohazard bag.",
        "treatment": "Incineration / Deep burial in designated zones."
    },
    {
        "id": "item-y-04",
        "name": "Expired Antibiotic & Discarded Medicine Tablets",
        "category": "yellow",
        "item_type": "Pharmaceutical Waste",
        "department": "Hospital Pharmacy / Wards",
        "hazard_rating": "Moderate (Chemical Toxicity)",
        "infection_risk": "Chemical hazard / environmental contamination",
        "features": {
            "primary_color": "multicolor_pills",
            "texture": "rigid_powder",
            "aspect_ratio": "small_capsules",
            "metallic": False
        },
        "handling_instructions": "Return unused/expired stocks to pharmacy for systematic incineration.",
        "treatment": "Incineration at >1200°C / encapsulation to prevent water table leaching."
    },
    {
        "id": "item-y-05",
        "name": "Discarded Blood Bag & Transfusion Tubing (Residual Blood)",
        "category": "yellow",
        "item_type": "Blood & Body Fluid Contaminated",
        "department": "Blood Bank / ICU",
        "hazard_rating": "High (Level 4)",
        "infection_risk": "Critical (HIV, HBV, HCV risk)",
        "features": {
            "primary_color": "deep_red_amber",
            "texture": "flexible_pouch",
            "aspect_ratio": "rectangular_bag",
            "metallic": False
        },
        "handling_instructions": "Seal clamp to prevent spillage; place inside heavy-gauge yellow bag.",
        "treatment": "Autoclaving followed by specialized incineration."
    },

    # RED BIN ITEMS (Contaminated Recyclable Plastics)
    {
        "id": "item-r-01",
        "name": "Used Surgical Latex / Nitrile Gloves",
        "category": "red",
        "item_type": "Contaminated Polymer",
        "department": "All Hospital Wards / OT",
        "hazard_rating": "Moderate (Level 3)",
        "infection_risk": "Surface viral/bacterial contamination",
        "features": {
            "primary_color": "blue_violet_white",
            "texture": "smooth_elastic",
            "aspect_ratio": "hand_glove",
            "metallic": False
        },
        "handling_instructions": "Peel off inside out to contain exterior contaminants; dispose in red bin.",
        "treatment": "Autoclaving/Microwaving followed by polymer shredding and recycling."
    },
    {
        "id": "item-r-02",
        "name": "Plastic IV Drip Bottle & Infusion Tubing (Saline/Dextrose)",
        "category": "red",
        "item_type": "Polymer Container & Tube",
        "department": "Inpatient Wards / ICU",
        "hazard_rating": "Low-Moderate (Level 2)",
        "infection_risk": "Low if no blood backflow; moderate surface contact",
        "features": {
            "primary_color": "translucent_clear",
            "texture": "semi_rigid_plastic",
            "aspect_ratio": "bottle_cylinder",
            "metallic": False
        },
        "handling_instructions": "Cut tubing with scissors to prevent illegal reuse; drain residual fluid; place in red bin.",
        "treatment": "Autoclaving and granulating for plastic recycling."
    },
    {
        "id": "item-r-03",
        "name": "Disposable Plastic Syringe Body (WITHOUT Needle)",
        "category": "red",
        "item_type": "Contaminated Plastic",
        "department": "Injection Room / Outpatient / Wards",
        "hazard_rating": "Moderate (Level 3)",
        "infection_risk": "Medication & bodily fluid residue",
        "features": {
            "primary_color": "clear_white_plunger",
            "texture": "rigid_polypropylene",
            "aspect_ratio": "cylinder_barrel",
            "metallic": False
        },
        "handling_instructions": "NEVER dispose needles here! Cut/destroy needle at hub using needle burner; place plastic barrel in red bin.",
        "treatment": "Autoclaving and plastic shredding."
    },
    {
        "id": "item-r-04",
        "name": "Urinary Catheter & Foley Urine Collection Bag",
        "category": "red",
        "item_type": "Contaminated Polymer",
        "department": "ICU / Post-Operative Ward",
        "hazard_rating": "Moderate-High (Level 3)",
        "infection_risk": "Urinary tract pathogen biohazard",
        "features": {
            "primary_color": "yellowish_translucent",
            "texture": "flexible_silicone",
            "aspect_ratio": "tubular_pouch",
            "metallic": False
        },
        "handling_instructions": "Empty urine into sluice drain; discard bag and silicone tube in red container.",
        "treatment": "Chemical disinfection or autoclaving and polymer shredding."
    },
    {
        "id": "item-r-05",
        "name": "Disposable Plastic Face Shield & Protective Apron",
        "category": "red",
        "item_type": "Personal Protective Equipment",
        "department": "Infection Isolation Ward",
        "hazard_rating": "Moderate (Level 2)",
        "infection_risk": "Aerosol droplet contamination",
        "features": {
            "primary_color": "transparent_blue_band",
            "texture": "flexible_film",
            "aspect_ratio": "sheet_flat",
            "metallic": False
        },
        "handling_instructions": "Fold contaminated side inward; discard into red bin.",
        "treatment": "Sterilization and plastic polymer recovery."
    },

    # WHITE BIN ITEMS (Sharps, Needles, Scalpels)
    {
        "id": "item-w-01",
        "name": "Hypodermic Injection Needles",
        "category": "white",
        "item_type": "Waste Sharps",
        "department": "Phlebotomy / Injection Clinic",
        "hazard_rating": "Extreme (Puncture Injury & Biohazard)",
        "infection_risk": "Severe (High transmission risk for HIV, Hepatitis B/C)",
        "features": {
            "primary_color": "metallic_silver",
            "texture": "sharp_rigid_steel",
            "aspect_ratio": "thin_needle",
            "metallic": True
        },
        "handling_instructions": "NEVER RECAP! Drop directly into puncture-proof translucent white sharps box.",
        "treatment": "Autoclaving/Dry heat sterilization followed by shredding / encapsulation."
    },
    {
        "id": "item-w-02",
        "name": "Surgical Scalpel Blade & Disposable Knife",
        "category": "white",
        "item_type": "Waste Sharps",
        "department": "Operation Theatre / Minor OT",
        "hazard_rating": "Extreme (Laceration & Pathogen Risk)",
        "infection_risk": "Severe (Direct blood contact)",
        "features": {
            "primary_color": "metallic_silver",
            "texture": "razor_sharp_steel",
            "aspect_ratio": "flat_tapered_blade",
            "metallic": True
        },
        "handling_instructions": "Use forceps to detach blade; deposit directly into white puncture-proof sharps box.",
        "treatment": "Dry heat sterilization and metal mutilation/melting."
    },
    {
        "id": "item-w-03",
        "name": "Contaminated Suture Needles & Needle Holders",
        "category": "white",
        "item_type": "Waste Sharps",
        "department": "Surgical Units / Trauma Care",
        "hazard_rating": "Extreme (Curved Needle Puncture)",
        "infection_risk": "Severe (Blood-borne pathogens)",
        "features": {
            "primary_color": "metallic_curved",
            "texture": "curved_sharp_wire",
            "aspect_ratio": "curved_arc",
            "metallic": True
        },
        "handling_instructions": "Count needles at end of surgery; dispose immediately in white sharps box.",
        "treatment": "Sterilization and metal recycling / encapsulation."
    },

    # BLUE BIN ITEMS (Glassware & Metal Implants)
    {
        "id": "item-b-01",
        "name": "Glass Medicine Vials (Antibiotic / Insulin)",
        "category": "blue",
        "item_type": "Glassware",
        "department": "Pharmacy / Wards",
        "hazard_rating": "Moderate (Laceration / Glass puncture)",
        "infection_risk": "Low-to-moderate residual medication contact",
        "features": {
            "primary_color": "amber_clear_glass",
            "texture": "smooth_rigid_glass",
            "aspect_ratio": "small_cylinder_bottle",
            "metallic": False
        },
        "handling_instructions": "Do not discard in regular trash or red bin! Place in blue cardboard/rigid box.",
        "treatment": "Sodium hypochlorite disinfection followed by glass recycling."
    },
    {
        "id": "item-b-02",
        "name": "Glass Ampoules with Broken Tips",
        "category": "blue",
        "item_type": "Glassware",
        "department": "Emergency / ICU / Anesthesia",
        "hazard_rating": "Moderate-High (Sharp Glass Cuts)",
        "infection_risk": "Chemical cut hazard",
        "features": {
            "primary_color": "clear_glass_broken",
            "texture": "sharp_jagged_glass",
            "aspect_ratio": "slender_glass_tube",
            "metallic": False
        },
        "handling_instructions": "Avoid touching broken neck; drop into blue puncture-proof container.",
        "treatment": "Chemical sterilization and glass furnace recycling."
    },
    {
        "id": "item-b-03",
        "name": "Orthopedic Metallic Body Implants & Screws",
        "category": "blue",
        "item_type": "Metallic Implants",
        "department": "Orthopedics / Trauma Surgery",
        "hazard_rating": "Low (Inert Titanium/Stainless Steel)",
        "infection_risk": "Surface biological contamination",
        "features": {
            "primary_color": "metallic_matte",
            "texture": "machined_metal",
            "aspect_ratio": "rod_plate_screw",
            "metallic": True
        },
        "handling_instructions": "Clean gross organic residue; place in blue puncture-proof container for metal recovery.",
        "treatment": "High-pressure autoclaving and metallurgical recycling."
    },

    # GENERAL / MUNICIPAL WASTE ITEMS (Green/Black Bin)
    {
        "id": "item-g-01",
        "name": "Medicine Packaging Cardboard & Drug Information Leaflets",
        "category": "general",
        "item_type": "General Dry Waste",
        "department": "All Wards / Reception",
        "hazard_rating": "None (Non-Hazardous)",
        "infection_risk": "Zero (Clean Packaging)",
        "features": {
            "primary_color": "white_cardboard",
            "texture": "paper_cardstock",
            "aspect_ratio": "folded_box",
            "metallic": False
        },
        "handling_instructions": "Flatten packaging box; deposit into general green/black bin.",
        "treatment": "Paper recycling / municipal waste recovery."
    },
    {
        "id": "item-g-02",
        "name": "Food Leftovers, Fruit Peels & Snack Wrappers",
        "category": "general",
        "item_type": "General Wet Waste",
        "department": "Hospital Cafeteria / Patient Rooms",
        "hazard_rating": "None (Biodegradable)",
        "infection_risk": "Zero (Non-Medical)",
        "features": {
            "primary_color": "organic_brown_green",
            "texture": "soft_organic",
            "aspect_ratio": "irregular_food",
            "metallic": False
        },
        "handling_instructions": "Dispose in green municipal bin for composting; never mix with hospital biohazard waste.",
        "treatment": "Aerobic composting / municipal waste management."
    }
]

def get_all_waste_items():
    return WASTE_ITEMS_CATALOG

def get_item_by_id(item_id):
    for item in WASTE_ITEMS_CATALOG:
        if item["id"] == item_id:
            return item
    return None

def get_bin_specs():
    return BIN_SPECIFICATIONS

