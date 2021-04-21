from tkinter import *
import tkinter.scrolledtext, tkinter.ttk, tkinter.messagebox, random
import csv
root = tkinter.Tk()
root.configure(background='white')
root.geometry('400x300')
root.resizable(width=False, height=False)
#scheduledimage=tkinter.PhotoImage('C:\\Users\\Admin\\Desktop\\Rus\\k.ico')

def new():
    login_window = tkinter.Tk()
    login_window.title('')
    display_width = 200
    display_height = 300
    login_window.resizable(height=False, width=False)
    w1 = login_window.winfo_screenwidth() // 2 - display_width // 2
    h1 = login_window.winfo_screenheight() // 2 - display_height // 2
    login_window.geometry('{}x{}+{}+{}'.format(display_width, display_height, w1, h1))
    note = tkinter.ttk.Notebook(login_window)
    tab1 = tkinter.Frame(note)
    tab2 = tkinter.Frame(note)
    tab3 = tkinter.Frame(note)
    note.add(tab1, text = "Питання-1")
    note.add(tab2, text = "Питання-2")
    note.add(tab3, text = "Питання_3")
    note.pack(fill='both', expand=True)

    easyQ = [
        [   "Що є результатом виконання фрагменту програми якщо x=34? \n print(float(x))",
            "34.0",       "34.000000",         "34",         "34.00"  ],
        [   "Вкажіть результат операції? \nX = 2+9*((3*12)-8)/10",
            "30.8",         "27.2",         "28.4",         "30.0"  ],
        [  "Що не належить до типів даних пайтон?",
            "integer",         "float",         "string",         "canvas"   ],
        [   "Який з класів застосовується \nдля формування віджета кнопки-прапорця",
            "canvas",         "radiobutton",         "checkbutton",         "notebook"   ]  ]
    answer = [ "checkbutton","34.0", "27.2", "canvas" ]

    def calc():
        global score
        score=0
        if (var.get() in answer):
            score += 1
        if (var1.get() in answer):
            score += 1
        if (var2.get() in answer):
            score += 1
        showMark(score)

    def start():
        global var, var1, var2
        li = [0, 1, 2, 3]
        x = random.choice(li[:])
        ques = tkinter.Label(tab1, text=easyQ[x][0]).pack()
        var = tkinter.StringVar()
        i=1
        while i<=4:
            tkinter.Radiobutton(tab1, text=easyQ[x][i], value=easyQ[x][i], variable=var).pack()
            i+=1
        var.set(-1)
        but1 = tkinter.Button(tab1, text='but', command=calc)
        but1.place(relx=0.5, rely=0.82, anchor='center')
        #root.mainloop()

        li.remove(x)
        x = random.choice(li[:])
        ques = tkinter.Label(tab2, text=easyQ[x][0]).pack()

        var1 = tkinter.StringVar()
        i = 1
        while i <= 4:
            tkinter.Radiobutton(tab2, text=easyQ[x][i], value=easyQ[x][i], variable=var1).pack()
            i += 1
        var1.set(-1)

        li.remove(x)
        x = random.choice(li[:])
        ques = tkinter.Label(tab3, text=easyQ[x][0]).pack()
        var2 = tkinter.StringVar()
        i = 1
        while i <= 4:
            tkinter.Radiobutton(tab3, text=easyQ[x][i], value=easyQ[x][i], variable=var2).pack()
            i += 1
        var2.set(-1)

    def showMark(mark):
        global sh
        sh = tkinter.Tk()
        st = "Your score is " + str(mark)
        mlabel = tkinter.Label(sh, text=st)
        mlabel.place(relx=0.5, rely=0.2, anchor='center')
        sh.mainloop()
    start()
button = tkinter.Button(root,text="open" ,command=new).pack()
root.mainloop()