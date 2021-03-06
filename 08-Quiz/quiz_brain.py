class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.user_score = 0
    
    def current_score(self):
        print(f'The current score is {self.user_score}/{self.question_number}')

    def still_has_questions(self):
        return  self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer = input(f'Q.{self.question_number}: {question.q_text} (True/False): ').lower()
        self.check_answer(user_answer,question)

    def check_answer(self,user_answer,question):
        if user_answer == question.q_answer.lower() or user_answer == question.q_answer.lower()[0]:
            print(f'You got it right.')
            self.user_score+=1
        else:
            print("You got it wrong")
        print(f'The correct answer is: {question.q_answer}')
        self.current_score()
        print('\n')
        
