from customtkinter import *
from PIL import Image
import random
from os.path import exists
import json


FILE_PATH = "main.json"


def getData():

    if not exists(FILE_PATH):
        return{}
    f = open(FILE_PATH, "r")
    data = f.read()
    return json.loads(data)

def setData(data):
    f = open(FILE_PATH, "w")
    jsonData = json.dumps(data)
    f.write(jsonData)

def account_number():

    
    random_number = random.randint(1000000, 9999999)
    number = str(random_number)

    return number

def create_user(name, balance):
    users = getData()
    user_number = account_number()
    users[user_number] = {
        "name": name, "balance": balance
    }
    setData(users)

def delete_user(user_number):

    users = getData()
    if user_number not in users: 
        print("No account :(")
        return
    del users[user_number]
    setData(users)

def transaction(skicka_pengar_snubbe, få_pengar_snubbe, amount):
    users = getData()

    if skicka_pengar_snubbe not in users:
        print("Donkey, el numero " + skicka_pengar_snubbe + " not existo")
        return
    
    if få_pengar_snubbe not in users: 
        print("Twat, el numero " + få_pengar_snubbe + " not existo")
        return
    
    if users[skicka_pengar_snubbe]["balance"] < amount:
        print("imbecile, you've got no fucking money")
        return
    

    users[skicka_pengar_snubbe]["balance"] -= amount
    users[få_pengar_snubbe]["balance"] += amount
    print(amount, "kronooarnonro sent from user:", skicka_pengar_snubbe, "name:", users[skicka_pengar_snubbe]["name"], "Money recieved by user:", få_pengar_snubbe, "name:", users[få_pengar_snubbe]["name"])
    setData(users)

def user_details(user_number):

    users = getData()

    print("\n\nUser number:", user_number)
    print("\n\nName:", users[user_number]["name"])
    print("Balance: ", users[user_number]["balance"], "krrorronrrnnonronr\n\n")
    

"""
while True:
    print("1: Create user")
    print("2: Transaction")
    print("3: Delete user")
    print("4: Show user details")
    print("5: Stop program")

    choice = int(input("Option: "))

    if choice == 1:
        print("Creating user")
        name = input("Name: ")
        balance = float(input("balance: "))
        create_user(name, balance)
        print("User created")
    
    if choice == 2:
        print("Transaction between users")
        skicka = input("User number of sender: ")
        få = input("User number of recipient: ")
        amount = float(input("Amount of money in transaction: "))
        transaction(skicka, få, amount)
        

    
    if choice == 3:
        print("Delete user")
        user_number = input("User_number of user to delete: ")
        delete_user(user_number)
        print("User deleted\n")

    if choice == 4:
        print("Show user details")
        user_number = input("Show detail from this user number: ")
        user_details(user_number)
    
    
    if choice == 5:
        break
"""



app = CTk()
app.geometry("600x400")


#Alla CTk funktioner
"""
def gone():
    Usercreation_.destroy()
    Transaction_.destroy()
    Del_.destroy()
    Exit_.destroy()

def start():
    Usercreation_.place(relx=0.5, rely=0.4, anchor="center")
    Transaction_.place(relx=0.5, rely=0.5, anchor="center")
    Del_.place(relx=0.5, rely=0.6, anchor="center")
    Exit_.place(relx=0.5, rely=0.7, anchor="center")

def getting():
    name = name_.get()
    balance = balance_.get()
    create_user(name, balance)
    name_.destroy()
    balance_.destroy()
    btn.destroy()
    start()

def guh():
    user_number = Delnumber_.get()
    delete_user(user_number)
    Delnumber_.destroy()
    Delete_.destroy()
    start()

def Tdone():
    skicka = first_.get()
    få = second_.get()
    amount = amount_.get()
    transaction(skicka, få, amount)
    first_.destroy()
    second_.destroy()
    amount_.destroy()
    TDone_.destroy()
    start()

def delete():
    gone()
    Delnumber_.place(relx=0.5, rely=0.4, anchor="center")
    Delete_.place(relx=0.5, rely=0.5, anchor="center")

def yup():  
    gone()
    name_.place(relx=0.5, rely=0.4, anchor="center")
    balance_.place(relx=0.5, rely=0.5, anchor="center")
    btn.place(relx=0.5, rely=0.6, anchor="center")

def trr():
    gone()
    first_.place(relx=0.5, rely=0.4, anchor="center")
    second_.place(relx=0.5, rely=0.5, anchor="center")
    amount_.place(relx=0.5, rely=0.6, anchor="center")
    TDone_.place(relx=0.5, rely=0.7, anchor="center")

def exit():
    app.destroy()
"""    

