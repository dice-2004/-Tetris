import tkinter as tk
from tkinter import ttk
import time
import os

iconfile = "src/assets/icons/kawasaki.ico"

class Setting:
    def __init__(self, fall_interval: float, rows: int, cols: int) -> None:
        self.root = tk.Tk()
        self.root.title("Setting")
        self.root.geometry("400x300")
        self.root.focus_force()
        
        if os.path.exists(iconfile):
            self.root.iconbitmap(iconfile)
        else:
            print(f"Icon file '{iconfile}' not found. Using default icon.")

        self.fall_interval = fall_interval
        self.rows = rows
        self.cols = cols
        self.side = 0
        self.last_change_time = 0

        # スタイルの設定
        style = ttk.Style()
        style.configure('TNotebook', background='#f0f0f0')
        style.configure('TNotebook.Tab', font=('Arial', 12), padding=[10, 5])
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TLabel', background='#f0f0f0', font=('Arial', 12))
        style.configure('TSpinbox', font=('Arial', 12), padding=[5, 5])

        self.note = ttk.Notebook(self.root, style='TNotebook')
        self.f_interval = ttk.Frame(self.note, style='TFrame')
        self.f_rows = ttk.Frame(self.note, style='TFrame')
        self.f_cols = ttk.Frame(self.note, style='TFrame')

        self.note.add(self.f_interval, text="Fall Interval")
        self.note.add(self.f_rows, text="Rows")
        self.note.add(self.f_cols, text="Cols")
        self.note.pack(expand=True, fill='both')

        self.create_widgets()

        self.error_label = None  # エラーメッセージ用のラベルを初期化

        self.root.bind("<Return>", self.end)
        self.root.bind("<Left>", self.left)
        self.root.bind("<Right>", self.right)

        self.root.mainloop()

    def create_widgets(self):
        # Fall Interval Tab
        setting1 = ttk.Label(self.f_interval, text="Fall Interval:", style='TLabel')
        setting1.pack(pady=10)
        self.fall_interval_var = tk.StringVar(value=str(self.fall_interval))
        self.spinbox1 = ttk.Spinbox(self.f_interval, from_=0, to=10, increment=0.1, textvariable=self.fall_interval_var, validate='key', validatecommand=(self.root.register(self.validate_float), '%P'), style='TSpinbox')
        self.spinbox1.pack(pady=5)

        # Rows Tab
        setting2 = ttk.Label(self.f_rows, text="Rows:", style='TLabel')
        setting2.pack(pady=10)
        self.rows_var = tk.StringVar(value=str(self.rows))
        self.spinbox2 = ttk.Spinbox(self.f_rows, from_=5, to=100, increment=1, textvariable=self.rows_var, validate='key', validatecommand=(self.root.register(self.validate_int), '%P'), style='TSpinbox')
        self.spinbox2.pack(pady=5)

        # Cols Tab
        setting3 = ttk.Label(self.f_cols, text="Cols:", style='TLabel')
        setting3.pack(pady=10)
        self.cols_var = tk.StringVar(value=str(self.cols))
        self.spinbox3 = ttk.Spinbox(self.f_cols, from_=5, to=100, increment=1, textvariable=self.cols_var, validate='key', validatecommand=(self.root.register(self.validate_int), '%P'), style='TSpinbox')
        self.spinbox3.pack(pady=5)

        # Instruction Label
        instruction_label = ttk.Label(self.root, text="Press Enter to change the setting", font=("Arial", 10), background='#f0f0f0')
        instruction_label.pack(pady=10)

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
            self.show_error("Please enter a valid number")
            return

        print(type(self.fall_interval), type(self.rows), type(self.cols))
        self.root.destroy()

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
        self.error_label = ttk.Label(self.root, text=message, foreground="red", font=("Arial", 10))
        self.error_label.pack(pady=5)

# インスタンスを作成してアプリケーションを実行
if __name__ == "__main__":
    app = Setting(1.0, 20, 10)
