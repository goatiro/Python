# import
from tkinter import *
from datetime import datetime
import requests
from bs4 import BeautifulSoup

win = Tk()

win.title("Lotto")

win.geometry('500x300')

win.resizable(False, False)

win.option_add("*Font", "맑은고딕 16")


def lotto_p():
    n = ent.get()
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(
        n)
    # div class="win.result"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    txt = soup.find("div", attrs={"class", "win_result"}).get_text()
    num = txt.split("\n")[7:13]
    bonus = txt.split("\n")[-4]

    lab2.config(text="[당첨번호]")
    lab3.config(text=num)
    lab4.config(text="[보너스]")
    lab5.config(text=bonus)


lab = Label(win)
lab.config(text="회차 입력")
lab.pack()

ent = Entry(win)
ent.pack()

btn = Button(win)
btn.config(text="번호 확인")
btn.config(width=20)
btn.config(command=lotto_p)

btn.pack()

lab2 = Label(win)
lab2.pack()
lab3 = Label(win)
lab3.pack()
lab4 = Label(win)
lab4.pack()
lab5 = Label(win)
lab5.pack()

win.mainloop()
