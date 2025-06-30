# What it uses: spaCy or HuggingFace Transformers.

# ✨ What it does: Uses your sample annotations to fine-tune a model to find "PROJECT" entities.
# train_ner.py
import spacy
from spacy.tokens import DocBin
from spacy.training import Example
import json
import random

ANNOT_FILE = r"C:\Users\Relig\Downloads\radiXplore_project\data\annotations\sample-annotations.json"
MODEL_DIR = r"C:\Users\Relig\Downloads\radiXplore_project\models\ner"

def load_data():
    with open(ANNOT_FILE) as f:
        annotations = json.load(f)
    training_data = []
    for item in annotations:
        text = item['data']['text']
        entities = []
        for ann in item['annotations'][0]['result']:
            if ann['value']['labels'][0] == 'PROJECT':
                start = ann['value']['start']
                end = ann['value']['end']
                entities.append((start, end, 'PROJECT'))
        training_data.append((text, {"entities": entities}))
    return training_data

def train():
    nlp = spacy.blank("en")
    ner = nlp.add_pipe("ner")
    ner.add_label("PROJECT")

    training_data = load_data()
    optimizer = nlp.initialize()

    for i in range(10):
        random.shuffle(training_data)
        losses = {}
        batches = spacy.util.minibatch(training_data, size=2)
        for batch in batches:
            texts, annotations = zip(*batch)
            examples = []
            for text, ann in zip(texts, annotations):
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, ann)
                examples.append(example)
            nlp.update(examples, drop=0.5, losses=losses)
        print(f"Losses at iteration {i}: {losses}")

    nlp.to_disk(MODEL_DIR)
    print(f"Model saved to {MODEL_DIR}")

if __name__ == "__main__":
    train()