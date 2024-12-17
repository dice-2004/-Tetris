import tkinter as tk

# import time


class top_page:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        # キーイベントのバインディング
        self.root.bind("<Up>", self.up)  # 上矢印キー
        self.root.bind("<Down>", self.down)  # 下矢印キー
        self.root.bind("<Return>", self.enter)  # Enterキー

        self.SECELT = "#FF0000"  # red
        self.NOT_SECELT = "#0000FF"  # blue
        self.menu = [
            {"text": "開始", "color": self.SECELT},
            {"text": "課金", "color": self.NOT_SECELT},
            {"text": "設定", "color": self.NOT_SECELT},
            {"text": "終了", "color": self.NOT_SECELT},
        ]
        self.select_value = 0
        self.labels = []

        self.draw_menue()

    # メニュー描写
    def draw_menue(self) -> None:
        for i in range(len(self.menu)):
            self.label = tk.Label(
                self.root, text=self.menu[i]["text"], bg=self.menu[i]["color"]
            )
            self.label.pack()
            self.labels.append(self.label)

    # 上キー
    def up(self, event: tk.Event) -> None:
        print("↑")
        if self.select_value > 0:
            self.select_value -= 1
        self.change_color()
        self.reset()
        self.draw_menue()

    # 下キー
    def down(self, event: tk.Event) -> None:
        print("↓")
        # 選択値を下に移動する処理を追加することができます
        if self.select_value < 3:
            self.select_value += 1
        self.change_color()
        self.reset()
        self.draw_menue()

    # Enterキー
    def enter(self, event: tk.Event) -> None:
        """Enterキーが押されたときの処理"""
        print("Enterキーが押されました")
        # 選択されたメニューの処理を追加することができます
        self.reset()
        self.root.destroy()
        return self.select_value

    # 終了
    def exit(self) -> None:
        print("終了します")
        self.select_value = 3
        self.root.destroy()

    # リセット
    def reset(self) -> None:
        for label in self.labels:
            label.pack_forget()  # ラベルを非表示にする
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


if __name__ == "__main__":
    import setting_enviroments as env
    env.init()

    # スタートメニュー
    title = tk.Tk()
    title.title("Start Menu")
    title.geometry("500x300")
    top = top_page(title)
    title.mainloop()
    value=top.get_select_value()
    print(value)

    # ゲーム画面
    if value != 3:
        root=tk.Tk()
        root.title("Game Play")
        root.geometry("400x300")
        root.mainloop()
