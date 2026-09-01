import requests

response = requests.get("https://api.github.com/bh-gaur")
print(response.status_code)

print(response.json())

with open("github_api_response.json", "w") as file:
    file.write(response.text)

# data = {"name": "Alice","age": 25}

# response = requests.post("https://api.example.com", json=data)
# print(response.status_code)

