"""
IoT Smart Bin Telemetry Simulator for Bio-Medical Waste Monitoring.
Simulates Ultrasonic Fill-Level Sensors (HC-SR04), Load Cell Weight Transducers (HX711),
MQ-135 Gas/Odor Quality Sensors, and Servo Actuator Chute Flap Control.
"""

from typing import Dict, Any, List
import datetime
from core.biomed_dataset import BIN_SPECIFICATIONS

class SmartBinMonitor:
    def __init__(self):
        # Initial state for the 5 hospital smart bins
        self.bins: Dict[str, Dict[str, Any]] = {
            "yellow": {
                "id": "bin-yellow-01",
                "name": "Yellow Bin (Infectious)",
                "category": "yellow",
                "fill_percentage": 58.0,
                "max_depth_cm": 60.0,
                "current_depth_cm": 25.2,
                "weight_kg": 14.2,
                "max_weight_kg": 25.0,
                "gas_ppm": 165.0,  # Ammonia / VOC ppm
                "temperature_c": 24.5,
                "lid_status": "LOCKED_IDLE",
                "lockout_full": False,
                "last_emptied": "2026-11-01 08:00 AM",
                "items_count": 34
            },
            "red": {
                "id": "bin-red-01",
                "name": "Red Bin (Recyclable Plastics)",
                "category": "red",
                "fill_percentage": 72.0,
                "max_depth_cm": 60.0,
                "current_depth_cm": 16.8,
                "weight_kg": 11.8,
                "max_weight_kg": 20.0,
                "gas_ppm": 110.0,
                "temperature_c": 23.8,
                "lid_status": "LOCKED_IDLE",
                "lockout_full": False,
                "last_emptied": "2026-11-01 07:30 AM",
                "items_count": 48
            },
            "white": {
                "id": "bin-white-01",
                "name": "White Bin (Sharps Safe)",
                "category": "white",
                "fill_percentage": 34.0,
                "max_depth_cm": 35.0,
                "current_depth_cm": 23.1,
                "weight_kg": 3.6,
                "max_weight_kg": 10.0,
                "gas_ppm": 85.0,
                "temperature_c": 23.0,
                "lid_status": "LOCKED_IDLE",
                "lockout_full": False,
                "last_emptied": "2026-10-31 06:00 PM",
                "items_count": 52
            },
            "blue": {
                "id": "bin-blue-01",
                "name": "Blue Bin (Glassware & Metal)",
                "category": "blue",
                "fill_percentage": 42.0,
                "max_depth_cm": 45.0,
                "current_depth_cm": 26.1,
                "weight_kg": 8.4,
                "max_weight_kg": 18.0,
                "gas_ppm": 90.0,
                "temperature_c": 23.2,
                "lid_status": "LOCKED_IDLE",
                "lockout_full": False,
                "last_emptied": "2026-11-01 09:15 AM",
                "items_count": 27
            },
            "general": {
                "id": "bin-general-01",
                "name": "General Bin (Municipal)",
                "category": "general",
                "fill_percentage": 25.0,
                "max_depth_cm": 60.0,
                "current_depth_cm": 45.0,
                "weight_kg": 5.1,
                "max_weight_kg": 30.0,
                "gas_ppm": 120.0,
                "temperature_c": 24.0,
                "lid_status": "LOCKED_IDLE",
                "lockout_full": False,
                "last_emptied": "2026-11-01 07:00 AM",
                "items_count": 18
            }
        }

    def get_all_bins(self) -> Dict[str, Any]:
        """Returns telemetry for all bins along with alerts and status labels."""
        summary = {}
        total_alerts = []

        for cat, b in self.bins.items():
            fill = b["fill_percentage"]
            gas = b["gas_ppm"]

            # Compute alerts
            alerts = []
            if fill >= 90.0:
                alerts.append("CRITICAL: Bin at or exceeding 90% capacity! Chute locked. Evacuation required.")
                b["lockout_full"] = True
                status_color = "red"
                status_label = "CRITICAL / OVERFLOW"
            elif fill >= 75.0:
                alerts.append("WARNING: Bin capacity exceeded 75%. Schedule collection pickup.")
                b["lockout_full"] = False
                status_color = "amber"
                status_label = "HIGH FILL LEVEL"
            else:
                b["lockout_full"] = False
                status_color = "emerald"
                status_label = "OPERATIONAL / NORMAL"

            if gas >= 300.0:
                alerts.append("HAZARD: Elevated volatile organic gas / odor detected! Inspect seal.")

            total_alerts.extend(alerts)

            summary[cat] = {
                **b,
                "status_color": status_color,
                "status_label": status_label,
                "alerts": alerts,
                "bin_specs": BIN_SPECIFICATIONS[cat]
            }

        return {
            "bins": summary,
            "total_alerts": total_alerts,
            "alerts_count": len(total_alerts),
            "system_online": True,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def record_disposal(self, category: str, item_weight_kg: float = 0.25) -> Dict[str, Any]:
        """Simulates item entering the smart bin chute."""
        cat = category.lower()
        if cat not in self.bins:
            cat = "yellow"

        target_bin = self.bins[cat]
        if target_bin["lockout_full"]:
            return {
                "success": False,
                "error": f"Cannot dispose item: {target_bin['name']} is FULL (>90%). Chute locked!"
            }

        # Increment weight and fill
        target_bin["weight_kg"] = round(target_bin["weight_kg"] + item_weight_kg, 2)
        added_fill = round((item_weight_kg / target_bin["max_weight_kg"]) * 50.0, 1)
        target_bin["fill_percentage"] = min(100.0, round(target_bin["fill_percentage"] + max(2.0, added_fill), 1))
        target_bin["items_count"] += 1
        target_bin["lid_status"] = "OPEN_DISCHARGING"

        return {
            "success": True,
            "bin": target_bin["name"],
            "new_fill": target_bin["fill_percentage"],
            "new_weight": target_bin["weight_kg"],
            "items_count": target_bin["items_count"]
        }

    def update_bin_telemetry(self, category: str, fill: float = None, weight: float = None, gas: float = None) -> Dict[str, Any]:
        """Allows dashboard sliders to update sensor telemetry for interactive demo."""
        cat = category.lower()
        if cat not in self.bins:
            return {"error": "Invalid bin category"}

        b = self.bins[cat]
        if fill is not None:
            b["fill_percentage"] = min(100.0, max(0.0, float(fill)))
        if weight is not None:
            b["weight_kg"] = min(b["max_weight_kg"], max(0.0, float(weight)))
        if gas is not None:
            b["gas_ppm"] = max(20.0, float(gas))

        return {"success": True, "bin": b}

    def empty_bin(self, category: str) -> Dict[str, Any]:
        """Simulates hospital sanitation worker emptying the bin."""
        cat = category.lower()
        if cat not in self.bins:
            return {"error": "Invalid bin category"}

        b = self.bins[cat]
        b["fill_percentage"] = 0.0
        b["weight_kg"] = 0.0
        b["items_count"] = 0
        b["gas_ppm"] = 65.0
        b["lockout_full"] = False
        b["lid_status"] = "LOCKED_IDLE"
        b["last_emptied"] = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")

        return {"success": True, "message": f"{b['name']} has been successfully emptied & sanitized."}

