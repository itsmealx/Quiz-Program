class QuizBrain:

    def __init__(self, question_list: list):
        self.question_number = 0
        self.score = 0
        self.q_list = question_list


    def still_has_question(self):
        return self.question_number < len(self.q_list)


    def next_question(self):
        current_question = self.q_list[self.question_number]
        self.question_number += 1 #for question number
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False): ")
        self.check_answer(user_answer=user_answer, correct_answer=current_question.answer)


    def check_answer(self, user_answer: str, correct_answer: str):
        if user_answer.lower() == correct_answer.lower():
            print("You are correct!")
            self.score += 1
        else:
            print(f"Correct answer: {correct_answer}")
        print(f"Current score: {self.score}/{self.question_number}")
        print("\n")

