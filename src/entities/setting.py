import tkinter as tk
from tkinter import ttk
import time

class Setting:
    def __init__(self, fall_interval: float, rows: int, cols: int) -> None:
        self.root = tk.Tk()
        self.root.title("Setting")
        self.root.geometry("500x500")
        self.root.focus_force()
        self.fall_interval = fall_interval
        self.rows = rows
        self.cols = cols
        self.side = 0
        self.last_change_time = 0

        self.note = ttk.Notebook(self.root)
        self.f_interval = ttk.Frame(self.note)
        self.f_rows = ttk.Frame(self.note)
        self.f_cols = ttk.Frame(self.note)

        self.note.add(self.f_interval, text="Fall Interval")
        self.note.add(self.f_rows, text="Rows")
        self.note.add(self.f_cols, text="Cols")
        self.note.pack(expand=True, fill='both')

        setting1 = tk.Label(self.f_interval, text="fall_interval")
        setting1.pack()
        self.fall_interval_var = tk.StringVar(value=str(self.fall_interval))
        self.spinbox1 = tk.Spinbox(self.f_interval, from_=0, to=10, increment=0.1, textvariable=self.fall_interval_var, validate='key', validatecommand=(self.root.register(self.validate_float), '%P'))
        self.spinbox1.pack()

        setting2 = tk.Label(self.f_rows, text="rows")
        setting2.pack()
        self.rows_var = tk.StringVar(value=str(self.rows))
        self.spinbox2 = tk.Spinbox(self.f_rows, from_=5, to=100, increment=1, textvariable=self.rows_var, validate='key', validatecommand=(self.root.register(self.validate_int), '%P'))
        self.spinbox2.pack()

        setting3 = tk.Label(self.f_cols, text="cols")
        setting3.pack()
        self.cols_var = tk.StringVar(value=str(self.cols))
        self.spinbox3 = tk.Spinbox(self.f_cols, from_=5, to=100, increment=1, textvariable=self.cols_var, validate='key', validatecommand=(self.root.register(self.validate_int), '%P'))
        self.spinbox3.pack()

        self.error_label = None  # エラーメッセージ用のラベルを初期化

        Label = tk.Label(self.root, text="Press Enter to change the setting")
        Label.pack()

        self.root.bind("<Return>", self.end)
        # self.root.bind("<Up>", self.upper)
        # self.root.bind("<Down>", self.lower)
        self.root.bind("<Left>", self.left)
        self.root.bind("<Right>", self.right)

        self.root.mainloop()

    def validate_float(self, value_if_allowed):
        if value_if_allowed == "":
            return True
        try:
            float(value_if_allowed)
            return True
        except ValueError:
            return False

    def validate_int(self, value_if_allowed):
        if value_if_allowed == "":
            return True
        try:
            int(value_if_allowed)
            return True
        except ValueError:
            return False

    def end(self, event) -> None:
        if self.error_label:
            self.error_label.pack_forget()  # 以前のエラーメッセージを削除

        try:
            self.fall_interval = float(self.spinbox1.get())
            self.rows = int(self.spinbox2.get())
            self.cols = int(self.spinbox3.get())
        except ValueError:
            print("error")
            self.error_label = tk.Label(self.root, text="Please enter a valid number")
            self.error_label.pack()
            return

        print(type(self.fall_interval), type(self.rows), type(self.cols))
        self.root.destroy()

    # def upper(self, event) -> None:
    #     current_time = time.time()
    #     if current_time - self.last_change_time < 5:  # 1秒以内に再度変更が加えられた場合
    #         return
    #     self.last_change_time = current_time

    #     try:
    #         if self.side == 0:
    #             if float(self.spinbox1.get()) >= 10:
    #                 return
    #             self.fall_interval = round(float(self.spinbox1.get()) + 0.1, 1)
    #             self.spinbox1.config(state='normal')
    #             self.spinbox1.delete(0, tk.END)
    #             self.spinbox1.insert(0, str(self.fall_interval))
    #             self.spinbox1.config(state='readonly')
    #         elif self.side == 1:
    #             if float(self.spinbox2.get()) >= 100:
    #                 return
    #             self.rows = int(float(self.spinbox2.get()) + 1)
    #             self.spinbox2.config(state='normal')
    #             self.spinbox2.delete(0, tk.END)
    #             self.spinbox2.insert(0, str(self.rows))
    #             self.spinbox2.config(state='readonly')
    #         elif self.side == 2:
    #             if float(self.spinbox3.get()) >= 100:
    #                 return
    #             self.cols = int(float(self.spinbox3.get()) + 1)
    #             self.spinbox3.config(state='normal')
    #             self.spinbox3.delete(0, tk.END)
    #             self.spinbox3.insert(0, str(self.cols))
    #             self.spinbox3.config(state='readonly')
    #     except ValueError:
    #         self.show_error("Please enter a valid number")

    # def lower(self, event) -> None:
    #     current_time = time.time()
    #     if current_time - self.last_change_time < 5:  # 1秒以内に再度変更が加えられた場合
    #         return
    #     self.last_change_time = current_time

    #     try:
    #         if self.side == 0:
    #             if float(self.spinbox1.get()) <= 0:
    #                 return
    #             self.fall_interval = round(float(self.spinbox1.get()) - 0.1, 1)
    #             self.spinbox1.config(state='normal')
    #             self.spinbox1.delete(0, tk.END)
    #             self.spinbox1.insert(0, str(self.fall_interval))
    #             self.spinbox1.config(state='readonly')
    #         elif self.side == 1:
    #             if float(self.spinbox2.get()) <= 5:
    #                 return
    #             self.rows = int(float(self.spinbox2.get()) - 1)
    #             self.spinbox2.config(state='normal')
    #             self.spinbox2.delete(0, tk.END)
    #             self.spinbox2.insert(0, str(self.rows))
    #             self.spinbox2.config(state='readonly')
    #         elif self.side == 2:
    #             if float(self.spinbox3.get()) <= 5:
    #                 return
    #             self.cols = int(float(self.spinbox3.get()) - 1)
    #             self.spinbox3.config(state='normal')
    #             self.spinbox3.delete(0, tk.END)
    #             self.spinbox3.insert(0, str(self.cols))
    #             self.spinbox3.config(state='readonly')
    #     except ValueError:
    #         self.show_error("Please enter a valid number")

    def left(self, event) -> None:
        self.current_tab()
        if self.side <= 0:
            return
        self.side -= 1
        self.note.select(self.side)

    def right(self, event) -> None:
        self.current_tab()
        if self.side >= 2:
            return
        self.side += 1
        self.note.select(self.side)

    def current_tab(self) -> None:
        current_tab = self.note.select()
        current_tab_index = self.note.index(current_tab)
        current_tab_label = self.note.tab(current_tab_index, "text")
        if current_tab_label == "Fall Interval":
            self.side = 0
        elif current_tab_label == "Rows":
            self.side = 1
        elif current_tab_label == "Cols":
            self.side = 2

    def show_error(self, message):
        if self.error_label:
            self.error_label.pack_forget()
        self.error_label = tk.Label(self.root, text=message, fg="red")
        self.error_label.pack()

# インスタンスを作成してアプリケーションを実行
if __name__ == "__main__":
    app = Setting(1.0, 20, 10)
