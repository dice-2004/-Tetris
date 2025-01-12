from tkinter import ttk
import tkinter as tk
from typing import Literal

class Setting:
    def __init__(self, fall_interval: float, rows: int, cols: int) -> None:
        self.root: tk.Tk = tk.Tk()
        self.root.title("Setting")
        self.root.geometry("500x500")
        self.root.focus_force()
        self.fall_interval: float = fall_interval
        self.rows: int = rows
        self.cols: int = cols
        self.side:int = 0

        self.note = ttk.Notebook(self.root)
        f_interval = ttk.Frame(self.root)
        f_rows = ttk.Frame(self.root)
        f_cols = ttk.Frame(self.root)


        setting1 = tk.Label(f_interval, text="fall_interval")
        setting1.pack()
        self.fall_interval_var = tk.StringVar(value=str(self.fall_interval))
        self.spinbox1 = tk.Spinbox(f_interval, from_=0, to=10, increment=0.1, textvariable=self.fall_interval_var)
        self.spinbox1.pack()

        setting2 = tk.Label(f_rows, text="rows")
        setting2.pack()
        self.rows_var = tk.StringVar(value=str(self.rows))
        self.spinbox2 = tk.Spinbox(f_rows, from_=5, to=100, increment=1, textvariable=self.rows_var)
        self.spinbox2.pack()

        setting3 = tk.Label(f_cols, text="cols")
        setting3.pack()
        self.cols_var = tk.StringVar(value=str(self.cols))
        self.spinbox3 = tk.Spinbox(f_cols, from_=5, to=100, increment=1, textvariable=self.cols_var)
        self.spinbox3.pack()

        self.note.add(f_interval, text="fall interval")
        self.note.add(f_rows, text="rows")
        self.note.add(f_cols, text="cols")
        self.note.pack()
        Label = tk.Label(self.root, text="Press Enter to start")
        Label.pack()

        self.root.bind("<Return>", self.end)
        self.root.bind("<Up>", self.upper)
        self.root.bind("<Down>", self.lower)
        self.root.bind("<Left>", self.left)
        self.root.bind("<Right>", self.right)

        self.root.mainloop()

    def end(self,event):
        self.fall_interval = self.spinbox1.get()
        self.rows = self.spinbox2.get()
        self.cols = self.spinbox3.get()
        print(self.fall_interval,self.rows,self.cols)
        self.root.destroy()

    def upper(self,event):
        if self.side == 0:
            if float(self.spinbox1.get()) >= 10:
                return
            self.fall_interval = round(float(self.spinbox1.get())+0.1,1)
            self.spinbox1.delete(0, tk.END)
            self.spinbox1.insert(0, str(self.fall_interval))
        elif self.side == 1:
            if float(self.spinbox2.get()) >= 100:
                return
            self.rows  = int(float(self.spinbox2.get())+1)
            self.spinbox2.delete(0, tk.END)
            self.spinbox2.insert(0, str(self.rows))
        elif self.side == 2:
            if float(self.spinbox3.get()) >= 100:
                return
            self.cols = int(float(self.spinbox3.get())+1)
            self.spinbox3.delete(0, tk.END)
            self.spinbox3.insert(0, str(self.cols))

    def lower(self,event):
        if self.side == 0:
            if float(self.spinbox1.get()) <= 0.1:
                return
            self.fall_interval = round(float(self.spinbox1.get())-0.1,1)
            self.spinbox1.delete(0, tk.END)
            self.spinbox1.insert(0, str(self.fall_interval))
        elif self.side == 1:
            if float(self.spinbox2.get()) <= 5:
                return
            self.rows  = int(float(self.spinbox2.get())-1)
            self.spinbox2.delete(0, tk.END)
            self.spinbox2.insert(0, str(self.rows))
        elif self.side == 2:
            if float(self.spinbox3.get()) <= 5:
                return
            self.cols = int(float(self.spinbox3.get())-1)
            self.spinbox3.delete(0, tk.END)
            self.spinbox3.insert(0, str(self.cols))

    def left(self,event):
        print(self.side)
        self.current_tab()
        if self.side <= 0:
            return
        self.side -= 1
        self.note.select(self.side)
        return

    def right(self,event):
        print(self.side)
        self.current_tab()
        if self.side >= 2:
            return
        self.side += 1
        self.note.select(self.side)
        return

    def current_tab(self):
        current_tab = self.note.select()
        current_tab_index = self.note.index(current_tab)
        current_tab_label = self.note.tab(current_tab_index, "text")
        if current_tab_label == "fall_interval":
            self.side = 0
        elif current_tab_label == "rows":
            self.side = 1
        elif current_tab_label == "cols":
            self.side = 2
