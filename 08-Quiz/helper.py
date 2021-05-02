#API from https://opentdb.com/api_config.php
#TODO: implement multiple user choice based questions
import requests
no_of_questions = input("Enter no of questions ")
difficulty = "easy"
key = f"https://opentdb.com/api.php?amount={no_of_questions}&category=18&difficulty={difficulty}&type=boolean"
response = requests.get(key)
json_response = response.json()

question_data = json_response["results"]

print(question_data)