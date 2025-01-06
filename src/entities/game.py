import tkinter as tk

class Game:
    def __init__(self) -> None:
        pass

if __name__=="__main__":
    import ctypes
    import utils.setting_enviroments as env
    env.init()
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    pass
