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
        self.MAP:field.Field = field.Field()

        with open("src/entities/dataclass/map.txt","w") as f:
            for row in self.MAP.map:
                f.write(" ".join(map(str, row)) + "\n")

        self.border_x:int = 0
        self.border_y:int = 0

        self.root:tk.Tk = tk.Tk()
        self.root.title("Tetris")
        self.root.geometry("500x500")
        # self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.focus_force()
        self.root.bind("<Down>", self.down)
        self.root.bind("<Right>", self.right)
        self.root.bind("<Left>", self.left)
        self.root.mainloop()
        # データクラスの書き換え
    def down(self,event) -> None:
        self.border_y=self.MAP.down(self.tetromino["L"],self.border_x,self.border_y)
        with open("src/entities/dataclass/map.txt","w") as f:
            for row in self.MAP.map:
                f.write(" ".join(map(str, row)) + "\n")

    def right(self,event) -> None:
        self.border_x=self.MAP.right(self.tetromino["L"],self.border_x,self.border_y)
        with open("src/entities/dataclass/map.txt","w") as f:
            for row in self.MAP.map:
                f.write(" ".join(map(str, row)) + "\n")

    def left(self,event) -> None:
        self.border_x=self.MAP.left(self.tetromino["L"],self.border_x,self.border_y)
        with open("src/entities/dataclass/map.txt","w") as f:
            for row in self.MAP.map:
                f.write(" ".join(map(str, row)) + "\n")

    def fall(self) -> None:
        string:str=random.choice(list(self.tetromino.keys()))
        while True:
            self.border_y=self.MAP.down(self.tetromino[string],self.border_y)

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
