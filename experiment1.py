import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("ID:", data["id"])
    print("Name:", data["name"])
    print("Email:", data["email"])
    print("City:", data["address"]["city"])
else:
    print("Failed to fetch data.")
