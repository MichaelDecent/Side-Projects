import requests
from bs4 import BeautifulSoup
import json

url = "https://parliament.ky/members/former-members/"
url2 = "https://parliament.ky/members/"
response = requests.get(url)

tenure_list = [
    "term2017-2021",
    "term2013-2017",
    "term2009-2013",
    "term2005-2009",
]

soup = BeautifulSoup(response.content, "html.parser")

members = []

for tenure in tenure_list:
    section = soup.find("section", id=tenure)

    if not section:
        continue

    tenure_time = (
        section.find(
            "h2", class_="elementor-heading-title elementor-size-default"
        ).text.strip()
        if section.find("h2", class_="elementor-heading-title elementor-size-default")
        else ""
    )

    member_list = section.find_all("div", class_="elementor-widget-container")

    for member in member_list:
        member_name = member.find("p").text.strip() if member.find("p") else None
        if member_name:
            member_role = (
                member.find("li").text.strip() if member.find("li") else None
            )
            if not member_role:
                continue
            members.append(
                {
                    "tenure": tenure_time,
                    "member_name": member_name,
                    "member_role": member_role,
                }
            )
            continue
        member_name = (
            member.find(string=True, recursive=False).strip() if member.text else None
        )
        member_role = member.find("li").text.strip() if member.find("li") else None
        if not member_name or not member_role or member_role == "Speaker":
            continue
        members.append(
            {
                "tenure": tenure_time,
                "member_name": member_name,
                "member_role": member_role,
            }
        )

member_list = soup.find_all(
    "section",
    class_="elementor-section elementor-top-section elementor-element elementor-element-5633cb9 former_members elementor-section-full_width elementor-section-height-default elementor-section-height-default",
)

# Iterate through each member and extract the name and role
for member in member_list:
    tenure = member.find("h2").text.strip() if member.find("h2") else ""
    member_name = (
        member.find("div", class_="elementor-widget-container").text.strip()
        if member.find("div", class_="elementor-widget-container")
        else ""
    )
    member_role = member.find("li").text.strip() if member.find("li") else ""
    members.append(
        {
            "tenure": tenure,
            "member_name": member_name,
            "member_role": member_role,
        }
    )

"""
Retrieve current members
"""
response = requests.get(url2)

soup = BeautifulSoup(response.content, "html.parser")

member_list = soup.find_all("div", class_="member-select-main")
div = soup.find(
    "div",
    class_="elementor-element elementor-element-19374c5 elementor-widget__width-initial elementor-widget-mobile__width-inherit elementor-widget elementor-widget-image-box",
)
tenure = div.find("h3", class_="elementor-image-box-title").text.strip()

for member in member_list:
    member_name = member.find("h1").text.strip() if member.find("h1") else ""
    member_role = member.find("p").text.strip() if member.find("p") else ""
    members.append(
        {"tenure": tenure, "member_name": member_name, "member_role": member_role}
    )


with open("members.json", "w") as json_file:
    json.dump(members, json_file, indent=4, ensure_ascii=False)

print("Data has been written to members.json")
