import requests

url = "https://opentdb.com/api_category.php"
response = requests.get(url)
categories = response.json()["trivia_categories"]

for cat in categories:
    print(f"{cat['id']}: {cat['name']}")
