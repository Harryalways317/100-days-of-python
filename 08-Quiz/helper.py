#API from https://opentdb.com/api_config.php
#TODO: implement multiple user choice based questions
import requests
key = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean"
response = requests.get(key)
json_response = response.json()

question_data = json_response["results"]
