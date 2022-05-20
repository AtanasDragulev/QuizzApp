import html


class Engine:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.options = []
        self.answer = ""

    def still_has_questions(self):
        """Checks if any questions left"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Loads next questions"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        self.options = self.current_question.options
        options = [html.unescape(q) for q in self.options]
        self.answer = self.current_question.answer
        return q_text, options, self.answer

    def check_answer(self, button):
        """Checks answer and if true increases score"""
        is_right = self.options[button] == self.answer
        if is_right:
            self.score += 1
            return True
        else:
            return False


class Question:

    def __init__(self, q_text, options, q_answer):
        self.text = q_text
        self.options = options
        self.answer = q_answer
