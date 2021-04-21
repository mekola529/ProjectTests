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

def new2 ():
    login1_window = tkinter.Tk()
    login1_window.title('')
    display_width = 200
    display_height = 300
    login1_window.resizable(height=False, width=False)
    w1 = login1_window.winfo_screenwidth() // 2 - display_width // 2
    h1 = login1_window.winfo_screenheight() // 2 - display_height // 2
    login1_window.geometry('{}x{}+{}+{}'.format(display_width, display_height, w1, h1))

    def testing():
        print(ind3.get(), ind4.get())

    global ind3
    global ind4
    ind3 = tkinter.IntVar()
    ind4 = tkinter.IntVar()

    radio100 = tkinter.Radiobutton(login1_window, variable=ind3, value=1)
    radio101 = tkinter.Radiobutton(login1_window, variable=ind3, value=2)
    radio102 = tkinter.Radiobutton(login1_window, variable=ind3, value=3)
    radio103 = tkinter.Radiobutton(login1_window, variable=ind3, value=4)
    radio104 = tkinter.Radiobutton(login1_window, text="Easy", variable=ind4, value=100)
    radio105 = tkinter.Radiobutton(login1_window, text="Medium", variable=ind4, value=200)
    radio106 = tkinter.Radiobutton(login1_window, text="Hard", variable=ind4, value=300)

    buttonka = tkinter.Button(login1_window, text="enter", command=testing).grid(row=7, column=0)

    radio100.grid(row=0, column=0)
    radio101.grid(row=1, column=0)
    radio102.grid(row=2, column=0)
    radio103.grid(row=3, column=0)
    radio104.grid(row=4, column=0)
    radio105.grid(row=5, column=0)
    radio106.grid(row=6, column=0)
def new():
    new2()

button = tkinter.Button(login_window,text="open" ,command=new).pack()


login_window.mainloop()