import tkinter as tk
from .dataclass import HIKAKIN, KAKIN, FIELD
import random
from time import time
from pprint import pprint
from typing import Callable
import copy


class Game:
    # rows,cols=22,12 # <-20*10
    def __init__(self, mode: int, time: int = 1000, rows: int = 23, cols: int = 12) -> None:
        self.default_time = time
        self.time = time
        if mode == 0:
            self.mode = KAKIN.Kakin({"x": int(cols / 2), "y": 0})
        elif mode == 1:
            self.mode = HIKAKIN.hikakin({"x": int(cols / 2), "y": 0})
        self.MAP: FIELD.Field = FIELD.Field(rows, cols)
        pprint(self.MAP.map)

        with open("src/entities/dataclass/map.txt", "w") as f:
            for row in self.MAP.map:
                f.write(" ".join(map(str, row)) + "\n")

        self.last_key_time: float = 0  # (s)
        self.min_interval: float = 0.22  # (s)
        self.is_falled: bool = False
        self.game_over_flag: bool = False
        self.string: str = random.choice(list(self.mode.Tetromino.keys()))
        self.next_string: str = random.choice(list(self.mode.Tetromino.keys()))
        self.paused: bool = False
        # self.string:str="I"
        self.tetromino = copy.deepcopy(self.mode.Tetromino[self.string])
        self.root: tk.Tk = tk.Tk()
        self.root.title("Tetris")
        self.root.geometry("500x500")
        # self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.focus_force()
        self.bind_keys()

        self.fall()
        self.game_over_observer()
        self.root.mainloop()
        # データクラスの書き換え

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

        return wapper

    @update
    def down(self, event) -> None:
        if self.is_falled == True:
            return
        if time() - self.last_key_time < self.min_interval:
            return
        self.is_falled = self.MAP.down(self.tetromino["tetro"], self.string, self.tetromino["shaft"])
        self.last_key_time = time()
        print("↓")

    @update
    def right(self, event) -> None:
        if time() - self.last_key_time < self.min_interval:
            return
        self.MAP.right(self.tetromino["tetro"], self.string,self.tetromino["shaft"])
        print("→")
        print(self.tetromino["shaft"])

    @update
    def left(self, event) -> None:
        if time() - self.last_key_time < self.min_interval:
            return
        self.MAP.left(self.tetromino["tetro"], self.string,self.tetromino["shaft"])
        self.tetromino["shaft"][0] -= 1
        print("←")
        print(self.tetromino["shaft"])

    @update
    def fall(self) -> None:
        if self.game_over_flag:
            return
        elif self.is_falled == True:
            self.prev_string = self.string
            self.string = self.next_string
            self.next_string: str = random.choice(list(self.mode.Tetromino.keys()))
            while self.prev_string == self.string:
                self.next_string: str = random.choice(list(self.mode.Tetromino.keys()))
            # self.string:str="I"
            self.tetromino = copy.deepcopy(self.mode.Tetromino[self.string])
            self.is_falled = False
            self.time = self.default_time

        self.is_falled = self.MAP.down(self.tetromino["tetro"], self.string, self.tetromino["shaft"])
        self.fall_id =self.root.after(self.time, self.fall)

        # print(self.MAP.map)

    @update
    def fall_all(self, event) -> None:
        self.time = 10

    @update
    def spin(self, event) -> None:
        if time() - self.last_key_time < self.min_interval or self.string == "O":
            return
        if event.keysym == "c":
            self.MAP.R_spin(self.tetromino, self.string)
        elif event.keysym == "z":
            self.MAP.L_spin(self.tetromino, self.string)
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
