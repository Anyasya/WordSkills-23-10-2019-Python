import tkinter as tk
import json

TITLE = "Authentification"

WIDTH = 140
HEIGHT = 150

# Classes and Utils functions


def load_data ():
    datafile = open('data.json', 'r')
    data = json.load(datafile)
    print('data has been loaded')
    return data

data = load_data()
new = {}

def save_data (new,data):
    with open("data.json", "w") as write_file:
        data['posts'].append(new)
        json.dump(data, write_file)        
        print('data is ',data)
        

root = tk.Tk()
root.title(TITLE)
root.geometry(str(WIDTH)+'x'+str(HEIGHT))
root.resizable(False, False)

# And other root configs

# Programm functions and Event handlers

def sign_up (new,data):
    login = entry_login.get()
    password = entry_password.get()
    new = {login:password}
    
    save_data(new,data)


def log_in (data):
    # grab login and password input
    login = entry_login.get()
    password = entry_password.get()

    # iterate over data['posts'] array
    print(data)
    for post in data["posts"]:
        # check if post's login and password match
        if post.get('login') == login and post.get('password') == password:
            print('Succesful!')
            return None
    else:
            print('Uncorrect')
    


# Forms Creating and Binding

label_login = tk.Label(root, text='Login:',)
entry_login = tk.Entry(root)

label_password = tk.Label(root, text='Password:')
entry_password = tk.Entry(root, show='*')

button_login = tk.Button(root, text='LogIn', command=lambda:log_in(data))
button_signup = tk.Button(root, text='SignUp', command=lambda:sign_up(new,data))


label_login.place(x=10, y=10)
entry_login.place(x=10, y=35)
label_password.place(x=10, y=60)
entry_password.place(x=10, y=85)

button_login.place(x=10, y=115, width=50, height=25)
button_signup.place(x=80, y=115, width=50, height=25)




root.mainloop()
