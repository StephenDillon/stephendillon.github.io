
import json
import datetime
import uuid
import os

def parse_date(date_str):
    # Format: Sun, Dec 28 2025
    clean = date_str.replace("**", "").strip()
    return datetime.datetime.strptime(clean, "%a, %b %d %Y").date()

def create_event(date_obj, summary, description):
    dt_start = date_obj.strftime("%Y%m%d")
    dt_end = (date_obj + datetime.timedelta(days=1)).strftime("%Y%m%d")
    uid = str(uuid.uuid4())
    now = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
    
    return "\n".join([
        "BEGIN:VEVENT",
        f"UID:{uid}",
        f"DTSTAMP:{now}",
        f"DTSTART;VALUE=DATE:{dt_start}",
        f"DTEND;VALUE=DATE:{dt_end}",
        f"SUMMARY:{summary}",
        f"DESCRIPTION:{description}",
        "END:VEVENT"
    ])

def main():
    json_path = os.path.join("_data", "training_plan.json")
    
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    with open(json_path, "r") as f:
        rows = json.load(f)

    ics_content = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Stephen Dillon//Rome Marathon Plan//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:Rome Marathon Training",
        "X-WR-TIMEZONE:Europe/Rome",
    ]

    for row in rows:
        if row.get("is_total"):
            continue
            
        date_str = row.get("date")
        if not date_str: continue
        
        try:
            date_obj = parse_date(date_str)
        except ValueError:
            continue
            
        workout_en = row.get("workout_en", "Run")
        
        # Skip Rest days from calendar?
        # Checks if "Rest" is in the English workout name or "Riposo" in Italian
        if "Rest" in workout_en or "Riposo" in row.get("workout_it", ""):
            continue
            
        dist = row.get("dist_km")
        pace = row.get("pace_km") # Use the string like "6:00-6:10 min/km"
        
        desc_parts = []
        if dist and dist != "-":
            desc_parts.append(f"Distance: {dist} km")
        if pace:
            desc_parts.append(f"Target Pace: {pace}")
            
        description = "\\n".join(desc_parts)
        
        ics_content.append(create_event(date_obj, f"Run: {workout_en}", description))

    ics_content.append("END:VCALENDAR")
    
    with open("training.ics", "w", encoding="utf-8") as f:
        f.write("\n".join(ics_content))
    
    print("Updated training.ics")

if __name__ == "__main__":
    main()
