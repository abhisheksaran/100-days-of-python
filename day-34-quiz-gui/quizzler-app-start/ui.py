from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title = "Quiz Game"
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score:", background=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, background='white')
        self.question_text = self.canvas.create_text(150, 125, text="Question Here", font=(FONT_NAME, 20, "italic"),
                                                     fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.right_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(row=2, column=0)
        self.wrong_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(background="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(background="white")
            self.canvas.itemconfig(self.question_text, text="You have reached to the end of the quiz.")
            self.right_button.config(state='disable')
            self.wrong_button.config(state='disable')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, is_right):
        self.window.after(500, self.get_next_question)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
