import json

# Read the JSON file
with open("config.json", "r") as json_file:
    data = json.load(json_file)

# Iterate through each dictionary in the JSON data
for entry in data:
    question = entry["Q"]
    answer = entry["A"]

    print("Question:", question)
    print("\n")
    print("Answer:", answer)
    print()