from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import string
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generete_pass():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_number + password_symbol

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Opps", message="Please dont leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"Saving info: \nEmail: {email} \nPassword: {password} \nConfirm to save.",
        )

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="E")
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="E")
pasaword_label = Label(text="Password:")
pasaword_label.grid(row=3, column=0, sticky="E")

# Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "prithbirajd@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

# Button
gen_pass_button = Button(text="Generate Password", command=generete_pass)
gen_pass_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()
