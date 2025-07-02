from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.config(pady=50,padx=50)
window.title("Password Manager")
canvas=Canvas(width=200,height=200)
photo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(row=0,column=1)
website_name=Label(text="Website:")
website_name.grid(row=1,column=0)
user_name=Label(text="Email/Username:")
user_name.grid(row=2,column=0)
password=Label(text="Password:")
password.grid(row=3,column=0)
website_input=Entry(width=35)
website_input.focus()
website_input.grid(row=1,column=1,columnspan=2)
user_name_input=Entry(width=35)
user_name_input.insert(0,"username@gmail.com")
user_name_input.grid(row=2,column=1,columnspan=2)
password_input=Entry(width=21,highlightthickness=0)
password_input.grid(row=3,column=1)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global first
    w=website_input.get()
    u=user_name_input.get()
    p=password_input.get()

    if len(w)==0 or len(u)==0 or len(p)==0:
        messagebox.showinfo(title="Empty Field", message="No field should empty")
    else:
        is_ok=messagebox.askyesno(title="Final call",message=f"details you entered :-\nwebsite:{w}\nusername: {u}\npassword:{p}\nis okay to submit ?")
        if is_ok:
            with open("passwords.txt", mode="a") as file:
                file.write(f"{w} | {u} | {p}\n")
            website_input.delete(0, END)
            user_name_input.delete(0, END)
            password_input.delete(0, END)

add=Button(text="Add",bg="white",width=35,highlightthickness=0,command=save)
add.grid(row=4,column=1,columnspan=2)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generator():
    password_input.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_input.insert(0,f"{password}")
generate_password=Button(text="Generate Password",highlightthickness=0,bg="white",command=generator)
generate_password.grid(row=3,column=2,columnspan=2)
window.mainloop()
