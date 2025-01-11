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

        self.score_label = tk.Label(self.root, text="Score: 0", font=('Arial', 14))
        self.score_label.pack(pady=5)
        self.level_label = tk.Label(self.root, text="Level: 1", font=('Arial', 14))
        self.level_label.pack(pady=5)

        self.update_score_display()

        self.fall()
        self.game_over_observer()
        self.root.mainloop()
        # データクラスの書き換え

    def update_score_display(self) -> None:
        """スコアとレベルの表示を更新"""
        try:
            self.score_label.config(text=f"Score: {self.MAP.score}")
            self.level_label.config(text=f"Level: {self.MAP.level}")
            
            # 落下速度をレベルに応じて調整（最小100ms）
            self.default_time = max(100, 1000 - (self.MAP.level - 1) * 50)
            
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

        return wapper

    @update
    def down(self, event) -> None:
        if self.is_falled == True:
            return
        if time() - self.last_key_time < self.min_interval:
            return
        self.is_falled = self.MAP.down(self.tetromino["tetro"], self.string)
        self.last_key_time = time()
        self.tetromino["shaft"][1] += 1
        print("↓")

    @update
    def right(self, event) -> None:
        if time() - self.last_key_time < self.min_interval:
            return
        self.MAP.right(self.tetromino["tetro"], self.string)
        self.tetromino["shaft"][0] += 1
        print("→")

    @update
    def left(self, event) -> None:
        if time() - self.last_key_time < self.min_interval:
            return
        self.MAP.left(self.tetromino["tetro"], self.string)
        self.tetromino["shaft"][0] -= 1
        print("←")

    @update
    def fall(self) -> None:
        if self.game_over_flag:
            return
        elif self.is_falled == True:
            self.prev_string = self.string
            self.string: str = random.choice(list(self.mode.Tetromino.keys()))
            while self.prev_string == self.string:
                self.string: str = random.choice(list(self.mode.Tetromino.keys()))
            # self.string:str="I"
            self.tetromino = copy.deepcopy(self.mode.Tetromino[self.string])
            self.is_falled = False
            self.time = self.default_time

        self.is_falled = self.MAP.down(self.tetromino["tetro"], self.string)
        self.root.after(self.time, self.fall)
        self.tetromino["shaft"][1] += 1

        # print(self.MAP.map)

    @update
    def fall_all(self, event) -> None:
        self.time = 10

    @update
    def spin(self, event) -> None:
        if time() - self.last_key_time < self.min_interval:
            return
        if event.keysym == "c":
            self.MAP.R_spin(self.tetromino, self.string)
        elif event.keysym == "z":
            self.MAP.L_spin(self.tetromino, self.string)
        print("spin")

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
