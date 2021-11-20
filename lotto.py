# import
import tkinter
from tkinter import ttk
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# instance
win = tkinter.Tk()

# title
win.title("First Window")

# geomerty
win.geometry('700x400')

# preventing GUI from resizing
win.resizable(False, False)

win.option_add("*Font", "맑은고딕 20")


def what_time():
    dnow = datetime.now()
    btn.config(text=dnow)


def ent_p():
    inp = ent.get()
    print(inp)


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

    print("당첨번호")
    print(num)
    print("보너스번호")
    print(bonus)


ent = ttk.Entry(win)

ent.pack()

btn = ttk.Button(win)
btn.config(text="번호 확인")
btn.config(width=20)
btn.config(command=lotto_p)

btn.pack()

win.mainloop()
