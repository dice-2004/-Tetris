import tkinter as tk
from tkinter import PhotoImage
from .dataclass import HIKAKIN, KAKIN, FIELD
import random
from time import time
from pprint import pprint
from typing import Callable,List
import copy
from time import sleep
from typing import Dict, Optional
import os


class Game:
    # rows,cols=22,12 # <-20*10
    def __init__(self, mode: int, time: int = 2000, rows: int = 23, cols: int = 12) -> None:

        self.default_time = time
        self.time = time
        if mode == 2:
            self.mode = KAKIN.Kakin({"x": int(cols / 2), "y": 0})
        elif mode == 0:
            self.mode = HIKAKIN.hikakin({"x": int(cols / 2), "y": 0})
        self.MAP: FIELD.Field = FIELD.Field(rows, cols)
        pprint(self.MAP.map)

        print(type(self.MAP.map[1][1]))

        # 画像パスの設定
        self.IMAGE_FILEPATH = [
            os.path.abspath("src/assets/images/Wall_and_Bottom(kari).png"),
            os.path.abspath("src/assets/images/empty_block.png"),
            os.path.abspath("src/assets/images/blue_block.png"),
            os.path.abspath("src/assets/images/green_block.png"),
            os.path.abspath("src/assets/images/orange_block.png"),
            os.path.abspath("src/assets/images/pink_block.png"),
            os.path.abspath("src/assets/images/purple_block.png"),
            os.path.abspath("src/assets/images/red_block.png"),
            os.path.abspath("src/assets/images/yellow_block.png"),
            os.path.abspath("src/assets/images/navi_block.png")
        ]

        with open("src/entities/dataclass/map.txt", "w") as f:
            for row in self.MAP.map:
                f.write(" ".join(map(str, row)) + "\n")
        self.last_key_time: float = 0  # (s)
        self.min_interval: float = 0.22  # (s)
        self.is_falled: bool = False
        self.game_over_flag: bool = False
        self.strings: List[str] = []
        self.gen_string()
        print(self.strings)

        self.paused: bool = False
        # self.string:str="I"
        self.tetromino = copy.deepcopy(self.mode.Tetromino[self.strings[0]])
        self.root: tk.Tk = tk.Tk()
        self.root.title("Tetris")
        self.root.geometry("500x600")
        self.labels: List[tk.Label] = []
        # self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.focus_force()
        self.bind_keys()

        # 画像の読み込みと保存
        self.images: Dict[int, PhotoImage] = {}
        self.load_images()

        self.score_label = tk.Label(self.root, text="Score: 0", font=('Arial', 14))
        self.score_label.place(x=cols * 25, y=100)
        self.level_label = tk.Label(self.root, text="Level: 1", font=('Arial', 14))
        self.level_label.place(x=cols * 25, y=200)

        self.update_score_display()

        self.fall()
        self.game_over_observer()
        self.root.mainloop()
        # データクラスの書き換え

    def load_images(self) -> None:
        """ブロック画像の読み込み"""
        for i, path in enumerate(self.IMAGE_FILEPATH):
            try:
                self.images[i] = PhotoImage(file=path)
            except Exception as e:
                print(f"Error loading image {path}: {e}")
                self.images[i] = None

    def bind_keys(self):
        self.root.bind("<Down>", self.down)
        self.root.bind("<Right>", self.right)
        self.root.bind("<Left>", self.left)
        self.root.bind("<Up>", self.fall_all)
        self.root.bind("<KeyPress>", self.spin)
        self.root.bind("<KeyPress-d>", self.pause)
        self.root.bind("<KeyPress-D>", self.pause)
        self.root.bind("<Escape>", self.exit)

    def unbind_keys(self):
        self.root.unbind("<Down>")
        self.root.unbind("<Right>")
        self.root.unbind("<Left>")
        self.root.unbind("<Up>")
        self.root.unbind("<KeyPress>")

    def update_score_display(self) -> None:
        """スコアとレベルの表示を更新"""
        try:
            self.score_label.config(text=f"Score: {self.MAP.score}")
            self.level_label.config(text=f"Level: {self.MAP.level}")
            
            # 落下速度をレベルに応じて調整（最小100ms）
            # self.default_time = max(100, 1000 - (self.MAP.level - 1) * 50)
            
            if not self.game_over_flag:
                self.root.after(100, self.update_score_display)
        except Exception as e:
            print(f"Error updating score display: {e}")

    def update(func: Callable) -> Callable:
        def wapper(self, event=None) -> None:
            if event is not None:
                func(self, event)
            else:
                func(self)
            # print("update")
            with open("src/entities/dataclass/map.txt", "w") as f:
                for row in self.MAP.map:
                    f.write(" ".join(f"{cell:2}" for cell in row) + "\n")
            self.draw_block()

        return wapper

    def draw_block(self) -> None:
        """マップデータに基づいてブロックを描画"""
        for label in self.labels:
            label.destroy()  # 古いラベルを削除
        self.labels.clear()

        for y, row in enumerate(self.MAP.map):
            for x, cell in enumerate(row):
                image = self.match_block(cell)
                # print(cell, end=" ")
                if image is not None:
                    label = tk.Label(self.root, image=image)
                    label.place(x=x * 25, y=y * 25)  # 適切な位置に配置
                    self.labels.append(label)

