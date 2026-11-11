# Smart MedWaste AI: Automated Bio-Medical Waste Segregation & IoT Monitoring System 🏥♻️

An intelligent, full-stack Hospital IoT and Computer Vision system designed to automate the classification, mechanical segregation, and compliance monitoring of hospital hazardous bio-medical waste according to **World Health Organization (WHO)** and **Central Pollution Control Board (CPCB)** guidelines.

---

## 🎯 Aim of the Project

> **The main aim of the Biomedical Waste Segregation System is to develop an efficient system for identifying and segregating biomedical waste into appropriate categories. The system aims to improve waste management in hospitals, laboratories, and healthcare facilities by ensuring the proper separation of different types of biomedical waste. It helps reduce the risk of infections, prevent environmental pollution, protect healthcare workers and the public, and promote safe and responsible biomedical waste disposal.**

---

### Key Objectives & Mission Pillars:
1. **Accurate Identification & Categorization:** Automatically classify hospital waste using Computer Vision and NLP into Yellow, Red, White, Blue, and General bins.
2. **Infection Risk Reduction:** Ensure pathological and infectious bio-waste is isolated without direct human contact to prevent viral/bacterial transmission.
3. **Protection of Healthcare Workers:** Eliminate sharps and needle-stick injuries with automated puncture-proof chute routing and 24/7 PPE safety guidance.
4. **Environmental Pollution Prevention:** Prevent toxic dioxin/furan emission by ensuring recyclable plastics (Red Bin) are never mixed into high-temperature incineration streams (Yellow Bin).
5. **Responsible Waste Disposal & Manifest Tracking:** Generate compliant digital manifests with barcodes, tracking total mass per category to meet WHO and CPCB statutory audits.

---

Improper segregation of bio-medical waste poses life-threatening risks to healthcare workers, sanitation staff, and public health:
- **Needle-stick & sharps injuries** transmit blood-borne pathogens (HIV, Hepatitis B, Hepatitis C).
- Mixing recyclable polymers (IV bottles, catheters) with pathological tissues leads to dioxin release during incineration.
- Manual segregation suffers from a **25%–40% error rate** during emergency clinical workflows.

**Smart MedWaste AI** solves this through an end-to-end automated system combining:
1. **AI Computer Vision Image Classification** for instant waste recognition.
2. **Automated Chute Flap Diverter (Servo Actuator)** routing items to the correct bin.
3. **IoT Smart Bin Telemetry** (Ultrasonic fill sensors, load cell mass, hazardous gas/ammonia detection).
4. **Digital Waste Manifest & Barcoding** for legal regulatory compliance.
5. **Staff Safety & Emergency Protocol Center** (Needle-Stick Injury PEP within 2 hours).

---

## 🛢️ Color-Coded Segregation Matrix (WHO & CPCB Standard)

| Bin Color | Waste Category | Examples | Mandated Treatment | Chute Servo Angle |
| :--- | :--- | :--- | :--- | :---: |
| 🟡 **Yellow** | **Infectious & Anatomical** | Soiled cotton/gauze, human tissue, expired antibiotics, blood bags | Incineration (>1100°C) / Plasma Pyrolysis | **0°** |
| 🔴 **Red** | **Contaminated Recyclable Plastics** | Disposable syringes (no needle), IV bottles, catheters, nitrile gloves | Autoclaving/Microwaving + Polymer Shredding | **45°** |
| ⚪ **White** | **Puncture-Proof Waste Sharps** | Hypodermic needles, scalpel blades, suture needles, lancets | Dry-Heat Sterilization + Encapsulation / Mutilation | **90°** |
| 🔵 **Blue** | **Glassware & Metal Implants** | Medicine vials, glass ampoules, broken test tubes, titanium implants | Disinfection (Sodium Hypochlorite) + Glass Recycling | **135°** |
| 🟢 **Green/Black** | **General Municipal Solid Waste** | Packaging cartons, paper leaflets, food scraps, clean water bottles | Municipal composting / safe landfill | **180°** |

---

## 🌟 Key Functional Modules

### 1. 📷 Computer Vision & Machine Learning Classifier
- Extracts a 13-dimensional visual descriptor:
  - Color distribution & dominant RGB/HSV ratios (identifies blood stains, clear polymers, metallic sheen, amber glass).
  - High-frequency edge density & Sobel gradients (identifies sharp needles and scalpels).
  - Aspect ratio & geometric profile (elongated tubes vs. compact gauze).
- Evaluated via a multi-class Random Forest & SVM ensemble with confidence calibration.
- **Includes 1-click test samples** (Soiled Gauze, Nitrile Glove, Hypodermic Needle, Glass Vial, Packaging Box).

### 2. 🛢️ IoT Smart Bins Telemetry & Capacity Controller
- **HC-SR04 Ultrasonic Sensor:** Measures real-time bin depth (cm) and fill percentage (0–100%).
- **HX711 Load Cell:** Tracks mass in kilograms (kg) and flags overloaded containers.
- **MQ-135 Gas Sensor:** Measures volatile organic compounds (VOCs) and decomposition ammonia (ppm).
- **Automated Chute Lockout:** Automatically locks the deposition chute when bin capacity exceeds 90% to prevent spillage.
- **Sanitation Action:** 1-click "Empty & Sanitize" functionality for hospital housekeeping teams.

### 3. 📋 Digital Waste Manifest & Audit Registry
- Generates compliant digital manifest tracking IDs (`BMW-2026-XXXX`).
- Logs timestamp, origin ward (ICU, OT-1, Emergency Trauma, Pathology Lab), item description, exact mass, and destination Common Bio-Medical Waste Treatment Facility (CBWTF).
- Generates barcode/QR tracking strings for waste bag transport.
- Computes aggregate statistics (total kg disposed per color code) for regulatory audits.

### 4. 🧪 IoT Hardware Lab & Simulator
- Interactive slider controls to simulate ultrasonic fill depth, weight load, and hazardous gas spikes.
- Complete microcontroller pinout blueprint for **ESP32 NodeMCU / Raspberry Pi / Arduino** with MG996R metal-gear servo motors.

### 5. 🏥 Staff Safety & Emergency Protocols
- **Needle-Stick Injury Protocol:** 5-step emergency procedure (immediate soap wash, no squeezing, antiseptic, hospital incident report, and Post-Exposure Prophylaxis within 2 hours).
- **Healthcare Worker Segregation Quiz:** Interactive 4-question training assessment with instant explanations.

---

## 🚀 How to Execute the Project

### Method 1: One-Click Launch (Easiest)
Double-click [`run_biomed.bat`](file:///c:/Users/drona/Desktop/AI%20Powered%20Carrer%20Gudience%20System/run_biomed.bat) in the project folder.

### Method 2: Command Line
Open **PowerShell** or **Command Prompt**:
```powershell
cd "C:\Users\drona\Desktop\AI Powered Carrer Gudience System"
& "C:\Users\drona\AppData\Local\Programs\Python\Python313\python.exe" biomed_app.py
```

### 🌐 Open Hospital Command Center in Browser:
```
http://127.0.0.1:5000
```

---

## 🧪 Run Automated Tests
```powershell
& "C:\Users\drona\AppData\Local\Programs\Python\Python313\python.exe" test_biomed_system.py
```
*(All 6 unit and integration tests pass in ~0.3s)*

