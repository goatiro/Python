# import
from tkinter import *
import requests
from bs4 import BeautifulSoup
import random

# window_option
win = Tk()

win.title("Lotto ver1.0")

win.geometry('500x300')

win.resizable(False, False)

win.option_add("*Font", "맑은고딕 16")

# <return> event


def enter(event):
    main_func()

# main_lotto_function


def main_func():
    n = ent2.get()
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(
        n)
    # div class="win.result"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    txt = soup.find("div", attrs={"class", "win_result"}).get_text()
    #num = txt.split("\n")[7:13]
    global num
    global bonus
    num = []
    bonus = []
    # prize
    p0 = 0
    p1 = 2000000000
    p2 = 55000000
    p3 = 1500000
    p4 = 50000
    p5 = 5000

    for i in range(7, 13):
        num.append(int(txt.split("\n")[i]))

    bonus.append(int(txt.split("\n")[-4]))

    for i in range(0, int(ent1.get())):
        # random_number
        rnd = []
        while len(rnd) < 6:
            rnd.append(random.randint(1, 45))
            a = set(rnd)
            rnd = list(a)
        print(rnd)
        same1 = len(set(num) & set(rnd))
        same2 = len(set(bonus) & set(rnd))
        same3 = same1+same2
        print(same3)
        if same1 == 6:
            p0 = p0+p1
            print("1st prize")
        elif same1 == 5 and same2 == 1:
            p0 = p0+p2
            print("2nd prize")
        elif same3 == 5:
            p0 = p0+p3
            print("3rd prize")
        elif same3 == 4:
            p0 = p0+p4
            print("4th prize")
        elif same3 == 3:
            p0 = p0+p5
            print("5th prize")
        else:
            print("No prize")
    print("Total prize : ", p0)

    lab2.config(text="[당첨번호]")
    lab3.config(text=num)
    lab4.config(text="[보너스]")
    lab5.config(text=bonus)


# Label/Entry/Button
lab0 = Label(win)
lab0.config(text="반복 횟수")
lab0.pack()

ent1 = Entry(win)
ent1.pack()

lab1 = Label(win)
lab1.config(text="복권 회차")
lab1.pack()

ent2 = Entry(win)
ent2.pack()

btn = Button(win)
btn.config(text="입력")
btn.config(width=20)
btn.config(command=main_func)

btn.pack()

win.bind('<Return>', enter)

lab2 = Label(win)
lab2.pack()
lab3 = Label(win)
lab3.pack()
lab4 = Label(win)
lab4.pack()
lab5 = Label(win)
lab5.pack()

win.mainloop()