#  0=Enpty 1=active_I   2=active_O   3=active_S   4=active_Z   5=active_J   6=active_L   7=active_T
# 10=wall 11=stacked_I 12=stacked_O 13=stacked_S 14=stacked_Z 15=stacked_J 16=stacked_L 17=stacked_T
    def match_block(self, cell:int) -> PhotoImage:
        # print(type(cell))
        match cell:
            case 10 | 20 | 30:
                return self.images[0]
            case 0:
                # print("empty")
                return self.images[1]
            case 1 | 11:
                # print("blue")
                return self.images[2]
            case 2 | 12:
                # print("yellow")
                return self.images[8]
            case 3 | 13:
                # print("a")
                return self.images[3]
            case 4 | 14:
                # print("b")
                return self.images[7]
            case 5 | 15:
                # print("c")
                return self.images[6]
            case 6 | 16:
                # print("d")
                return self.images[4]
            case 7 | 17:
                # print("e")
                return self.images[5]
            case _:
                # print("mattai")
                return None

    @update
    def down(self, event) -> None:
        if self.is_falled == True:
            return
        if time() - self.last_key_time < self.min_interval:
            return
        self.is_falled = self.MAP.down(self.tetromino["tetro"], self.strings[0])
        self.last_key_time = time()
        print("↓")

    @update
    def right(self, event) -> None:
        if time() - self.last_key_time < self.min_interval:
            return
        self.MAP.right(self.tetromino["tetro"], self.strings[0])
        print("→")
        self.last_key_time = time()
        print(self.tetromino["shaft"])

    @update
    def left(self, event) -> None:
        if time() - self.last_key_time < self.min_interval:
            return
        self.MAP.left(self.tetromino["tetro"], self.strings[0])
        print("←")
        self.last_key_time = time()
        print(self.tetromino["shaft"])

    @update
    def fall(self) -> None:
        if self.game_over_flag:
            return
        elif self.is_falled == True:
            self.unbind_keys()
            self.strings.pop(0)
            G_string = random.choice(list(self.mode.Tetromino.keys()))
            count:int = 0
            while G_string == self.strings[-2]:
                G_string = random.choice(list(self.mode.Tetromino.keys()))
                count += 1
                if count > 30:
                    break

            self.strings.append(G_string)
            self.tetromino = copy.deepcopy(self.mode.Tetromino[self.strings[0]])
            print(self.strings)
            self.bind_keys()

            self.is_falled = False
            self.time = self.default_time

        self.unbind_keys()
        self.is_falled = self.MAP.down(self.tetromino["tetro"], self.strings[0])
        self.bind_keys()

        self.fall_id =self.root.after(self.time, self.fall)
        if self.is_falled:
            sleep(0.1)
            self.unbind_keys()


        # print(self.MAP.map)

    @update
    def fall_all(self, event) -> None:
        self.time = 10

    @update
    def spin(self, event) -> None:
        if time() - self.last_key_time < self.min_interval or self.strings[0] == "O":
            return
        if event.keysym == "c":
            self.MAP.R_spin(self.tetromino, self.strings[0])
        elif event.keysym == "z":
            self.MAP.L_spin(self.tetromino, self.strings[0])
        self.last_key_time = time()
        print("spin")

    def pause(self, event =None) -> None:
        if not self.paused:
            self.paused = True
            self.root.after_cancel(self.fall_id)
            self.unbind_keys()
            print("Paused")
        else:
            self.paused = False
            self.fall_id = self.root.after(self.time, self.fall)
            self.bind_keys()
            print("Resumed")

    def exit(self, event=None):
        self.root.after_cancel(self.fall_id)
        self.root.destroy()

    def gen_string(self) -> None:
        self.strings.append(random.choice(list(self.mode.Tetromino.keys())))
        for i in range(1,4):
            string = random.choice(list(self.mode.Tetromino.keys()))
            count:int = 0
            while self.strings[i-1] == string:
                string= random.choice(list(self.mode.Tetromino.keys()))
                count+=1
                if count > 30:
                    break
            self.strings.append(string)


    def game_over_observer(self) -> None:
        if self.MAP.is_game_over():
            print("Game Over")

            self.root.destroy()
            self.game_over_flag: bool = True
            return
        self.root.after(1, self.game_over_observer)

if __name__ == "__main__":
    # import ctypes
    # import utils.setting_enviroments as env
    # env.init()
    # ctypes.windll.shcore.SetProcessDpiAwareness(1)
    # game=Game(0)
    # games=Game(1)
    pass
