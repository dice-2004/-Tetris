import tkinter as tk
from tkinter import PhotoImage
import os
from typing import Dict, Optional

class Top_page:
    def __init__(self, window_title: str, width: int, height: int, x_position: int, y_position: int) -> None:
        # ウィンドウの初期化
        self.root = tk.Tk()
        self.root.title(window_title)
        self.root.geometry(f"{width}x{height}+{x_position}+{y_position}")
        
        # 画像パスの設定
        self.IMAGE_FILEPATH = [
            os.path.abspath("src/assets/images/menu_start.png"),
            os.path.abspath("src/assets/images/menu_setting.png"),
            os.path.abspath("src/assets/images/menu_charge.png")
        ]
        
        # メニュー状態の初期化
        self.select_value = 0  # デフォルトでGAME STARTを選択
        
        # 画像の読み込みと保存
        self.images: Dict[int, PhotoImage] = {}
        self.load_images()
        
        # メニューラベルの初期化
        self.label = None
        
        # キーバインディング
        self.root.bind('<Up>', self.up)
        self.root.bind('<Down>', self.down)
        self.root.bind('<Return>', self.enter)
        self.root.bind('<Escape>', self.exit)
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        
        # メニューの描画
        self.draw_menu()
        
        # メインループの開始
        self.root.mainloop()

    def load_images(self) -> None:
        """メニュー画像の読み込み"""
        for i, path in enumerate(self.IMAGE_FILEPATH):
            try:
                self.images[i] = PhotoImage(file=path)
            except Exception as e:
                print(f"Error loading image {path}: {e}")
                self.images[i] = None

    def draw_menu(self) -> None:
        """メニューの描画"""
        if self.label is not None:
            self.label.destroy()
        
        current_image = self.images.get(self.select_value)
        if current_image:
            self.label = tk.Label(self.root, image=current_image)
            self.label.pack(expand=True)

    def up(self, event: Optional[tk.Event] = None) -> None:
        """上キーの処理"""
        if self.select_value > 0:
            self.select_value -= 1
            self.draw_menu()
        else :
            self.select_value = 0

    def down(self, event: Optional[tk.Event] = None) -> None:
        """下キーの処理"""
        if self.select_value < 2:
            self.select_value += 1
            self.draw_menu()
        else :
            self.select_value = 2

    def enter(self, event: Optional[tk.Event] = None) -> None:
        """Enterキーの処理"""
        self.root.quit()
        self.root.destroy()

    def exit(self, event = None) -> None:
        """終了処理"""
        self.select_value = 3  # Exit value
        self.root.quit()
        self.root.destroy()

    def get_select_value(self) -> int:
        """選択値の取得"""
        return self.select_value
