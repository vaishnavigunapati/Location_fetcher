# What it uses: Your trained model from train_ner.py.

# ✨ What it does: Reads text from each PDF and predicts mining project names.

# ✅ Outputs partial JSONL: coordinates = null for now.

# infer_ner.py
# infer_ner.py
import spacy
import json
import os

# ✅ 1. Load your trained model path
MODEL_DIR = r"C:\Users\Relig\Downloads\radiXplore_project\models\ner"

# ✅ 2. Your extracted PDF text file (from extract_text.py)
TEXT_FILE = r"C:\Users\Relig\Downloads\radiXplore_project\data\output\pdf_texts.json"

# ✅ 3. Where you want the output JSONL to go
OUTPUT_FILE = r"C:\Users\Relig\Downloads\radiXplore_project\data\output\extracted_projects.jsonl"

def run_inference():
    nlp = spacy.load(MODEL_DIR)

    # Add sentencizer for sentence boundaries!
    if "sentencizer" not in nlp.pipe_names:
        nlp.add_pipe("sentencizer")

    with open(TEXT_FILE) as f:
        pages = json.load(f)

    with open(OUTPUT_FILE, "w") as out_f:
        for page in pages:
            doc = nlp(page["text"])
            for ent in doc.ents:
                if ent.label_ == "PROJECT":
                    record = {
                        "pdf_file": page["pdf_file"],
                        "page_number": page["page_number"],
                        "project_name": ent.text,
                        "context_sentence": ent.sent.text,   # ✅ will now work!
                        "coordinates": None
                    }
                    out_f.write(json.dumps(record) + "\n")
    print(f"✅ Inference output saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    run_inference()
