from waste_data import WASTE_DATABASE

def analyze_waste(item):
    item = item.strip().lower()

    # 1️⃣ Exact & partial match from database
    for key in WASTE_DATABASE:
        if key.lower() in item or item in key.lower():
            data = WASTE_DATABASE[key]
            return {
                "type": data["type"],
                "degradable": data["degradable"],
                "recyclable": data["recyclable"],
                "disposal": data["disposal"],
                "impact": data["impact"]
            }

    # 2️⃣ Intelligent fallback rules (AI-style)
    if any(word in item for word in ["plastic", "polythene", "cover", "bottle"]):
        return {
            "type": "Plastic Waste",
            "degradable": "No",
            "recyclable": "Yes",
            "disposal": "Dry waste bin or plastic recycling center",
            "impact": "Reduces plastic pollution and landfill accumulation"
        }

    if any(word in item for word in ["food", "banana", "vegetable", "fruit", "leftover"]):
        return {
            "type": "Organic Waste",
            "degradable": "Yes",
            "recyclable": "No (Compostable)",
            "disposal": "Compost pit or wet waste bin",
            "impact": "Converts waste into natural manure and reduces methane"
        }

    if any(word in item for word in ["battery", "cell", "charger", "electronics"]):
        return {
            "type": "Hazardous / E-Waste",
            "degradable": "No",
            "recyclable": "Yes (Special handling)",
            "disposal": "Authorized e-waste collection center",
            "impact": "Prevents toxic chemicals from contaminating soil and water"
        }

    if any(word in item for word in ["paper", "cardboard", "newspaper"]):
        return {
            "type": "Paper Waste",
            "degradable": "Yes",
            "recyclable": "Yes",
            "disposal": "Dry waste bin or paper recycling unit",
            "impact": "Saves trees and reduces deforestation"
        }

    # 3️⃣ Final fallback (never blank / useless)
    return {
        "type": "General Waste",
        "degradable": "Depends on material",
        "recyclable": "Partially recyclable",
        "disposal": "Follow local municipal waste guidelines",
        "impact": "Improper disposal may negatively affect the environment"
    }
