from tkinter import *
import tkinter.scrolledtext, tkinter.ttk, tkinter.messagebox
import csv

login_window=tkinter.Tk()
login_window.title('')
display_width=200
display_height=300
login_window.resizable(height = False , width = False)
w1=login_window.winfo_screenwidth()//2-display_width//2
h1=login_window.winfo_screenheight()//2-display_height//2
login_window.geometry('{}x{}+{}+{}'.format(display_width,display_height, w1, h1))

def login():
    global cur_user
    check = 0
    type = ""
    log = log_ent.get()
    password = pass_ent.get()
    cur_user = log
    wb = "Welcome back " + cur_user
    with open("users.csv", "r", encoding="utf-8") as users_file_r:
        content = csv.DictReader(users_file_r, delimiter=";")

        for line in content:
            if log == line["login"] and password == line["password"]:
                check = 1
                type = line["type"]
                break

        if check == 0:
            tkinter.messagebox.showinfo("Error", "Wrong login or password!\ntry another or log in")
        else:
            if type == "user":
                user_window(wb)
            else:
                teacher_window(wb)

def register():
    global cur_user
    login_check = 0
    log = log_ent.get()
    password = pass_ent.get()
    cur_user = log
    wb = "Hello " + cur_user
    data = {"login":log,"password":password,"type":"user"}
    with open("users.csv", "r", encoding="utf-8") as users_file_r:
        content = csv.DictReader(users_file_r, delimiter=";")


        for line in content:
            if log==line["login"]:
                login_check=1
                tkinter.messagebox.showinfo("Error", "This login already taken!\ntry another or log in")
                break


        if login_check == 0:
            with open("users.csv", "a", encoding="utf-8",newline="") as users_file_a:
                writer = csv.DictWriter(users_file_a,fieldnames=["login","password","type"], delimiter=";")
                writer.writerow(data)
                user_window(wb)




def user_window(wb):
    login_window.withdraw()
    user_window = tkinter.Tk()
    user_window.title(wb)
    display_width = 400
    display_height = 200
    #user_window.resizable(height=False, width=False)
    w1 = user_window.winfo_screenwidth() // 2 - display_width // 2
    h1 = user_window.winfo_screenheight() // 2 - display_height // 2
    user_window.geometry('{}x{}+{}+{}'.format(display_width, display_height, w1, h1))

def teacher_window(wb):
    login_window.withdraw()
    user_window = tkinter.Tk()
    user_window.title(wb+" *teacher*")
    display_width = 400
    display_height = 200
    #user_window.resizable(height=False, width=False)
    w1 = user_window.winfo_screenwidth() // 2 - display_width // 2
    h1 = user_window.winfo_screenheight() // 2 - display_height // 2
    user_window.geometry('{}x{}+{}+{}'.format(display_width, display_height, w1, h1))




log_lbl = tkinter.Label(login_window, text="login",font=("Arial, 10"))
log_ent = tkinter.Entry(login_window,width=20,font=("Arial, 12"))
pass_lbl = tkinter.Label(login_window, text="password",font=("Arial, 10") )
pass_ent = tkinter.Entry(login_window,width=20,font=("Arial, 12"),show="*")
log_btn = tkinter.Button(login_window,text="Login",font=("Arial, 12"),command=login)
reg_btn = tkinter.Button(login_window,text="Register",font=("Arial, 12"),command=register)

log_lbl.place(x=10,y=5)
log_ent.place(x=10,y=30)
pass_lbl.place(x=10,y=55)
pass_ent.place(x=10,y=80)
log_btn.place(x=10,y=110)
reg_btn.place(x=80,y=110)


login_window.mainloop()