from tkinter import *
import random
from datetime import datetime

#
win = Tk()
win.title("AIM_GAME")
win.geometry("550x100")
win.option_add("*Font", "궁서 20")
#
lab = Label(win)
lab.config(text="표적 개수")
lab.grid(column=0, row=0, padx=20, pady=30)
#
ent = Entry(win)
ent.grid(column=1, row=0, padx=20, pady=30)

k = 1


def cc():
    global k
    if k < num_t:
        k += 1
        btn.destroy()
        ran_btn()
    else:
        fin = datetime.now()
        dif_sec = (fin-start).total_seconds()
        btn.destroy()
        lab = Label(win)
        lab.config(text="Clear\n"+str(dif_sec)+"초")
        lab.pack(pady=230)


def ran_btn():
    global btn
    btn = Button(win)
    btn.config(bg="red")
    btn.config(command=cc)
    btn.config(text=k)
    btn.place(relx=random.uniform(0.1, 0.9), rely=random.uniform(0.1, 0.9))


def btn_f():
    global num_t, start
    num_t = int(ent.get())
    for wg in win.grid_slaves():
        wg.destroy()
    win.geometry("500x500")
    ran_btn()
    start = datetime.now()


#
btn = Button(win)
btn.config(text="시작")
btn.config(command=btn_f)
btn.grid(column=2, row=0)

win.mainloop()
