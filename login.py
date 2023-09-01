# tkinter를 사용하기 위한 import
from tkinter import *
import tkinter as tk            

# tkinter 객체 생성
window = Tk()

# 사용자 id와 password를 저장하는 변수 생성
user_id, password = '', ''

# 사용자 id와 password를 비교하는 함수
def check_data():
    if user_id.get() == "Passing" and password.get() == "Story":
        # 새로운 화면 생성
        newwin = Tk()
        tk.Label(newwin, text="Welcome to " + user_id.get()).grid(row = 0, column = 0, padx = 10, pady = 10)
        newwin.mainloop()
        print("Logged IN Successfully")
    else:
        print("Check your Username/Password")

# id와 password, 그리고 확인 버튼의 UI를 만드는 부분
tk.Label(window, text = "Username : ").grid(row = 0, column = 0, padx = 10, pady = 10)
tk.Label(window, text = "Password : ").grid(row = 1, column = 0, padx = 10, pady = 10)
tk.Entry(window, textvariable = user_id).grid(row = 0, column = 1, padx = 10, pady = 10)
tk.Entry(window, textvariable = password, show='*').grid(row = 1, column = 1, padx = 10, pady = 10)
tk.Button(window, text = "Login", command = check_data).grid(row = 2, column = 1, padx = 10, pady = 10)

window.mainloop()
