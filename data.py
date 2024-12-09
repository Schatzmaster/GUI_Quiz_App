import requests

AMOUNT = 10
TYPE = "boolean"

params = {
    "amount": AMOUNT,
    "type": TYPE
}

response = requests.get(url="https://opentdb.com/api.php", params=params)
response.raise_for_status()
question_data = response.json()["results"]