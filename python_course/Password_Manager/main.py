import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    letters = [_ for _ in list(range(65, 91))+list(range(97, 123))]
    numbers = [_ for _ in range(48, 58)]
    symbols = [_ for _ in list(range(33, 48))+list(range(58, 65))]
    rand_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    rand_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    rand_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password = [chr(_) for _ in rand_letters+rand_numbers+rand_symbols]
    random.shuffle(password)
    password = "".join(password)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pwd_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if not website or not email or not password:
        messagebox.showwarning(title="Password Manager", message="All fields are required")
        return
    option = messagebox.askyesno(title=website, message=f"This are the details entered :\n\nEmail: {email}\n"
                                               f"Password: {password}\nIs it ok to save?")
    if option:
        website_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)
        new_data = {website:{
            "email":email,
            "password":password,
        }}
        try:
            with open("python_course/Password_Manager/TOP-SECRET.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        with open("python_course/Password_Manager/TOP-SECRET.json", "w") as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo(title="Password Manager", message="Password added successfully.")
# ---------------------------- LOAD PASSWORD ------------------------------- #
def load_pwd_data():
    website = website_entry.get()
    try:
        with open("python_course/Password_Manager/TOP-SECRET.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
        return
    item = data.get(website)
    if item:
        messagebox.showinfo(title=website, message=f"Email/Username : {item['email']}\nPassword : {item['password']}")
    else:
        messagebox.showinfo(title=website, message="No details for the website exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file="python_course/Password_Manager/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website : ")
website_label.grid(row=1, column=0)
website_entry = tkinter.Entry(width=27)
website_entry.grid(row=1, column=1, sticky="w")
website_load = tkinter.Button(text="Load password", command=load_pwd_data, width=15)
website_load.grid(row=1, column=2, sticky="w")

email_label = tkinter.Label(text="Email/Username : ")
email_label.grid(row=2, column=0)
email_entry = tkinter.Entry(width=44)
email_entry.insert(0, "gimjh003@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")

password_label = tkinter.Label(text="Password : ")
password_label.grid(row=3, column=0)
password_entry = tkinter.Entry(width=27)
password_entry.grid(row=3, column=1, sticky="w")
password_generator = tkinter.Button(text="Generate Password", command=generate_pwd)
password_generator.grid(row=3, column=2, sticky="w")

add = tkinter.Button(text="Add", width=43, command=add_pwd_data)
add.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()