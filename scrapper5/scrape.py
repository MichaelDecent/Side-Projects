import requests
from bs4 import BeautifulSoup
import json
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source="es", target="en")

base_url = "https://peps.directoriolegislativo.org/colombia/es/search?page="
page_number = 1
member_list = []

while True:
    url = base_url + str(page_number)
    response = requests.get(url)

    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.content, "html.parser")
    page = soup.find("main", class_="container-fluid")

    if not page:
        break

    titles = [
        title.text.strip(":") for title in page.find_all("h1", class_="display-4")
    ]

    section1 = page.find(
        "div", class_="flex flex-row flex-wrap items-end justify-start"
    )
    if section1:
        all_members = section1.find_all(
            "div", class_="bg-gray-50 py-6 px-6 rounded-3xl w-64 my-4 mx-2 shadow-xl"
        )
        if not all_members:
            break  # No members found on this page, exit loop

        for member in all_members:
            first_name = member.find("p", class_="text-lg font-semibold").text.strip()
            last_name = member.find(
                "p", class_="text-xl font-semibold mb-2"
            ).text.strip()
            name = f"{first_name} {last_name}"
            div_role = member.find("div", class_="flex space-x text-gray-400 text-sm")
            if div_role:
                role = translator.translate(div_role.find("p").text.strip())
            div_info = member.find("div", class_="my-2 w-full")
            if div_info:
                other_info = div_info.find(
                    "p", class_="font-semibold text-base mb-2"
                ).text.strip()

            member_list.append({"name": name, "role": role, "other_info": other_info})

    sections = page.find_all("div", class_="row")

    for section in sections:
        all_members = section.find_all(
            "div", class_="bg-gray-50 py-6 px-6 rounded-3xl w-64 my-4 mx-2 shadow-xl"
        )
        for member in all_members:
            name = member.find("p", class_="text-xl font-semibold mb-3").text.strip()
            other_name = (
                member.find("p", class_="text-xl font-semibold mb-2").text.strip()
                if member.find("p", class_="text-xl font-semibold mb-2")
                else None
            )
            if other_name:
                name = f"{name} {other_name}"
            role = "None"
            div_info = member.find("div", class_="my-2 w-full")
            if div_info:
                other_info = translator.translate(
                    div_info.find(
                        "p", class_="font-semibold text-base mb-2"
                    ).text.strip()
                )

            member_list.append({"name": name, "role": role, "other_info": other_info})
    print(page_number, "Done!")
    page_number += 1

with open("members_data.json", "w") as jsonfile:
    json.dump(member_list, jsonfile, indent=4, ensure_ascii=False)

print("members scraped and saved to 'members_data.json'")
