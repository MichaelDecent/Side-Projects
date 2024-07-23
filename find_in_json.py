import json
import sys


def get_values_from_json(key, json_file):
    try:
        with open(json_file, "r") as file:
            data = json.load(file)

            if isinstance(data, list):
                values = [
                    item.get(key, None) for item in data if isinstance(item, dict)
                ]
            elif isinstance(data, dict):
                values = [data.get(key, None)]
            else:
                values = []

            return [value for value in values if value is not None]
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
        print("Usage: python script.py <key> <json_file>")
        sys.exit(1)

    key = sys.argv[1]
    json_file = sys.argv[2]

    values = get_values_from_json(key, json_file)
    if values:
        print(f"Values for key '{key}': {values}")
    else:
        print(f"No values found for key '{key}' or key does not exist in the file.")
