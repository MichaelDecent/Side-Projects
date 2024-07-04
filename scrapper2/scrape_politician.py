import requests
from bs4 import BeautifulSoup
import json

url = "https://www.meineabgeordneten.at/Abgeordnete?partei="
response = requests.get(url)

politicians = []

soup = BeautifulSoup(response.content, "html.parser")

politician_list = soup.find_all("div", class_="col-9 col-md-8 col-lg-7")


for politician in politician_list:
    function = politician.find("div", class_="untertitel").text.strip()
    politician_details = politician.find("span", class_="name")
    prefix = (
        politician_details.find(
            "span", itemprop="http://schema.org/honorificPrefix"
        ).text.strip()
        if politician.find("span", itemprop="http://schema.org/honorificPrefix")
        else None
    )
    given_name = (
        politician_details.find(
            "span", itemprop="http://schema.org/givenName"
        ).text.strip()
        if politician.find("span", itemprop="http://schema.org/givenName")
        else None
    )
    family_name = (
        politician_details.find(
            "span", itemprop="http://schema.org/familyName"
        ).text.strip()
        if politician.find("span", itemprop="http://schema.org/familyName")
        else None
    )

    if not prefix or not given_name or not family_name:
        continue

    full_name = f"{prefix} {given_name} {family_name}"

    politicians.append({"full_name": full_name, "function": function})


with open("politicians.json", "w") as json_file:
    json.dump(politicians, json_file, indent=4, ensure_ascii=False)

print("Data has been written to politicians.json")
