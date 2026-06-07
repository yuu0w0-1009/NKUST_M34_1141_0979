import tkinter as tk
import random

root = tk.Tk()
root.title("打地鼠遊戲")

# --- 遊戲初始狀態與設定 ---
stage = 1           # 目前關卡
score = 0           # 總分
moles_left = 0      # 畫面上剩餘的地鼠數量
stage_time = 2000   # 每關的時間限制 (2000 毫秒 = 2 秒)
timer_id = None     # 紀錄計時器 ID，方便重設時間
buttons = []        # 新增：建立一個全域變數來存放二維按鈕陣列

# --- 建立 UI 介面 ---
def create_widgets():
    global stage_label, moles_label, score_label, buttons
    
    # 1. 上方遊戲區：建立 10x10 的按鈕網格
    grid_frame = tk.Frame(root)
    grid_frame.pack()
    
    for r in range(10):
        row_buttons = []
        for c in range(10):
            # 建立按鈕，點擊時會觸發 hit_mole 並傳入座標 (r, c)
            btn = tk.Button(grid_frame, text="", width=4, height=2,
                            command=lambda r=r, c=c: hit_mole(r, c))
            btn.grid(row=r, column=c)
            row_buttons.append(btn)
        buttons.append(row_buttons) # 將整列按鈕加入二維列表

    # 2. 下方資訊區：顯示關卡、數量與總分
    info_frame = tk.Frame(root)
    info_frame.pack(pady=10)

    # Stage 標籤
    stage_label = tk.Label(info_frame, text="Stage: 1", font=("Arial", 12))
    stage_label.grid(row=0, column=0, padx=20)

    # 地鼠數量 標籤
    moles_label = tk.Label(info_frame, text="地鼠數量: 0", font=("Arial", 12))
    moles_label.grid(row=0, column=1, padx=20)

    # 總分 標籤
    score_label = tk.Label(info_frame, text="總分: 0", font=("Arial", 12))
    score_label.grid(row=1, column=0, columnspan=2, pady=5)

# --- 開始第一關 ---
def start_stage():
    global timer_id, moles_left, buttons
    
    # 1. 清空上一關的盤面 (對 buttons 陣列操作)
    for r in range(10):
        for c in range(10):
            buttons[r][c].config(text="")

    # 2. 隨機決定這關要有幾隻地鼠
    moles_left = random.randint(5, 12)

    # 3. 在 100 個格子中隨機抽出要放地鼠的位置
    positions = random.sample(range(100), moles_left)
    for pos in positions:
        r = pos // 10  # 計算列 (row)
        c = pos % 10   # 計算行 (column)
        buttons[r][c].config(text="M") # 指定位置顯示 "M"

    # 4. 更新畫面文字
    update_labels()

    # 5. 設定倒數計時器
    if timer_id is not None:
        root.after_cancel(timer_id)
    # 設定過了 stage_time 毫秒後，自動執行 next_stage 換下一關
    timer_id = root.after(stage_time, next_stage)

def hit_mole(r, c):
    global score, moles_left, buttons
    # 檢查玩家點擊的按鈕上面是不是地鼠 ("M")
    if buttons[r][c]["text"] == "M":
        # 如果是，就把地鼠清掉，總分+1，剩餘地鼠-1
        buttons[r][c].config(text="")
        score += 1
        moles_left -= 1
        update_labels() # 更新文字顯示

def next_stage():
    global stage
    # 關卡數 +1，並重新開始新的一關
    stage += 1
    start_stage()

def update_labels():
    global stage_label, moles_label, score_label
    # 更新三個 Label 的顯示文字
    stage_label.config(text=f"Stage: {stage}")
    moles_label.config(text=f"地鼠數量: {moles_left}")
    score_label.config(text=f"總分: {score}")

# --- 主程式執行區 ---

create_widgets() # 建立 UI 元件
start_stage()    # 啟動第一關

root.mainloop()