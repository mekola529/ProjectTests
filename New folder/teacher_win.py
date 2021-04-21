from tkinter import *
import tkinter.scrolledtext, tkinter.ttk, tkinter.messagebox
import csv

global count
count = 1

teacher_window = tkinter.Tk()
teacher_window.title("*teacher*")
display_width = 400
display_height = 350
#user_window.resizable(height=False, width=False)
w1 = teacher_window.winfo_screenwidth() // 2 - display_width // 2
h1 = teacher_window.winfo_screenheight() // 2 - display_height // 2
teacher_window.geometry('{}x{}+{}+{}'.format(display_width, display_height, w1, h1))
nav = tkinter.ttk.Notebook(teacher_window)
tab1 = tkinter.Frame(nav)
tab2 = tkinter.Frame(nav)
tab3 = tkinter.Frame(nav)
nav.add(tab2, text="Create test")
nav.add(tab1, text="Students")
nav.add(tab3, text="Manage tests")
nav.pack(fill='both', expand=True)



def create_test():
    global count
    name = test_name_ent.get()
    test_level = ""
    right_answer = ""
    if ind.get() == 1:
        right_answer = answ1.get()
    elif ind.get() == 2:
        right_answer = answ2.get()
    elif ind.get() == 3:
        right_answer = answ3.get()
    elif ind.get() == 4:
        right_answer = answ4.get()

    if ind2.get() == 1:
        test_level = "easy_tests"
    elif ind2.get() == 2:
        test_level = "medium_tests"
    elif ind2.get() == 3:
        test_level = "hard_tests"


    data = {"question": question_ent.get(), "answer1": answ1.get(), "answer2": answ2.get(), "answer3": answ3.get(),
            "answer4": answ4.get(), "right_answer": right_answer}

    link = test_level + "\\" + name + ".csv"

    with open(link, "a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file,fieldnames=["question", "answer1", "answer2", "answer3", "answer4", "right_answer"],delimiter=";")
        writer.writerow(data)

    question_ent.delete(0, 'end')
    answ1.delete(0, 'end')
    answ2.delete(0, 'end')
    answ3.delete(0, 'end')
    answ4.delete(0, 'end')

    count = 1
    test_name_ent['state'] = "normal"
    radio5['state'] = 'normal'
    radio6['state'] = 'normal'
    radio7['state'] = 'normal'
    test_name_ent.delete(0, 'end')
    question_ent.delete(0, 'end')
    answ1.delete(0, 'end')
    answ2.delete(0, 'end')
    answ3.delete(0, 'end')
    answ4.delete(0, 'end')


def next_question():
    global count
    name = test_name_ent.get()
    test_level = ""
    right_answer = ""
    test_name_ent['state'] = "readonly"
    radio5['state'] = 'disable'
    radio6['state'] = 'disable'
    radio7['state'] = 'disable'
    if ind.get() == 1:
        right_answer = answ1.get()
    elif ind.get() == 2:
        right_answer = answ2.get()
    elif ind.get() == 3:
        right_answer = answ3.get()
    elif ind.get() == 4:
        right_answer = answ4.get()

    if ind2.get() == 1:
        test_level = "easy_tests"
    elif ind2.get() == 2:
        test_level = "medium_tests"
    elif ind2.get() == 3:
        test_level = "hard_tests"

    radio1.deselect()



    data = {"question":question_ent.get(),"answer1":answ1.get(),"answer2":answ2.get(),"answer3":answ3.get(),"answer4":answ4.get(),"right_answer":right_answer}

    link = test_level+"\\"+name+".csv"

    if count==1:
        with open(link, "a", encoding="utf-8",newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["question", "answer1", "answer2", "answer3", "answer4", "right_answer"], delimiter=";")
            writer.writeheader()
            writer.writerow(data)
    else:
        with open(link, "a", encoding="utf-8",newline="") as file:
            writer = csv.DictWriter(file,fieldnames=["question", "answer1", "answer2", "answer3", "answer4", "right_answer"],delimiter=";")
            writer.writerow(data)

    question_ent.delete(0, 'end')
    answ1.delete(0, 'end')
    answ2.delete(0, 'end')
    answ3.delete(0, 'end')
    answ4.delete(0, 'end')
    ind.set(0)
    count += 1
    quest_count_lbl["text"] = "№"+str(count)





ind = tkinter.IntVar()
ind2 = tkinter.IntVar()



test_name_lbl = tkinter.Label(tab2,text="Enter test name")
test_name_ent = tkinter.Entry(tab2)
question_lbl = tkinter.Label(tab2, text="Enter question")
question_ent = tkinter.Entry(tab2)
quest_count_lbl = tkinter.Label(tab2, text="№1")
answ_lbl = tkinter.Label(tab2, text="Enter answer")
answ1 = tkinter.Entry(tab2)
answ2 = tkinter.Entry(tab2)
answ3 = tkinter.Entry(tab2)
answ4 = tkinter.Entry(tab2)
radio1 = tkinter.Radiobutton(tab2,variable=ind,value=1)
radio2 = tkinter.Radiobutton(tab2,variable=ind,value=2)
radio3 = tkinter.Radiobutton(tab2,variable=ind,value=3)
radio4 = tkinter.Radiobutton(tab2,variable=ind,value=4)
radio5 = tkinter.Radiobutton(tab2,text="Easy",variable=ind2,value=1)
radio6 = tkinter.Radiobutton(tab2,text="Medium",variable=ind2,value=2)
radio7 = tkinter.Radiobutton(tab2,text="Hard",variable=ind2,value=3)

next_ques_btn = tkinter.Button(tab2,text="Next question",command=next_question)
create_test_btn = tkinter.Button(tab2,text="End test",command=create_test)



test_name_lbl.grid(row=0,column=1)
test_name_ent.grid(row=1,column=1)
radio5.grid(row=2,column=0)
radio6.grid(row=2,column=1)
radio7.grid(row=2,column=2)
question_lbl.grid(row=3,column=1)
quest_count_lbl.grid(row=3,column=0)
question_ent.grid(row=4,column=1)
answ_lbl.grid(row=5,column=1)
answ1.grid(row=6,column=1)
answ2.grid(row=7,column=1)
answ3.grid(row=8,column=1)
answ4.grid(row=9,column=1)
radio1.grid(row=6,column=0)
radio2.grid(row=7,column=0)
radio3.grid(row=8,column=0)
radio4.grid(row=9,column=0)
next_ques_btn.grid(row=10,column=1)
create_test_btn.grid(row=11,column=1)



teacher_window.mainloop()