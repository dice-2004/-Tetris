##########################################################################################################################
#########################################ここは変えるな 変えたら殺#########################################################
##########################################################################################################################
import tkinter as tk
import ctypes

import utils.setting_enviroments as env
from entities.top import Top_page

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


    if value == 0:
        # entities/Tetromino/kakin.py
        # entities/game.py
        pass
    elif value == 1:
        # entities/Tetromino/defalut.py
        # entities/game.py
        pass
    elif value == 2:
        # entities/setting.py
        print("Setting")
        pass
    elif value == 3:
        # 終了
        exit()


# Tkinterを使用してウィンドウを作成
root:tk.TK = tk.Tk()
root.title("Hello, Tkinter!")
label:tk.Label = tk.Label(root, text="Hello, World!")
label.pack()
root.mainloop()

# ゲーム画面
