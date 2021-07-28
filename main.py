from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

WHITE = "#EDF6E5"

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generator():

    password_list = [ choice(letters) for char in range ( randint(8, 10) )] + \
                    [ choice(symbols) for char in range ( randint(2, 4) ) ] + \
                    [ choice(numbers) for char in range ( randint(2, 4) ) ]
    shuffle(password_list)
    password = "".join(password_list)

    # Insert value to input box
    pass_input.insert(0, string=f"{password}")

    # Copy paste password immediately
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    user_web = web_input.get()
    user_email = user_input.get()
    user_pass = pass_input.get()

    new_data = {
        user_web: {
            "email:": user_email,
            "password:": user_pass,
        }
    }

    if len(user_web) == 0 or len(user_pass) == 0:
        messagebox.askretrycancel(title="Warning!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Update old data with new data
            data.update(new_data)

            with open("data.json", mode="w" ) as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)

#-----------------------------SEARCH WEBSITE---------------------------#


def find_password():
    website = web_input.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Warning!", message="File is not exist...")

    else:
        for (key, value) in data.items():
            if website in data:
                messagebox.showinfo(title="Your Information", message=f"Your Email is {data[website]['email:']}"
                                                                f"\nYour password is {data[website]['password:']}")
            else:
                messagebox.showinfo(title="Warning!", message="Website is not exist...")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

# Canvas

canvas = Canvas(width=200, height=200, bg=WHITE)
logo_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label

web_label = Label(text="Website:", bg=WHITE)
web_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:", bg=WHITE)
user_label.grid(column=0, row=2)

pass_label = Label(text="Password:", bg=WHITE)
pass_label.grid(column=0, row=3)


# Entry

web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

user_input = Entry(width=35)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0, "example@emal.com")

pass_input = Entry(width=35)
pass_input.grid(row=3, column=1)


# Button

generate_button = Button(text="Generate Passwword", width=20, command=generator)
generate_button.grid(column=3, row=3)

add_button = Button(text="Add", width=30, command= save )
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=20, command=find_password)
search_button.grid(column=3, row=1)
window.mainloop()