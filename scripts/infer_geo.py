# infer_geo.py
import json
from groq import Groq  # Make sure groq package is installed

# ✅ Full absolute paths for Windows - adjust as needed
INPUT_FILE = r"C:\Users\Relig\Downloads\radiXplore_project\data\output\extracted_projects.jsonl"
OUTPUT_FILE = r"C:\Users\Relig\Downloads\radiXplore_project\data\output\extracted_projects_with_geo.jsonl"

# ✅ Your Groq API key (should ideally come from environment variables!)
GROQ_API_KEY = "API"
client = Groq(api_key=GROQ_API_KEY)

def get_coordinates(project_name, context):
    prompt = (
        f"Given this mining project: '{project_name}' in this context: '{context}', "
        f"provide approximate latitude and longitude coordinates in JSON like this: "
        f"{{\"latitude\": -23.12, \"longitude\": 132.56}}. "
        f"If you don't know, respond with: {{\"latitude\": null, \"longitude\": null}}. "
        f"Do not include any extra text, just the JSON object. DO NOT use a list."
    )

    response = client.chat.completions.create(
        model="llama3-8b-8192",  # ✅ Or whichever model you want
        messages=[
            {
                "role": "system",
                "content": "You are a precise geolocation expert. Only reply with a single valid JSON object. No explanations, no text."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content.strip()

    try:
        coords = json.loads(content)

        # ✅ Some models might still return a list: flatten it
        if isinstance(coords, list) and len(coords) > 0:
            coords = coords[0]

        if not isinstance(coords, dict):
            raise ValueError("Output is not a valid dict.")

    except Exception as e:
        print(f"⚠️ Could not parse JSON! Raw output:\n{content}")
        print(f"Error: {e}")
        coords = {"latitude": None, "longitude": None}

    return coords

def run_geo_inference():
    # ✅ Make sure output dir exists if needed
    import os
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(INPUT_FILE, "r") as f:
        lines = f.readlines()

    with open(OUTPUT_FILE, "w") as out_f:
        for idx, line in enumerate(lines):
            record = json.loads(line)

            print(f"🔍 Processing record {idx+1}/{len(lines)}: {record['project_name']}")

            coords = get_coordinates(record['project_name'], record['context_sentence'])
            record['coordinates'] = [coords.get("latitude"), coords.get("longitude")]
            out_f.write(json.dumps(record) + "\n")

    print(f"✅ Geo inference saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    run_geo_inference()
