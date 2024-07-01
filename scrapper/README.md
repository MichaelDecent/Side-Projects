# Web Scraping Members of Parliament

This project involves web scraping a list of members of parliament from a given URL and saving the extracted data into a JSON file.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python3
- `pip` 

## Step-by-Step Guide

1. **Install Required Libraries**

    First, you need to install the necessary Python libraries. Open your terminal or command prompt and run:

    ```bash
    pip install requests beautifulsoup4
    ```

2. **Fetch the Webpage and Extract Data**

    Create a new Python file (e.g., `scrape_members.py`) and paste the following code into it:

    ```python
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
    ```

3. **Run the Script**

    Navigate to the directory where your `scrape_members.py` file is located and run the script:

    ```bash
    python scrape_members.py
    ```

    This will fetch the data from the specified URL, parse it, and save the member information into a `members.json` file.

4. **Check the Output**

    After running the script, you should see a `members.json` file in the same directory. Open this file to view the extracted member data formatted in JSON.

    Example content of `members.json`:

    ```json
    [
        {
            "member_name": "John Doe",
            "member_role": "Prime Minister"
        },
        {
            "member_name": "Jane Smith",
            "member_role": "Minister of Health"
        }
        // Additional members...
    ]
    ```

## Additional Notes

- Ensure you have an active internet connection when running the script as it fetches data from an online source.
