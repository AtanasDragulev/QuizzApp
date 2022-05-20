from data import question_data
from engine import Engine, Question
from ui import Interface
import random

question_bank = []
for question in question_data:
    question_text = question["question"]
    correct_answer = question["correct_answer"]
    options = question["incorrect_answers"]
    options.append(correct_answer)
    random.shuffle(options)
    new_question = Question(question_text, options, correct_answer)
    question_bank.append(new_question)

quiz = Engine(question_bank)
quiz_ui = Interface(quiz)

