import requests
from bs4 import BeautifulSoup
import json
from deep_translator import GoogleTranslator

base_url = "https://www.sukobinteresa.hr/hr/registar-duznosnika?page="
translator = GoogleTranslator(source="hr", target="en")
all_rows = []

page_number = 0
first_page = True

while True:
    url = f"{base_url}{page_number}"
    response = requests.get(url)

    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")

    if not table:
        break

    headers = [th.text.strip() for th in table.find_all("th")]
    translated_headers = [translator.translate(header) for header in headers]

    if first_page:
        translated_first_row = {
            translated_headers[i]: translator.translate(header)
            for i, header in enumerate(headers)
        }
        all_rows.append(translated_first_row)
        first_page = False

    for tr in table.find_all("tr")[1:]:
        cells = tr.find_all("td")
        if len(cells) > 0:
            row = {}
            for i, cell in enumerate(cells):
                text = cell.text.strip()
                if i in [1, 2, len(cells) - 1]:
                    text = translator.translate(text)
                row[translated_headers[i]] = text
            all_rows.append(row)

    print(f"Page {page_number} is Done!")
    page_number += 1
    print(all_rows)

with open("table_data.json", "w") as jsonfile:
    json.dump(all_rows, jsonfile, indent=4, ensure_ascii=False)

print("All pages scraped, translated, and saved to 'table_data.json'")
