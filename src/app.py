##########################################################################################################################
#########################################ここは変えるな 変えたら殺#########################################################
##########################################################################################################################
import tkinter as tk
import ctypes
import tkinter.messagebox as messagebox
from typing import List, Any,Dict
from time import sleep

from utils import setting_enviroments as env
from entities.top import Top_page
from entities import game

# 初期化処理
value:int = env.init()
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# スタートメニュー
while value == 2:
    top:Top_page = Top_page("Start Menu",600,500,0,0)
    # value -> 0:課金, 1:Gama Start, 2:Setting, 3:Exit
    value:int=top.get_select_value()
    print(value)

# Valueによって処理を分岐すればいい

##########################################################################################################################
#########################################ここは変えるな 変えたら殺#########################################################
##########################################################################################################################
# ￥10,000,000,000
#              ￥0
    if value == 0:
        while True:
            if messagebox.askyesno("警告", "￥0\n残高がありません\n追加しますか？"):
                messagebox.showinfo("警告", "￥10,000,000,000\n追加しました")
                messagebox.showwarning("警告", "￥10,000,000,000\n支払いが完了しました")
                break
            else:
                pass
        GAME:game.Game=game.Game(value)
        # entities/Tetromino/kakin.py
        # entities/game.py
    elif value == 1:
        GAME:game.Game=game.Game(value)
        # entities/Tetromino/defalut.py
        # entities/game.py

        GAME.fall()
        pass
    elif value == 2:
        # entities/setting.py
        print("Setting")
        pass
    elif value == 3:
        # 終了
        exit()


# Tkinterを使用してウィンドウを作成
root:tk.Tk = tk.Tk()
root.title("Hello, Tkinter!")
root.focus_force()
label:tk.Label = tk.Label(root, text="Hello, World!")
label.pack()
root.mainloop()

# ゲーム画面
