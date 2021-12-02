# import
from tkinter import *
import requests
from bs4 import BeautifulSoup
import random
# prize
p1 = 2000000000
p2 = 55000000
p3 = 1500000
p4 = 50000
p5 = 5000
# random_number
rnd = []

while len(rnd) < 6:
    rnd.append(random.randint(1, 45))
    a = set(rnd)
    rnd = list(a)

print(rnd)
# window_option
win = Tk()

win.title("Lotto ver1.0")

win.geometry('500x300')

win.resizable(False, False)

win.option_add("*Font", "맑은고딕 16")

# <return> event


def enter(event):
    lotto_p()

# main_lotto_function


def lotto_p():
    n = ent.get()
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

    for i in range(7, 13):
        num.append(int(txt.split("\n")[i]))

    bonus.append(int(txt.split("\n")[-4]))
    same1 = len(set(num) & set(rnd))
    same2 = len(set(bonus) & set(rnd))
    print(same1)
    print(same2)

    lab2.config(text="[당첨번호]")
    lab3.config(text=num)
    lab4.config(text="[보너스]")
    lab5.config(text=bonus)


lab = Label(win)
lab.config(text="반복 횟수")

ent = Entry(win)
ent.pack()

btn = Button(win)
btn.config(text="입력")
btn.config(width=20)
btn.config(command=lotto_p)

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
