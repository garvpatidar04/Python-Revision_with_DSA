"""
json module"""
import json

with open('method.json', 'r', encoding='utf-8') as file:
    json_read = file.read()


print(f"This is orignal: {json_read}")

# Convert JSON data to Python dictionary
json_python = json.loads(json_read)

mini_json = json.dumps(json_python, indent=None, separators=(',', ':') )
with open('mini_method.json', 'w', encoding='utf-8') as file:
    file.write(mini_json)

print(f"This is mini json: {mini_json}")
