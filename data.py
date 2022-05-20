import requests

parameters = {
    "amount": 20,
    "difficulty": "easy",
    "category": 18,
    "type": "multiple",
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
