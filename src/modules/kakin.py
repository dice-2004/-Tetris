import tkinter as tk

class Kakin:
    def __init__(self) -> None:
        pass


if __name__=="__main__":
    import ctypes
    import modules.setting_enviroments as env
    env.init()
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    pass
