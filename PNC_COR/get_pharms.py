import requests
import json

url = "https://pcncore.azurewebsites.net/PublicSearch/PharmacistLicence"

response = requests.get(url)

pharm_data = []

if response.status_code == 200:
    data = response.json()

    for item in data["Data"]:
        if not item["PharmacistRegNumber"]:
            continue
        pharm_data.append(item)

    output_file = "pharmacist_licence.json"

    with open(output_file, "w") as file:
        json.dump(pharm_data, file, indent=4)

    print(f"Data has been written to {output_file}")
else:
    print(f"Failed to fetch data. HTTP Status code: {response.status_code}")
