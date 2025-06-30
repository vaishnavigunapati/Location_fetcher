# What it uses: Calls all the above scripts in order.

# ✨ What it does: This is your “run all” file!
# pipeline.py
import subprocess

print("Running pipeline step-by-step...")

subprocess.call(["python", "scripts/extract_text.py"])
subprocess.call(["python", "scripts/train_ner.py"])
subprocess.call(["python", "scripts/infer_ner.py"])
subprocess.call(["python", "scripts/infer_geo.py"])

print("Pipeline complete!")
