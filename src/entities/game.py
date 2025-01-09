import tkinter as tk
from .dataclass import HIKAKIN, KAKIN, FIELD
import random
from time import time
from pprint import pprint
from typing import Callable
import copy


class Game:
    # rows,cols=22,12 # <-20*10
    def __init__(
        self, mode: int, time: int = 1000, rows: int = 23, cols: int = 12
    ) -> None:
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
        self.string: str = random.choice(list(self.mode.Tetromino.keys()))
        # self.string:str="I"
        self.tetromino = copy.deepcopy(self.mode.Tetromino[self.string])
        self.root: tk.Tk = tk.Tk()
        self.root.title("Tetris")
        self.root.geometry("500x500")
        # self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.focus_force()
        self.root.bind("<Down>", self.down)
        self.root.bind("<Right>", self.right)
        self.root.bind("<Left>", self.left)
        self.root.bind("<Up>", self.fall_all)
        self.root.bind("<KeyPress>", self.spin)
        self.fall()
        self.root.mainloop()
        # データクラスの書き換え

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
        self.is_falled = self.MAP.down(self.tetromino, self.string)
        self.last_key_time = time()
        print("↓")

    @update
    def right(self, event) -> None:
        if time() - self.last_key_time < self.min_interval:
            return
        self.MAP.right(self.tetromino, self.string)
        print("→")

    @update
    def left(self, event) -> None:
        if time() - self.last_key_time < self.min_interval:
            return
        self.MAP.left(self.tetromino, self.string)
        print("←")

    @update
    def fall(self) -> None:
        if self.is_falled == True:
            self.prev_string = self.string
            self.string: str = random.choice(list(self.mode.Tetromino.keys()))
            while self.prev_string == self.string:
                self.string: str = random.choice(list(self.mode.Tetromino.keys()))
            # self.string:str="I"
            self.tetromino = copy.deepcopy(self.mode.Tetromino[self.string])
            self.is_falled = False

        self.is_falled = self.MAP.down(self.tetromino, self.string)
        self.root.after(self.time, self.fall)

        # print(self.MAP.map)

    @update
    def fall_all(self, event) -> None:
        self.MAP.fall_all(self.tetromino, self.string)
        print("↑")
        self.prev_string = self.string
        self.string: str = random.choice(list(self.mode.Tetromino.keys()))
        while self.prev_string == self.string:
            self.string: str = random.choice(list(self.mode.Tetromino.keys()))
        # self.string:str="I"
        self.tetromino = copy.deepcopy(self.mode.Tetromino[self.string])
        self.is_falled = False

    @update
    def spin(self, event) -> None:
        if time() - self.last_key_time < self.min_interval:
            return
        if event.keysym == "c":
            self.MAP.R_spin(self.tetromino, self.string)
        elif event.keysym == "z":
            self.MAP.L_spin(self.tetromino, self.string)
        print("spin")


if __name__ == "__main__":
    # import ctypes
    # import utils.setting_enviroments as env
    # env.init()
    # ctypes.windll.shcore.SetProcessDpiAwareness(1)
    # game=Game(0)
    # games=Game(1)
    pass
