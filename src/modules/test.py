# import tkinter as tk
# import setting_enviroments as env
# env.init()

# def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
#     """角丸の長方形を描画する関数"""
#     points = [
#         x1+radius, y1, x1+radius, y1,
#         x2-radius, y1, x2-radius, y1,
#         x2, y1, x2, y1+radius,
#         x2, y2-radius, x2, y2-radius,
#         x2, y2, x2-radius, y2,
#         x1+radius, y2, x1+radius, y2,
#         x1, y2, x1, y2-radius,
#         x1, y1+radius, x1, y1+radius,
#         x1, y1
#     ]
#     return canvas.create_polygon(points, **kwargs, smooth=True)

# root = tk.Tk()
# root.geometry("300x200")
# root.title("Rounded Label")

# canvas = tk.Canvas(root, width=300, height=200, bg="white", highlightthickness=0)
# canvas.pack(fill="both", expand=True)

# # 角丸の背景を描画
# create_rounded_rectangle(canvas, 50, 50, 250, 100, radius=20, fill="lightblue", outline="blue")

# # ラベルテキストを表示
# # canvas.create_text(150, 75, text="Rounded Label", font=("Arial", 16), fill="black")

# root.mainloop()
import tkinter as tk
import setting_enviroments as env
class MenuDrawer:
    def __init__(self, root, menu):
        self.root = root
        self.menu = menu
        self.labels = []  # ラベルのリスト
        self.canvas = tk.Canvas(root, bg="white", highlightthickness=0)  # Canvasの作成
        self.canvas.pack(fill="both", expand=True)

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        """角丸の長方形をCanvasに描画する関数"""
        points = [
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

    def draw_menu(self) -> None:
        for i in range(len(self.menu)):
            x, y = 500, 0  # 初期座標
            if i == 0:
                # 1つ目のラベルの位置とサイズ
                x = 500
                y = 0
                width = 120
                height = 50
                font_size = 10
                radius = 15
            else:
                # 2つ目以降のラベルの位置とサイズ
                x = -50 + 100 * i
                y = 130 + 80 * i
                width = 200
                height = 60
                font_size = 20
                radius = 25

            # 角丸の長方形を描画
            self.create_rounded_rectangle(x, y, x+width, y+height, radius=radius, fill=self.menu[i]["color"])

            # テキストを配置
            text_x = x + width // 2
            text_y = y + height // 2
            self.canvas.create_text(
                text_x,
                text_y,
                text=self.menu[i]["text"],
                font=("Helvetica", font_size),
                fill="black"
            )

# アプリケーションの設定
env.init()
root = tk.Tk()
root.geometry("800x600")

menu = [
    {"text": "Menu 1", "color": "lightblue"},
    {"text": "Menu 2", "color": "lightgreen"},
    {"text": "Menu 3", "color": "lightpink"},
    {"text": "Menu 4", "color": "lightyellow"},
]

app = MenuDrawer(root, menu)
app.draw_menu()

root.mainloop()
