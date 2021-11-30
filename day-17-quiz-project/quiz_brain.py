from question_model import Question
class Quiz:
    def __init__(self, question_data):
        self.total_questions = len(question_data)
        self.questions=[]
        for question in question_data:
            self.questions.append(Question(question["text"], question["answer"]))
    def play(self):
        print("There are total {} question.".format(self.total_questions))
        for i in range(self.total_questions):
            question = self.questions[i]
            print("{}. {}".format(i+1, question.data))
            your_answer = input("(True or False):")
            if question.is_correct(your_answer):
                print("Congratulations, that's correct!\n")
            else:
                print("Sorry, that's not the right answer!\n")
