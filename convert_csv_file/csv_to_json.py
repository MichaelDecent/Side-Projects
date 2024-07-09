import pandas as pd
import json
from deep_translator import GoogleTranslator

# Initialize the translator
translator = GoogleTranslator(source="pt", target="en")

csv_file_path = "202405_PEP.csv"
json_file_path = "202405_PEP.json"

try:
    df = pd.read_csv(
        csv_file_path, encoding="latin1", delimiter=";", on_bad_lines="skip"
    )
except pd.errors.ParserError as e:
    print(f"Error reading the CSV file: {e}")


def translate_text(text):
    try:
        translated = translator.translate(text)
        print(translated)
        return translated
    except Exception as e:
        print(f"Error translating text: {text}. Error: {e}")
        return text


df.columns = [translate_text(col) for col in df.columns]

first_row = df.iloc[0].apply(translate_text)

df.iloc[0] = first_row

json_data = df.to_json(orient="records")

with open(json_file_path, "w") as json_file:
    json.dump(json.loads(json_data), json_file, indent=4, ensure_ascii=False)

print(
    f"CSV file has been translated to English, converted to JSON, and saved to {json_file_path}"
)
