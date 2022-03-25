from tkinter import *


def miles_to_km():
    miles = float(entry.get())
    km = miles * 1.609
    label_ans.config(text=f"{km}")


# Create tkinter window
window = Tk()
window.title("Miles to KM")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Create the text entry
entry = Entry(width=10)
entry.focus()
entry.grid(column=1, row=0)

# Create labels
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_iseq = Label(text="is equal to")
label_iseq.grid(column=0, row=1)

label_ans = Label(text="0")
label_ans.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

# Create Button
button_cal = Button(text="Calculate", command=miles_to_km)
button_cal.grid(column=1, row=2)

window.mainloop()
