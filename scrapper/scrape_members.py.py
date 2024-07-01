import requests
from bs4 import BeautifulSoup
import json

# Fetch the webpage
url = "https://parliament.ky/members/"
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, "html.parser")

# Initialize an empty list to store member data
members = []

# Find all member elements
member_list = soup.find_all("div", class_="member-select-main")

# Iterate through each member and extract the name and role
for member in member_list:
    member_name = member.find("h1").text.strip() if member.find("h1") else ""
    member_role = member.find("p").text.strip() if member.find("p") else ""
    members.append({
        "member_name": member_name,
        "member_role": member_role
    })

# Write the data to a JSON file
with open("members.json", "w") as json_file:
    json.dump(members, json_file, indent=4, ensure_ascii=False)

print("Data has been written to members.json")
