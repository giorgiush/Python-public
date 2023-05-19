import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- SEARCH DATA ------------------------------- #


def search():
    WEB = website_entry.get().lower()
    try:
        with open("./days_29_and_30_password_manager/Credentials.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message="Not found")
    else:
        if WEB in data:
            messagebox.showinfo(title=f"{WEB}", message=f"Login: {data[WEB]['Login']}\nPassword: {data[WEB]['Password']}\n\npassword copied to clipboard")
            pyperclip.copy(data[WEB]['Password'])
        else:
            messagebox.showinfo(title="ERROR", message="Not found")
    finally:
        website_entry.delete(0, tkinter.END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    pass_entry.delete(0, tkinter.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password1 = [random.choice(letters) for i in range(random.randint(8,10))]
    password2 = [random.choice(numbers) for i in range (random.randint(3,5))]
    password3 = [random.choice(symbols) for i in range (random.randint(3,5))]
    password = password1+password2+password3
    random.shuffle(password)
    PASSWORD = ''.join(password)
    pass_entry.insert(0, PASSWORD)
    pyperclip.copy(PASSWORD)
    
    
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    WEB = website_entry.get().lower()
    MAIL = mail_entry.get()
    PASS = pass_entry.get()
    new_entry = {
        WEB: {
            "Login": MAIL,
            "Password": PASS
        }
    }
    
    if len(WEB) == 0 or len(MAIL) == 0 or len(PASS) ==0:
        messagebox.showinfo(title="ERROR", message="Field(s) empty")
        return
    else:
        OK = messagebox.askokcancel(title=WEB, message=f"Login: {MAIL}\nPassword: {PASS}")
        if OK:
            try:
                with open("./days_29_and_30_password_manager/Credentials.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("./days_29_and_30_password_manager/Credentials.json", "w") as file:
                    json.dump(new_entry, file, indent=4)
            else:
                data.update(new_entry)
                with open("./days_29_and_30_password_manager/Credentials.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, tkinter.END)
                pass_entry.delete(0, tkinter.END)
        
    
# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file="./days_29_and_30_password_manager/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)


website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)


website_entry = tkinter.Entry(width=36)
website_entry.grid(row=1, column=1)
website_entry.focus()


website_search = tkinter.Button(text="Search", width=15, command=search)
website_search.grid(row=1, column=2)


mail_label = tkinter.Label(text="Email/Username:")
mail_label.grid(row=2, column=0)


mail_entry = tkinter.Entry(width=55)
mail_entry.grid(row=2, column=1, columnspan=2)
mail_entry.insert(0, "non@existant.email")


pass_label = tkinter.Label(text="Password:")
pass_label.grid(row=3, column=0)


pass_entry = tkinter.Entry(width=36)
pass_entry.grid(row=3, column=1)


pass_button = tkinter.Button(text="Generate Password", command=generate_password)
pass_button.grid(row=3, column=2)


add_button = tkinter.Button(text="Add", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()