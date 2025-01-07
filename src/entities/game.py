import tkinter as tk
from .dataclass import default, kakin,field
import random
from pprint import pprint
from time import sleep

class Game:
    def __init__(self,mode:int) -> None:
        self.mode:int = mode
        if self.mode == 0:
            self.tetromino = kakin.Kakin().Tetromino
        elif self.mode == 1:
            self.tetromino = default.Defalut().Tetromino
        self.root = tk.Tk()
        self.MAP:field.Field = field.Field()

        with open("src/entities/dataclass/map.txt","w") as f:
            for row in self.MAP.map:
                f.write(" ".join(map(str, row)) + "\n")

        # データクラスの書き換え

    def fall(self) -> None:
        border_y:int = 0
        border_x:int = 0
        string:str=random.choice(list(self.tetromino.keys()))
        # while True:
        #     self.MAP.down(self.tetromino[string],border_y)
        #     border_y+=1
        #     with open("src/entities/dataclass/map.txt","w") as f:
        #         for row in self.MAP.map:
        #             f.write(" ".join(map(str, row)) + "\n")
        #     sleep(1)
        while True:
            border_x=self.MAP.right(self.tetromino[string],border_x)

            with open("src/entities/dataclass/map.txt","w") as f:
                for row in self.MAP.map:
                    f.write(" ".join(map(str, row)) + "\n")
            sleep(1)

        # print(self.MAP.map)


if __name__=="__main__":
    # import ctypes
    # import utils.setting_enviroments as env
    # env.init()
    # ctypes.windll.shcore.SetProcessDpiAwareness(1)
    # game=Game(0)
    # games=Game(1)
    pass
