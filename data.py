import requests
from settings import *
parameters = {
    "amount": QUESTIONS,
    "difficulty": DIFFICULTIES[DIFFICULTY],
    "category": CATEGORY,
    "type": "multiple",
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
