import csv
import json
from deep_translator import GoogleTranslator


csv_file_path = "peps.csv"
json_file_path = "peps.json"


def translate_text(text):
    translator = GoogleTranslator(source="es", target="en")
    return translator.translate(text)


with open(csv_file_path, mode="r", newline="", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    translated_fieldnames = [translate_text(field) for field in csv_reader.fieldnames]

    data = [
        {
            translated_fieldnames[i]: row[field]
            for i, field in enumerate(csv_reader.fieldnames)
        }
        for row in csv_reader
    ]
with open(json_file_path, mode="w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print(f"CSV data has been successfully converted to JSON and saved to {json_file_path}")
