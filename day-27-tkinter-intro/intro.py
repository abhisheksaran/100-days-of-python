from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=800)
window.config(padx=20, pady=20)

# Label

my_label = Label(text="I am a label", font=("Arial", 26, "bold"))
my_label.pack()


# Button

def change_the_lable_name():
    """
    modify the label name
    """
    my_label.config(text="The button got clicked")
    my_label.pack(side="bottom")


my_button = Button(text="click me", command=change_the_lable_name)

# 3 ways to put it into GUI
my_button.pack()
# my_button.place(x=20, y=30)
# my_button.grid(column=2, row=2)


# Entry

entry = Entry()
entry.insert(END, string="Type sth here")
entry.pack()
print(entry.get())

# Text
text = Text(height=5, width=40)
text.focus()
text.insert(END, "Example of multiline text entry")
# print text from first line and 4th character in zero indexing system
print(text.get("1.4", END))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Check Button
def checkbutton_used():
    print(checked_state.get())


# Variable to hold the checked button state, 1 is on, 0 is off
checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radio Button
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Banana", "Grapes", "Mango"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



window.mainloop()
