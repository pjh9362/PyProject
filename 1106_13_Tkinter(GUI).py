
# coding: utf-8

import tkinter as tk

# Tk 객체 인스턴스 생성
root = tk.Tk()

switch = False

# 버튼을 눌렀을 때 처리
def func():
    print("Pushed")
    global switch
    switch = not(switch)
    if switch:
        label.config(text = "apple")
    else:
        label.config(text = "orange")
    
    #label.config(text = 'Pushed')               # label 표시 변경

# 라벨 생성
label = tk.Label(root, text = 'Push Button')

# 라벨 배치
label.pack()

# 버튼 생성
button = tk.Button(root, text = 'Push!', command = func)

# 버튼 배치
button.pack()

# root 표시
print("Ready to application")
root.mainloop()
print("Finished app")
