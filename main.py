from customtkinter import *

app = CTk()
app.geometry("600x400")

def clicked():
    print(f"Name: {entry.get()} {entry2.get()}")
    btn.destroy()
    entry.destroy()
    entry2.destroy()

btn = CTkButton(master=app, text="Done", corner_radius=32, fg_color="transparent",
                hover_color="#4158D0", border_color="#FFCC70", 
                border_width=2, command=clicked)

entry = CTkEntry(master=app, placeholder_text="Förnamn", width=300, 
                text_color="#FFCC70")

entry2 = CTkEntry(master=app, placeholder_text="Efternamn", width=300, 
                text_color="#FFCC70")

entry.place(relx=0.5, rely=0.4, anchor="center")

entry2.place(relx=0.5, rely=0.5, anchor="center")

btn.place(relx=0.5, rely=0.6, anchor="center")


app.mainloop()



class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        return f"Thank you, {self.age} year old, {self.name.title()}"
        
class Bank(user):
    total_deposits = 0
    total_withdraws = 0

    def __init__(self, name, age, balance):
        super().__init__(name, age)
        self.balance = balance

    def show_info(self):
        return f"{self.name} has a remaining balance of: ${round(self.balance, 2)}"
    
