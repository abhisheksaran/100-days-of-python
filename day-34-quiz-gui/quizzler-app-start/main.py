import time

from question_model import Question
import data
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface
import time

# Filling data file with random new 10 questions
response = requests.get(url="https://opentdb.com/api.php?amount=8&type=boolean")
response.raise_for_status()
question_data = response.json()['results']
# print(question_data)
with open("data.py","w") as f:
    f.write(f"question_data={question_data}")

# Get the questions from data file
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

#while quiz.still_has_questions():
#    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
