import random
from tkinter import *
import tkinter as tk

random=random.sample(range(1,101),1)[0]
print(random)
window=Tk()

def a():
    def c():
        window3=Tk()

        if int(entry.get())<random:
                tk.Label(window3, text='업!').grid(row=0, column=0, padx=10, pady=10)
        if int(entry.get())>random:
                tk.Label(window3, text='다운!').grid(row=0, column=0, padx=10, pady=10)
        if int(entry.get())==random:
            print("정답")
            tk.Label (window3, text='정답입니다!').grid(row=0, column=0, padx=10, pady=10)
        
         
            
    window2=Tk()
    label = tk.Label(window2, text='컴퓨터가 고른 숫자를 맞춰라!(1~100)')
    entry = tk.Entry(window2)
    button = tk.Button(window2, text='Enter',command=c)

    label.grid(row=0, column=0, padx=10, pady=10)
    entry.grid(row=1, column=0, padx=12, pady=10)
    button.grid(row=2, column=0, padx=13, pady=10)


def b():
    window.destroy()
    

tk.Label(window, text ='게임을 시작하시겠습니까?').grid(row=0, column=0, padx=30, pady=10)
tk.Button(window, text= '예', command=a).grid(row=1, column=1, padx=3, pady=10)
tk.Button(window, text= '아니요',command=b).grid(row=1, column=2, padx=3, pady=10)



window.mainloop()
