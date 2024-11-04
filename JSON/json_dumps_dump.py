"""
json module
json.dumps -> JSON-Formated-String
json.dump -> JSON-Formated-File """
import json


method = {
    "first": "Master one thing and become good at it",
    "second": "Then stack other things on top of that",
    "third": "this is how you learn many things and become good at it"
}

# Convert Python dictionary to JSON
json_data = json.dumps(method, indent=2) # -> JSON-Formated-String

print(f"This is the json data: {json_data}")


# writing python data to json data in external file
with open("method.json", 'w', encoding='utf-8') as file:
    json.dump(method, file, indent=2) # -> JSON-Formated-File
