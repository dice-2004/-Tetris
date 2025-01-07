import tkinter as tk
from .dataclass import default, kakin,field
import random
from pprint import pprint

class Game:
    def __init__(self,mode:int) -> None:
        if mode == 0:
            self.tetromino = kakin.Kakin().Tetromino
        elif mode == 1:
            self.tetromino = default.Defalut().Tetromino
        self.root = tk.Tk()
        self.MAP:field.Field = field.Field()
        
        with open("src/entities/dataclass/map.txt","w") as f:
            for row in self.MAP.map:
                f.write(" ".join(map(str, row)) + "\n")

        # データクラスの書き換え

    def fall(self) -> None:
        string:str=random.choice(list(self.tetromino.keys()))
        for block in self.tetromino[string]:
            print(block)
        #     self.MAP.down(block)
        # print(self.MAP.map)


if __name__=="__main__":
    # import ctypes
    # import utils.setting_enviroments as env
    # env.init()
    # ctypes.windll.shcore.SetProcessDpiAwareness(1)
    # game=Game(0)
    # games=Game(1)
    pass
