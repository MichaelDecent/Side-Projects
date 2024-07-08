import requests
from bs4 import BeautifulSoup
import json

url = "https://www.judicial.ky/judicial-administration/judges"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

page = soup.find("section", id="content")

judges_list = []

sections = page.find_all("div", class_="fusion-column-wrapper fusion-flex-column-wrapper-legacy")
for section in sections:
    status = section.find("h3").text.strip() if section.find("h3") else None
    if status:
        current = section.find("div", class_="accordian fusion-accordian")
        current_judges = current.find_all("div", class_="panel-heading")

        for judge in current_judges:
            name = judge.find("span", class_="fusion-toggle-heading").text.strip()
            judges_list.append({"name": name, "status": status})

with open("judges_data.json", "w") as jsonfile:
    json.dump(judges_list, jsonfile, indent=4, ensure_ascii=False)

print("judges scraped and saved to 'judges_data.json'")
