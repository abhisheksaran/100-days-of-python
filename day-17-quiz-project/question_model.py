class Question:
    def __init__(self, question, answer):
        self.data = question
        self.answer = answer
    def is_correct(self, your_answer):
        if your_answer.lower() == self.answer.lower():
            return True
        else :
            return False

