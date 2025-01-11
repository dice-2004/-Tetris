
import random

import tkinter as tk
import ctypes
import tkinter.messagebox as messagebox
from typing import List, Any,Dict
from time import sleep

from utils import setting_enviroments as env
from entities.top import Top_page
from entities import game

# 初期化処理
value:int = env.init()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
fall_interval:int = 500 # (ms)

class Tetris:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple Tetris")
        
        # ゲーム設定
        self.BOARD_WIDTH = 10
        self.BOARD_HEIGHT = 20
        self.BLOCK_SIZE = 30
        self.GAME_SPEED = 500  # ミリ秒
        
        # テトリミノの形状定義
        self.SHAPES = {
            'I': [[1, 1, 1, 1]],
            'O': [[1, 1],
                  [1, 1]],
            'T': [[0, 1, 0],
                  [1, 1, 1]],
            'S': [[0, 1, 1],
                  [1, 1, 0]],
            'Z': [[1, 1, 0],
                  [0, 1, 1]],
            'J': [[1, 0, 0],
                  [1, 1, 1]],
            'L': [[0, 0, 1],
                  [1, 1, 1]]
        }
        
        # 色の定義
        self.COLORS = {
            'I': 'cyan',
            'O': 'yellow',
            'T': 'purple',
            'S': 'green',
            'Z': 'red',
            'J': 'blue',
            'L': 'orange',
            0: 'black'  # 空きマス用
        }
        
        # ゲームボード初期化
        self.board = [[0 for _ in range(self.BOARD_WIDTH)] for _ in range(self.BOARD_HEIGHT)]
        
        # Canvas作成
        self.canvas = tk.Canvas(
            self.root,
            width=self.BOARD_WIDTH * self.BLOCK_SIZE,
            height=self.BOARD_HEIGHT * self.BLOCK_SIZE,
            bg='black'
        )
        self.canvas.pack()
        
        # スコア表示
        self.score = 0
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}")
        self.score_label.pack()
        
        # 現在のテトリミノ
        self.current_piece = None
        self.current_x = 0
        self.current_y = 0
        self.current_shape = None
        
        # キーバインド
        self.root.bind('<Left>', self.move_left)
        self.root.bind('<Right>', self.move_right)
        self.root.bind('<Down>', self.move_down)
        self.root.bind('<z>', self.rotate_left)
        self.root.bind('<c>', self.rotate_right)
        self.root.bind('<space>', self.drop)

        self.update_id = None
        
        # ゲーム開始
        self.spawn_piece()
        self.update()
        
        self.root.mainloop()
    
    def draw_board(self):
        self.canvas.delete('all')
        # 固定されたブロックの描画
        for y in range(self.BOARD_HEIGHT):
            for x in range(self.BOARD_WIDTH):
                if self.board[y][x]:
                    self.draw_block(x, y, self.board[y][x])
        
        # 現在落下中のテトリミノの描画
        if self.current_piece:
            for y, row in enumerate(self.current_piece):
                for x, val in enumerate(row):
                    if val:
                        self.draw_block(
                            self.current_x + x,
                            self.current_y + y,
                            self.current_shape
                        )
    
    def draw_block(self, x, y, shape):
        x1 = x * self.BLOCK_SIZE
        y1 = y * self.BLOCK_SIZE
        x2 = x1 + self.BLOCK_SIZE
        y2 = y1 + self.BLOCK_SIZE
        self.canvas.create_rectangle(
            x1, y1, x2, y2,
            fill=self.COLORS[shape],
            outline='white'
        )
    
    def spawn_piece(self):
        self.current_shape = random.choice(list(self.SHAPES.keys()))
        self.current_piece = self.SHAPES[self.current_shape]
        self.current_x = self.BOARD_WIDTH // 2 - len(self.current_piece[0]) // 2
        self.current_y = 0
        
        if self.check_collision():
            self.game_over()
    
    def check_collision(self):
        for y, row in enumerate(self.current_piece):
            for x, val in enumerate(row):
                if val:
                    if (self.current_y + y >= self.BOARD_HEIGHT or
                        self.current_x + x < 0 or
                        self.current_x + x >= self.BOARD_WIDTH or
                        (self.current_y + y >= 0 and
                         self.board[self.current_y + y][self.current_x + x])):
                        return True
        return False
    
    def merge_piece(self):
        for y, row in enumerate(self.current_piece):
            for x, val in enumerate(row):
                if val and self.current_y + y >= 0:
                    self.board[self.current_y + y][self.current_x + x] = self.current_shape
    
    def move_left(self, event=None):
        self.current_x -= 1
        if self.check_collision():
            self.current_x += 1
        self.draw_board()
    
    def move_right(self, event=None):
        self.current_x += 1
        if self.check_collision():
            self.current_x -= 1
        self.draw_board()
    
    def move_down(self, event=None):
        self.current_y += 1
        if self.check_collision():
            self.current_y -= 1
            self.merge_piece()
            self.clear_lines()
            self.spawn_piece()
        self.draw_board()
    
    def rotate_left(self, event=None):
        # 左回転: 現在のピースを反時計回りに回転
        rotated = list(zip(*self.current_piece))[::-1]
        old_piece = self.current_piece
        self.current_piece = rotated
  
        # 衝突した場合は元に戻す
        if self.check_collision():
            self.current_piece = old_piece
        self.draw_board()

    def rotate_right(self, event=None):
        # 右回転: 現在のピースを時計回りに回転
        rotated = list(zip(*self.current_piece[::-1]))
        old_piece = self.current_piece
        self.current_piece = rotated

        # 衝突した場合は元に戻す
        if self.check_collision():
            self.current_piece = old_piece
        self.draw_board()
    
    def drop(self, event=None):
        while not self.check_collision():
            self.current_y += 1
        self.current_y -= 1
        self.merge_piece()
        self.clear_lines()
        self.spawn_piece()
        self.draw_board()
    
    def clear_lines(self):
        lines_cleared = 0
        for y in range(self.BOARD_HEIGHT - 1, -1, -1):
            if all(self.board[y]):
                lines_cleared += 1
                del self.board[y]
                self.board.insert(0, [0 for _ in range(self.BOARD_WIDTH)])
        
        if lines_cleared:
            self.score += lines_cleared * 100 * lines_cleared  # ボーナススコア
            self.score_label.config(text=f"Score: {self.score}")
    
    def update(self):
        if self.update_id is None:
            return

        self.move_down()
        self.draw_board()
        self.update_id = self.root.after(self.GAME_SPEED, self.update)
    
    def game_over(self):
        self.canvas.create_text(
            self.BOARD_WIDTH * self.BLOCK_SIZE / 2,
            self.BOARD_HEIGHT * self.BLOCK_SIZE / 2,
            text="GAME OVER",
            fill="white",
            font=("Arial", 24)
        )
        self.root.unbind('<Left>')
        self.root.unbind('<Right>')
        self.root.unbind('<Down>')
        self.root.unbind('<Up>')
        self.root.unbind('<space>')

        if self.update_id is not None:
            self.root.after_cancel(self.update_id)
            self.update_id = None

if __name__ == "__main__":
    game = Tetris()