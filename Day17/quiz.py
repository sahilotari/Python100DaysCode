# Questions
# Attributes: 1. Text, 2. Answer

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    qText = question["text"]
    qAns = question["answer"]
    cur = Question(qText, qAns)
    question_bank.append(cur)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")