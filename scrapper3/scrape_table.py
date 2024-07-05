import requests
from bs4 import BeautifulSoup
import json
from deep_translator import GoogleTranslator

url = 'https://www.hcdn.gob.ar/diputados/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table')

headers = [th.text.strip() for th in table.find_all('th')]

translator = GoogleTranslator(source='spanish', target='english')
translated_headers = [translator.translate(header) for header in headers]

rows = []
for tr in table.find_all('tr')[1:]:
    cells = tr.find_all('td')
    if len(cells) > 0:
        row = {translated_headers[i]: cell.text.strip() for i, cell in enumerate(cells)}
        rows.append(row)

if rows:
    last_row = rows[-1]
    translated_last_row = {key: translator.translate(value) for key, value in last_row.items()}
    rows[-1] = translated_last_row

with open('table_data.json', 'w') as jsonfile:
    json.dump(rows, jsonfile, indent=4, ensure_ascii=False)

print("Table scraped and saved to 'table_data.json'")
