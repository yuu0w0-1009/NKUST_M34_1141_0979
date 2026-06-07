import tkinter as tk
import random

# --- 全域變數 ---
first_btn = None        # 用來記錄每次配對時按下的「第一個按鈕」
remaining_pairs = 50    # 剩餘配對數，預設為 50 組

def button_click(btn):
    global first_btn, remaining_pairs
    
    # 若按鈕已經被按下了(處於禁用狀態)，就不做任何事
    if btn['state'] == tk.DISABLED:
        return
        
    # 【情況一】這是點擊的「第一個」按鈕
    if first_btn is None:
        first_btn = btn
        btn.config(state=tk.DISABLED) # 將按下的按鈕設為停用(變灰)
        
    # 【情況二】這是點擊的「第二個」按鈕
    else:
        btn.config(state=tk.DISABLED) # 先將第二個按鈕也停用
        
        # 判斷配對是否成功 (比較兩個按鈕的文字)
        if btn['text'] == first_btn['text']:
            # 配對成功：更新剩餘數量與標籤
            remaining_pairs -= 1
            label.config(text=f"剩餘配對數: {remaining_pairs}")
            first_btn = None # 清空紀錄，準備下一輪配對
            
        else:
            # 配對失敗：延遲 300 毫秒後，把兩個按鈕恢復成正常狀態
            # 延遲是為了讓玩家看清楚按錯的數字
            window.after(300, reset_buttons, first_btn, btn)
            first_btn = None # 清空紀錄

def reset_buttons(btn1, btn2):
    """恢復按鈕狀態的輔助函式"""
    btn1.config(state=tk.NORMAL)
    btn2.config(state=tk.NORMAL)

# --- 主視窗設定 ---
window = tk.Tk()
window.title("配對遊戲")

# 準備數字 0~9，每個數字出現 10 次 (共 100 個數字)
numbers = list(range(10)) * 10
random.shuffle(numbers) # 隨機打亂數字陣列

# 建立 10x10 的按鈕網格
for r in range(10):
    for c in range(10):
        # 從打亂的陣列取出一個數字
        num = numbers.pop() 
        
        # 建立按鈕，設定大小與字體
        btn = tk.Button(window, text=str(num), width=3, height=1, font=('Arial', 14))
        
        # 綁定點擊事件。使用 lambda: button_click(b) 確保每個按鈕傳遞的是自己
        btn.config(command=lambda b=btn: button_click(b))
        
        # 將按鈕放置到網格上
        btn.grid(row=r, column=c, padx=1, pady=1)

# 顯示剩餘配對數的標籤 (放置在第 11 列，跨越 10 個欄位)
label = tk.Label(window, text=f"剩餘配對數: {remaining_pairs}", font=('Arial', 12))
label.grid(row=10, column=0, columnspan=10, pady=5)

# 啟動應用程式
window.mainloop()   