from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for q_data in question_data:
    question_bank.append(Question(q_data["question"],q_data["correct_answer"]))


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("Yay you have completed the quiz")
print(f'Your final score is {quiz.user_score}/{quiz.question_number}')


