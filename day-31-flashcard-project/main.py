import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
new_word_pair = {}
# ---------------------------- Create the new flash card ------------------------------- #
try:
    words_df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_df = pandas.read_csv("data/french_words.csv")
    word_pair_list = original_df.to_dict(orient='records')
else:
    word_pair_list = words_df.to_dict(orient='records')


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=new_word_pair['English'], fill='white')


def next_card():
    global new_word_pair, flip_id
    window.after_cancel(flip_id)
    new_word_pair = random.choice(word_pair_list)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=new_word_pair['French'], fill='black')
    flip_id = window.after(3000, func=flip_card)


def is_known():
    word_pair_list.remove(new_word_pair)
    data = pandas.DataFrame(word_pair_list)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


# ---------------------------- Set up the UI ------------------------------- #
window = Tk()
window.title("Flashcard Project")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_id = window.after(3000, func=flip_card)

# Create the canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263)
card_title = canvas.create_text(400, 150, text="French", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="the word", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Create the buttons
cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, command=next_card, highlightthickness=0, padx=50, pady=50)
cross_button.grid(column=1, row=1)

tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_image, command=is_known, highlightthickness=0, padx=50, pady=50)
tick_button.grid(column=0, row=1)

next_card()

window.mainloop()
