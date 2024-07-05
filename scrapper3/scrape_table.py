import requests
from bs4 import BeautifulSoup
import json
from deep_translator import GoogleTranslator

url = "https://www.hcdn.gob.ar/diputados/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table")

headers = [th.text.strip() for th in table.find_all("th")[1:]]

translator = GoogleTranslator(source="spanish", target="english")
translated_headers = [translator.translate(header) for header in headers]

rows = []
for tr in table.find_all("tr")[1:]:
    cells = tr.find_all("td")[1:]
    if len(cells) > 0:
        row = {translated_headers[i]: cell.text.strip() for i, cell in enumerate(cells)}
        rows.append(row)

if rows:
    for row in rows:
        last_column_key = translated_headers[-1]
        row[last_column_key] = translator.translate(row[last_column_key])


with open("table_data.json", "w") as jsonfile:
    json.dump(rows, jsonfile, indent=4, ensure_ascii=False)

print("Table scraped and saved to 'table_data.json'")
