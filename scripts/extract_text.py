# extract_text.py
# What it uses: PyMuPDF (aka fitz) to read PDFs page by page.

# ✨ What it does: For each PDF, save page number & text.
import fitz  # PyMuPDF
import os
import json

PDF_DIR = r"C:\Users\Relig\Downloads\radiXplore_project\data\pdfs"
OUTPUT_DIR = r"C:\Users\Relig\Downloads\radiXplore_project\data\output\pdf_texts.json"

def extract_text():
    results = []
    for pdf_file in os.listdir(PDF_DIR):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(PDF_DIR, pdf_file)
            doc = fitz.open(pdf_path)
            for page_num in range(len(doc)):
                page = doc[page_num]
                text = page.get_text()
                results.append({
                    "pdf_file": pdf_file,
                    "page_number": page_num + 1,
                    "text": text
                })
    with open(OUTPUT_DIR, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Extracted text saved to {OUTPUT_DIR}")

if __name__ == "__main__":
    extract_text()
