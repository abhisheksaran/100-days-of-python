from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_countdown():
    start_button.config(state="active")
    window.after_cancel(timer_sec)
    window.after_cancel(timer_min)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    # if you press start when timer is already running, it will malfunction
    # Thus once the timer has started we can disable start button
    start_button.config(state="disable")
    global reps
    reps += 1
    # print(f"the rep number is {reps} started")
    if reps % 8 == 0:
        # print("long break")
        start_countdown(LONG_BREAK_MIN)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        # print("short break")
        start_countdown(SHORT_BREAK_MIN)
        title_label.config(text="Break", fg=PINK)
    else:
        # print("work")
        start_countdown(WORK_MIN)
        title_label.config(text="Work", fg=GREEN)
    # print(f"the rep number is {reps} finished")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_countdown(minute_time):
    countdown_minutes(minute_time)
    # print(f"countdown {minute_time} done")


def countdown_seconds(mint, sec):
    if sec >= 0:
        # print(f"inside countdown_seconds: {mint}:{sec}")
        canvas.itemconfig(timer_text, text=f"{mint:02d}:{sec:02d}")
        global timer_sec
        timer_sec = window.after(1000, countdown_seconds, mint, sec - 1)


def countdown_minutes(mint):
    if mint > 0:
        # print(f"Minute={mint}")
        # print("countdown 1 min started")
        countdown_seconds(mint - 1, 59)
        # print("countdown 1 min finished")
        global timer_min
        timer_min = window.after(60000, countdown_minutes, mint - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✅"
        checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create the canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# TODO Create the labels
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "normal"))
title_label.grid(column=1, row=0)

checkmark_label = Label(bg=YELLOW)
checkmark_label.grid(column=1, row=3)

# TODO Create the buttons
start_button = Button(text="Start", bg=YELLOW, command=start_timer, highlightthickness=0, borderwidth=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, command=reset_countdown, highlightthickness=0, borderwidth=0)
reset_button.grid(column=2, row=2)

window.mainloop()