#-------------------frames------------------------
BankPage = CTkFrame(master=app, width=200, height=200, corner_radius=20, bg_color="yellow")

RegPage = CTkFrame(master=app, width=600, height=360, corner_radius=20, bg_color="blue")

FPage = CTkFrame(master=app, width=600, height=360, corner_radius=20, bg_color="green")

FPage.pack()


#CTk för image
image = Image.open("shartv1.png")
l_image = CTkImage(image, size=(100, 100))

label = CTkLabel(app, text="", image=l_image)
label.place(relx=0.1, rely=0.1, anchor="center")


#CTk för User creation
name_ = CTkEntry(master=app, placeholder_text="Name", width=300, 
                text_color="#FFCC70")

balance_ = CTkEntry(master=app, placeholder_text="How many money", width=300, 
                text_color="#FFCC70")

btn = CTkButton(master=app, text="Create user", corner_radius=32, fg_color="transparent",
                hover_color="#4158D0", border_color="#FFCC70", 
                border_width=2, command=getting)

Usercreation_ = CTkButton(master=app, text="Create user", corner_radius=32, fg_color="transparent",
                hover_color="#4158D0", border_color="#FFCC70", 
                border_width=2, command=yup)


#CTk för transaction
first_ = CTkEntry(master=app, placeholder_text="Usernumber of sender", width=300, 
                text_color="#FFCC70")

second_ = CTkEntry(master=app, placeholder_text="Usernumber of recipient", width=300, 
                text_color="#FFCC70")

amount_ = CTkEntry(master=app, placeholder_text="Amount", width=300, 
                text_color="#FFCC70")

Transaction_ = CTkButton(master=app, text="Transaction", corner_radius=32, fg_color="transparent",
                hover_color="#4158D0", border_color="#FFCC70", 
                border_width=2, command=trr)

TDone_ = CTkButton(master=app, text="Done", corner_radius=32, fg_color="transparent",
                hover_color="#4158D0", border_color="#FFCC70", 
                border_width=2, command=Tdone)


#CTk för delete users
Delnumber_ = CTkEntry(master=app, placeholder_text="Usernumber of user to delete", width=300, 
                text_color="#FFCC70")

Delete_ = CTkButton(master=app, text="Delete", corner_radius=32, fg_color="transparent",
                hover_color="#4158D0", border_color="#FFCC70", 
                border_width=2, command=guh)

Del_ = CTkButton(master=app, text="Done", corner_radius=32, fg_color="transparent",
                hover_color="#4158D0", border_color="#FFCC70", 
                border_width=2, command=delete)


#CTk för exit
Exit_ = CTkButton(master=app, text="Exit", corner_radius=32, fg_color="transparent",
                hover_color="#4158D0", border_color="#FFCC70", 
                border_width=2, command=exit)


start()

app.mainloop()




"""
def clicked():
    print(f"Name: {entry.get()} {entry2.get()}")
    btn.destroy()
    entry.destroy()
    entry2.destroy()
    btn2.place(relx=0.5, rely=0.5, anchor="center")
def clicked2():
    btn2.destroy()
    entry3.place(relx=0.5, rely=0.4, anchor="center")
    btn3.place(relx=0.5, rely=0.5, anchor="center")

def clicked3():
    print(f"Summa: {entry3.get()}")"""
