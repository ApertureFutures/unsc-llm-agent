import json

def load_sample_resolution():
    with open("sample_data/sample_resolution.json", "r", encoding="utf-8") as f:
        return json.load(f)
