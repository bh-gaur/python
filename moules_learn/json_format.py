import json

# Python Dictionary
person = {"name": "Alice", "age1": 25}

# Method 1: Using json.dumps() and file.write()
json_data = json.dumps(person, indent=4)
with open("./person.json", "w") as file:
    file.write(json_data)

print("Created person.json using json.dumps():")
print(json_data)

# Method 2: Direct file write using json.dump() (Recommended shorthand)
# with open("person.json", "w") as file:
#     json.dump(person, file, indent=4)

# ------------------------------------------------------------------------------
# Reading from the created JSON file
# ------------------------------------------------------------------------------
with open("./person.json", "r") as file:
    loaded_data = json.load(file)

print("\nRead back from person.json:")
print("Data type:", type(loaded_data))
print("Content  :", loaded_data)
# print(json_data) # Output: {"name": "Alice","age": 25}