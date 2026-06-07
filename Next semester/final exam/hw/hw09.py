import tkinter as tk
import random
import string

class TypingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("TOD")
        self.root.resizable(False, False)

        # --- 遊戲設定 ---
        self.cols = 10
        self.rows = 10
        self.cell_size = 40
        self.canvas_width = self.cols * self.cell_size
        self.canvas_height = self.rows * self.cell_size

        self.score = 0
        self.total_dropped = 0
        self.max_blocks = 10     # 總共掉落 10 個方塊
        self.active_blocks = []  # 儲存目前在畫面上的方塊 ID
        self.game_over = False

        # --- UI 介面佈局 ---
        # 1. 遊戲主要畫布 (繪製格線與方塊)
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="#f0f0f0")
        self.canvas.pack(padx=5, pady=5)
        self.draw_grid()

        # 2. 底部控制區塊框架
        self.bottom_frame = tk.Frame(root)
        self.bottom_frame.pack(fill=tk.X, padx=5, pady=(0, 5))

        # 提示文字 Label
        self.target_var = tk.StringVar()
        self.target_label = tk.Label(self.bottom_frame, textvariable=self.target_var, width=10, anchor='w', font=("Arial", 12))
        self.target_label.pack(side=tk.LEFT)

        # 玩家輸入 Entry
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.bottom_frame, textvariable=self.entry_var, font=("Arial", 12))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        # 綁定 Enter 鍵來檢查輸入
        self.entry.bind("<Return>", self.check_input)

        # 分數 Label
        self.score_var = tk.StringVar()
        self.score_var.set("score: 0")
        self.score_label = tk.Label(self.bottom_frame, textvariable=self.score_var, width=10, anchor='e', font=("Arial", 12))
        self.score_label.pack(side=tk.RIGHT)

        # --- 初始化遊戲 ---
        self.next_word()
        self.entry.focus()       # 讓輸入框自動獲得焦點
        self.spawn_block()       # 開始掉落第一個方塊
        self.update_blocks()     # 啟動方塊掉落更新迴圈

    def draw_grid(self):
        """繪製 10x10 的背景格線"""
        for i in range(self.cols + 1):
            x = i * self.cell_size
            self.canvas.create_line(x, 0, x, self.canvas_height, fill="gray")
        for i in range(self.rows + 1):
            y = i * self.cell_size
            self.canvas.create_line(0, y, self.canvas_width, y, fill="gray")

    def next_word(self):
        """隨機產生 1~5 個字母的字串作為練習目標"""
        length = random.randint(1, 5)
        word = ''.join(random.choices(string.ascii_lowercase, k=length))
        self.target_var.set(word)

    def spawn_block(self):
        """隨機從最上方位置掉落方塊，並設定為每 1000 毫秒 (1秒) 出現一個"""
        if self.game_over or self.total_dropped >= self.max_blocks:
            return

        # 隨機選擇欄位
        col = random.randint(0, self.cols - 1)
        x1 = col * self.cell_size
        y1 = 0
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size

        # 建立方塊並記錄其 ID
        block = self.canvas.create_rectangle(x1, y1, x2, y2, fill="darkgray", outline="black")
        self.active_blocks.append(block)
        self.total_dropped += 1

        # ⭐️ 核心修改：將 2500 改為 1000，實現一秒生成一個
        if self.total_dropped < self.max_blocks:
            self.root.after(1000, self.spawn_block)

    def update_blocks(self):
        """處理方塊的向下移動動畫"""
        if self.game_over:
            return

        blocks_to_remove = []
        for block in self.active_blocks:
            # ⭐️ 核心修改 1：每次向下移動「一整格」的距離
            self.canvas.move(block, 0, self.cell_size)
            coords = self.canvas.coords(block)
            
            # 如果方塊落出邊界，將其從畫面上移除
            if coords[1] >= self.canvas_height:
                blocks_to_remove.append(block)

        # 清理已經落到底部的方塊
        for block in blocks_to_remove:
            self.active_blocks.remove(block)
            self.canvas.delete(block)

        self.check_game_over()

        # ⭐️ 核心修改 2：將更新間隔拉長到 800 毫秒，也就是每 0.8 秒下降一格
        if not self.game_over:
            self.root.after(1000, self.update_blocks)

    def check_input(self, event):
        """檢查玩家輸入的文字"""
        if self.game_over:
            return

        user_input = self.entry_var.get()
        # 當輸入的文字與目前要輸入文字相同時 [cite: 6]
        if user_input == self.target_var.get():
            self.score += 1
            self.score_var.set(f"score: {self.score}")
            self.entry_var.set("") # 清空輸入框
            self.next_word()       # 換下一個單字

            if self.active_blocks:
                # 找出離底部最近 (Y軸座標最大) 的方塊並消除
                lowest_block = max(self.active_blocks, key=lambda b: self.canvas.coords(b)[1])
                self.active_blocks.remove(lowest_block)
                self.canvas.delete(lowest_block)

            self.check_game_over()
        else:
            self.entry_var.set("") 

    def check_game_over(self):
        """檢查遊戲結束條件：當方塊都掉落完或者被消除完畢，則遊戲結束 [cite: 8]"""
        if self.total_dropped >= self.max_blocks and not self.active_blocks:
            self.game_over = True
            self.target_var.set("Game Over!")
            self.entry.config(state="disabled") # 停用輸入框

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingGame(root)
    root.mainloop()