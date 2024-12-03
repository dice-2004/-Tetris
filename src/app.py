import os
import tkinter as tk

# 現在のユーザー名を取得
user_name = os.getlogin()

# 環境変数を設定
os.environ['TCL_LIBRARY'] = fr'C:\Users\{user_name}\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'

# Tkinterを使用してウィンドウを作成
root = tk.Tk()
root.title("Hello, Tkinter!")
label = tk.Label(root, text="Hello, World!")
label.pack()
root.mainloop()
