# 🚀 RadiXplore Candidate Coding Challenge  
## 🪨 Mining Project Intelligence System

Hello! This project is my solution for the **RadiXplore Candidate Coding Challenge**.  
It builds an **automated pipeline** that:

✅ Extracts mining project names from unstructured PDF reports  
✅ Infers approximate **geographic coordinates** for each project  
✅ Outputs everything as a neat **JSONL** file

---

## 📂 **Folder Structure**

radiXplore_project/
│
├── data/
│ ├── pdfs/ # All input PDF mining reports
│ ├── annotations/ # JSON annotation file for training
│ ├── output/ # Where extracted & final JSONL will go
│ └── geolocation_cache/ # (Optional) cache for API responses
│
├── scripts/
│ ├── extract_text.py # Extracts text from PDFs
│ ├── train_ner.py # Fine-tunes NER model
│ ├── infer_ner.py # Runs trained model to find project names
│ ├── infer_geo.py # Uses LLM (Groq API) to get coordinates
│ ├── pipeline.py # Runs all steps in order
│ └── utils.py # (Optional) helper functions
│
├── requirements.txt # Python dependencies
├── README.md # This file!
└── .gitignore


---

## 🛠️ **Tech Stack**

| Step                     | Tools / Libraries Used                        |
|--------------------------|-----------------------------------------------|
| PDF Text Extraction      | PyMuPDF (`fitz`)                               |
| Named Entity Recognition | spaCy (or Transformers)                       |
| Geolocation Inference    | Groq API (Mixtral or Llama models) + JSON     |
| General                  | Python, tqdm, json, subprocess                |

---

## ⚡ **Step-by-Step Workflow**

---

### ✅ 1️⃣ Install Python Environment

```bash
# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # Or on Windows: venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt
python scripts/extract_text.py
python scripts/train_ner.py
python scripts/infer_ner.py
# Windows PowerShell
setx GROQ_API_KEY "YOUR_GROQ_API_KEY"
python scripts/infer_geo.py
python scripts/pipeline.py
{
  "pdf_file": "report1.pdf",
  "page_number": 3,
  "project_name": "Minyari Dome Project",
  "context_sentence": "Minyari Dome Project is located in Western Australia...",
  "coordinates": [-23.12, 132.56]
}



🚀
