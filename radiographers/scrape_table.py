import requests
from bs4 import BeautifulSoup
import json

url = "https://portal.rrbn.gov.ng/licensed-radiographers/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

script_tag = soup.find(
    "script", type="text/javascript", string=lambda t: t and "window.tablesomeTables" in t
)

if script_tag:
    script_content = script_tag.string.strip()
    json_data_start = script_content.find("[")
    json_data_end = script_content.rfind("]") + 1
    json_str = script_content[json_data_start:json_data_end]

    tablesome_tables = json.loads(json_str)

    column_titles = [column["name"] for column in tablesome_tables[0]["items"]["columns"]]

    radiographer_list = []
    for row in tablesome_tables[0]["items"]["rows"]:
        radiographer_dict = {}
        for index, value in enumerate(row["content"].values()):
            radiographer_dict[column_titles[index]] = value["value"]
        radiographer_list.append(radiographer_dict)

    with open("output.json", "w", encoding="utf-8") as json_file:
        json.dump(radiographer_list, json_file, ensure_ascii=False, indent=4)

    print("Data successfully written to output.json")
else:
    print("Script tag containing tablesomeTables not found.")
