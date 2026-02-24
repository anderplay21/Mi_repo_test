import requests

url = "https://api.bird.com/workspaces/261b591d-f0af-42be-b0b7-92960184744c/contacts"

headers = {
    "Content-Type": "application/json",
    "Authorization": "AccessKey QdeHO8Dc7rt8FMsI9d4lodmeUBMv33Zbezw1"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())



