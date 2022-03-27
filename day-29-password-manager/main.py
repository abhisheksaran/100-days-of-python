from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def set_password():
    random_password = generate_password()
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)


def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    # Validate the entries ie entries don't contain any whitespace or are empty.
    if not website or not username or not password:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any field empty.")
        is_ok = False
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f'These are the detail entered: \nEmail/Username: {username}\nPassword: {password}')

    if is_ok:
        with open("data.txt", "a") as f:
            entry = " | ".join([website, username, password]) + "\n"
            # print(entry)
            f.write(entry)

    # Clear the entries
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Create the canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Create the labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Create the entries
website_entry = Entry(width=38)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=38)
username_entry.insert(0, "abhishekbishnoi694@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Create buttons
genpass_button = Button(text="Generate Password", command=set_password)
genpass_button.grid(column=2, row=3)

save_button = Button(text="Add", command=save_password, width=36)
save_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
