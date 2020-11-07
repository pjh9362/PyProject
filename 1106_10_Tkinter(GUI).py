
# coding: utf-8

import tkinter as tk

# Tk 객체 인스턴스 생성
root = tk.Tk()

# 버튼을 눌렀을 때 처리
def func():
    print("Pushed")

# 버튼 생성
button = tk.Button(root, text = 'Push!', command = func)

# 버튼 배치
button.pack()

# root 표시
print("Ready to application")
root.mainloop()
print("Finished app")
