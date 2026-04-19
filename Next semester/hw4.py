import tkinter as tk

class AdvancedTicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("進階版九宮格")
        
        # 初始狀態
        self.current_size = 3  # 從 3x3 開始
        self.current_player = 0
        self.symbols = ["O", "X"]
        self.game_over = False
        
        self.setup_ui()
        self.start_game()

    def setup_ui(self):
        # 1. 上方狀態欄 (黃色背景)
        self.status_label = tk.Label(
            self.root, text="", bg="yellow", font=("Arial", 12, "bold"), height=2
        )
        self.status_label.pack(fill=tk.X)

        # 2. 中間棋盤容器 (重要：不給固定高寬，讓按鈕撐開它)
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(expand=True, fill=tk.BOTH)

        # 3. 下方按鈕區 (確保它永遠在最底下)
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.restart_btn = tk.Button(
            self.control_frame, text="Restart", command=self.reset_current_level, 
            height=2
        )
        self.restart_btn.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.next_level_btn = tk.Button(
            self.control_frame, text="下一關", command=self.next_level, 
            height=2
        )
        self.next_level_btn.pack(side=tk.LEFT, expand=True, fill=tk.X)

    def start_game(self):
        """初始化或重建棋盤並自動調整視窗"""
        self.game_over = False
        self.current_player = 0
        self.status_label.config(text=f"遊戲開始!!請玩家{self.current_player}先下")
        
        # 清除舊按鈕
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        self.buttons = []
        self.board = [["" for _ in range(self.current_size)] for _ in range(self.current_size)]

        # 建立動態格線
        for r in range(self.current_size):
            row_btns = []
            for c in range(self.current_size):
                # 這裡固定按鈕的大小，視窗會被這些按鈕撐大
                btn = tk.Button(
                    self.grid_frame, text="", font=("Arial", 16, "bold"), 
                    width=4, height=2,
                    command=lambda r=r, c=c: self.handle_click(r, c)
                )
                btn.grid(row=r, column=c, sticky="nsew")
                row_btns.append(btn)
            self.buttons.append(row_btns)

        # 讓每一列每一行都能均等縮放
        for i in range(self.current_size):
            self.grid_frame.grid_columnconfigure(i, weight=1)
            self.grid_frame.grid_rowconfigure(i, weight=1)

        # 【關鍵步驟】強制更新視窗佈局，並讓視窗適應內容大小
        self.root.update_idletasks()
        self.root.geometry("")  # 設定為空字串，tkinter 會自動計算最小需要的視窗大小

    def handle_click(self, r, c):
        if self.board[r][c] == "" and not self.game_over:
            symbol = self.symbols[self.current_player]
            self.board[r][c] = symbol
            self.buttons[r][c].config(text=symbol)

            if self.check_winner(r, c):
                self.status_label.config(text=f"玩家{self.current_player}獲得勝利")
                self.game_over = True
            elif self.is_draw():
                self.status_label.config(text="平手!!!遊戲結束!!!")
                self.game_over = True
            else:
                self.current_player = 1 - self.current_player
                self.status_label.config(text=f"換玩家{self.current_player}了")

    def check_winner(self, r, c):
        symbol = self.board[r][c]
        size = self.current_size
        # 檢查橫向
        if all(self.board[r][i] == symbol for i in range(size)): return True
        # 檢查縱向
        if all(self.board[i][c] == symbol for i in range(size)): return True
        # 檢查主對角線
        if r == c and all(self.board[i][i] == symbol for i in range(size)): return True
        # 檢查副對角線
        if r + c == size - 1 and all(self.board[i][size - 1 - i] == symbol for i in range(size)): return True
        return False

    def is_draw(self):
        return all(self.board[r][c] != "" for r in range(self.current_size) for c in range(self.current_size))

    def reset_current_level(self):
        self.start_game()

    def next_level(self):
        self.current_size += 1
        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    # 移除固定的 root.geometry，讓它自然生長
    game = AdvancedTicTacToe(root)
    root.mainloop()