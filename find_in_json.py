import json
import sys


def search_value_in_json(value, json_file):
    try:
        with open(json_file, "r") as file:
            data = json.load(file)

            def search(data, value):
                found = []
                if isinstance(data, dict):
                    for k, v in data.items():
                        if v == value:
                            found.append((k, v))
                        elif isinstance(v, (dict, list)):
                            found.extend(search(v, value))
                elif isinstance(data, list):
                    for item in data:
                        found.extend(search(item, value))
                return found

            found_items = search(data, value)
            return found_items

    except FileNotFoundError:
        print(f"Error: The file '{json_file}' was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON file.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <value> <json_file>")
        sys.exit(1)

    value = sys.argv[1]
    json_file = sys.argv[2]

    found_items = search_value_in_json(value, json_file)
    if found_items:
        print(f"Found items containing value '{value}':")
        for key, val in found_items:
            print(f"{key}: {val}")
    else:
        print(f"No items found containing value '{value}' in the file.")
