from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

# ---------------------------- Set up the UI ------------------------------- #
window = Tk()
window.title("Flashcard Project")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Create the canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="French", font=(FONT_NAME, 40, "italic"))
the_word = canvas.create_text(400, 263, text="the word", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Create the buttons
tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, padx=50, pady=50)
tick_button.grid(column=0, row=1)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, padx=50, pady=50)
cross_button.grid(column=1, row=1)


window.mainloop()
