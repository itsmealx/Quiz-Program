from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]

    new_question = Question(text=text, answer=answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've finish the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

