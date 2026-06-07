import tkinter as tk
import random

class MaAhTaiGame:
    def __init__(self, root):
        self.root = root
        self.root.title("麻阿台")
        
        # 將視窗設定為正方形 (700x700 像素)
        self.root.geometry("700x700")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(False, False)

        # 將圖片分為「限定一個」與「可重複」兩組
        self.special_files = ['double7.png', 'star.png']
        self.normal_files = [
            'apple.png', 'betelnut.png', 'grape.png', 
            'orange.png', 'ring.png', 'watermelon.png'
        ]
        
        # 使用字典快取已載入的圖片，避免重複消耗記憶體
        self.images_cache = {}
        for file in self.special_files + self.normal_files:
            try:
                self.images_cache[file] = tk.PhotoImage(file=file)
            except Exception as e:
                print(f"警告：找不到圖片 {file}，請確認圖片與程式位於同一目錄。")

        # 為了配合正方形視窗，將外圍版面改為 7x7 的網格 (總格數一樣是 24 格)
        # 上排左至右: (0,0) ~ (0,6) (7格)
        # 右排上至下: (1,6) ~ (5,6) (5格)
        # 下排右至左: (6,6) ~ (6,0) (7格)
        # 左排下至上: (5,0) ~ (1,0) (5格)
        self.positions = []
        for c in range(7): self.positions.append((0, c))
        for r in range(1, 6): self.positions.append((r, 6))
        for c in range(6, -1, -1): self.positions.append((6, c))
        for r in range(5, 0, -1): self.positions.append((r, 0))

        self.labels = []
        self.current_index = 0
        self.is_spinning = False

        # 設定行列的權重，讓網格能平均分配空間，維持正方形比例
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

        self.setup_ui()

    def setup_ui(self):
        # 1. 先把 77 和 star 加入準備放到版面上的清單 (保證只有一個)
        board_layout = list(self.special_files) 
        
        # 2. 剩下的 22 格，從一般的圖案中隨機抽取並加入
        for _ in range(22):
            board_layout.append(random.choice(self.normal_files))
            
        # 3. 將這 24 個圖案的順序打亂
        random.shuffle(board_layout)

        # 將打亂後的圖案依序放置到 7x7 外圍的網格上
        for i, (r, c) in enumerate(self.positions):
            img_file = board_layout[i]
            img = self.images_cache.get(img_file, None)
            
            # sticky="nsew" 讓格子自動填滿分配到的空間
            lbl = tk.Label(self.root, image=img, bg="white", relief="ridge", bd=2)
            lbl.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
            self.labels.append(lbl)

        # 建立中間的區域來放置 GO 按鈕
        # 中間的空間是 row 1~5, col 1~5 (跨越 5 行 5 列)
        center_frame = tk.Frame(self.root, bg="#f0f0f0")
        center_frame.grid(row=1, column=1, rowspan=5, columnspan=5, sticky="nsew")
        center_frame.grid_rowconfigure(0, weight=1)
        center_frame.grid_columnconfigure(0, weight=1)

        # 建立 GO 按鈕
        self.go_btn = tk.Button(center_frame, text="GO", font=("Arial", 24, "bold"), width=6, height=2, command=self.start_spin)
        self.go_btn.grid(row=0, column=0)

        # 初始設定第一個位置亮起
        if self.labels:
            self.labels[self.current_index].config(bg="red")

    def start_spin(self):
        if self.is_spinning:
            return

        self.is_spinning = True
        self.go_btn.config(state="disabled")

        self.steps_remaining = random.randint(50, 80)
        self.current_speed = 40 

        self.spin()

    def spin(self):
        if not self.labels: 
            return

        self.labels[self.current_index].config(bg="white")
        self.current_index = (self.current_index + 1) % len(self.positions)
        self.labels[self.current_index].config(bg="red")

        self.steps_remaining -= 1

        if self.steps_remaining > 0:
            if self.steps_remaining < 5:
                self.current_speed += 80
            elif self.steps_remaining < 15:
                self.current_speed += 30
            elif self.steps_remaining < 25:
                self.current_speed += 10

            self.root.after(self.current_speed, self.spin)
        else:
            self.is_spinning = False
            self.go_btn.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = MaAhTaiGame(root)
    root.mainloop()