import tkinter as tk
from typing import Dict,List,Any
from typing import Union,Literal
# import time
Num=Union[int,float]

class Top_page:
    def __init__(self, window_title: str,width:int,height:int,x_position:int,y_position:int) -> None:
        self.root:tk.Tk = tk.Tk()
        self.root.title(window_title)
        self.root.geometry(f"{width}x{height}+{x_position}+{y_position}")
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.focus_force()
        # キーイベントのバインディング
        self.root.bind("<Up>", self.up)  # 上矢印キー
        self.root.bind("<Down>", self.down)  # 下矢印キー
        self.root.bind("<Return>", self.enter)  # Enterキー

        self.SECELT:str = "#FF0000"  # red
        self.NOT_SECELT:str = "#0000FF"  # blue
        self.menu:List[Dict[str,Literal["#FF0000", "#0000FF"]]] = [
            {"text": "課金", "color": self.NOT_SECELT},
            {"text": "Start Game", "color": self.SECELT},
            {"text": "Setting", "color": self.NOT_SECELT},
            {"text": "Exit", "color": self.NOT_SECELT},
        ]
        self.select_value:int = 1
        self.labels:Any = []
        # self.Canvases = []
        self.canvas:tk.Canvas = tk.Canvas(self.root, bg="white", highlightthickness=0)  # Canvasの作成
        self.canvas.pack(fill="both", expand=True)
        self.draw_menu()
        self.root.mainloop()

    # メニュー描写
    def draw_menu(self) -> None:
        for i in range(len(self.menu)):
            x, y = 500, 0  # 初期座標
            if i == 0:
                self.label:tk.Label = tk.Label(
                    self.root,
                    text=self.menu[i]["text"],
                    bg=self.menu[i]["color"],
                    font=("Helvetica", 10),
                    bd=8,
                    width=6,
                    height=1,
                )
                self.label.place(x=500 ,y=0)
                self.labels.append(self.label)
            else:
                # 2つ目以降のラベルの位置とサイズ
                x:int = -50 + 100 * i
                y:int = 130 + 80 * i
                width:int = 250
                height:int = 60
                font_size:int = 20
                radius:int = 25
                            # 角丸の長方形を描画
                self.create_rounded_rectangle(x, y, x+width, y+height, radius=radius, fill=self.menu[i]["color"])

                # テキストを配置
                text_x :Num= x + width // 2
                text_y :Num= y + height // 2
                self.canvas.create_text(
                    text_x,
                    text_y,
                    text=self.menu[i]["text"],
                    font=("Helvetica", font_size),
                    fill="black"
                )
                # self.Canvases.append(self.canvas)


    # def draw_menu(self) -> None:
    #     for i in range(len(self.menu)):
    #         if i == 0:
    #             self.canvas = tk.Canvas(
    #                 self.root,
    #                 text=self.menu[i]["text"],
    #                 bg=self.menu[i]["color"],
    #                 font=("Helvetica", 10),
    #                 bd=8,
    #                 width=6,
    #                 height=1,
    #             )
    #             self.label.place(x=500 ,y=0)
    #             self.labels.append(self.label)
    #         else:
    #             self.label = tk.Label(
    #                 self.root,
    #                 text=self.menu[i]["text"],
    #                 bg=self.menu[i]["color"],
    #                 font=("Helvetica", 20),
    #                 bd=10,
    #                 width=10,
    #                 height=1,
    #             )
    #             self.label.place(x=-50+100*i, y=130 + 80 * i)
    #             self.labels.append(self.label)

    # 上キー
    def up(self, event: tk.Event) -> None:
        print("↑")
        if self.select_value > 0:
            int;self.select_value -= 1
        self.change_color()
        self.reset()
        self.draw_menu()

    # 下キー
    def down(self, event: tk.Event) -> None:
        print("↓")
        if self.select_value < 3:
            self.select_value += 1
        self.change_color()
        self.reset()
        self.draw_menu()

    # Enterキー
    def enter(self, event: tk.Event) -> None:
        """Enterキーが押されたときの処理"""
        print("Enterキーが押されました")
        self.reset()
        self.root.destroy()
        return self.select_value

    # 終了
    def exit(self) -> None:
        print("終了します")
        self.select_value:int = 3
        self.root.destroy()

    # リセット
    def reset(self) -> None:
        for label in self.labels:
            label.pack_forget()  # ラベルを非表示にする
        # for canvas in self.Canvases:
        #     canvas.pack_forget()
        self.root.configure(bg="white")  # 背景を白に設定

    # 色変更
    def change_color(self) -> None:
        for i in range(len(self.menu)):
            if i == self.select_value:
                self.menu[i]["color"] = self.SECELT
            else:
                self.menu[i]["color"] = self.NOT_SECELT

    # 選択値取得
    def get_select_value(self) -> int:
        return self.select_value

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        """角丸の長方形を描画する関数"""
        points:Num= [
            x1+radius, y1, x1+radius, y1,
            x2-radius, y1, x2-radius, y1,
            x2, y1, x2, y1+radius,
            x2, y2-radius, x2, y2-radius,
            x2, y2, x2-radius, y2,
            x1+radius, y2, x1+radius, y2,
            x1, y2, x1, y2-radius,
            x1, y1+radius, x1, y1+radius,
            x1, y1
        ]

        return self.canvas.create_polygon(points, **kwargs, smooth=True)


if __name__ == "__main__":
    from ..utils import setting_enviroments as env
    import ctypes
    env.init()
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    # スタートメニュー
    top = Top_page("Start Menu",600,500,0,0)
    value=top.get_select_value()
    print(value)

    # ゲーム画面
    if value != 3:
        root=tk.Tk()
        root.title("Game Play")
        root.geometry("400x300")
        root.mainloop()
