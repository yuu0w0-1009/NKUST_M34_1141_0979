from tkinter import *
import math

# 1. 建立 tkinter 主視窗 
root = Tk()
root.title("") # 設定視窗標題與範例一致 

# 2. 在終端機取得使用者輸入
n = int(input(""))

# 準備一個串列，用來儲存每一層的字串
triangle_lines = []

# 3. 計算第 0 到第 N 層的 Pascal Triangle 
for i in range(n + 1):
    row_numbers = []
    # 第 i 層共有 i+1 個數字 
    for j in range(i + 1):
        # 計算第 j 個數字並轉為字串
        num = math.comb(i, j)
        row_numbers.append(str(num))
    # 將這一層的所有數字用空格隔開連接起來 (使用4個空格讓間距較為明顯)
    row_str = "    ".join(row_numbers)
    triangle_lines.append(row_str)
# 將每一層的字串以換行符號 (\n) 連接成一整個大字串
final_text = "\n".join(triangle_lines)

# 4. 顯示在畫面上並排版成正三角形 
# 使用 justify="center" 可以自動將每一行置中對齊，自然形成正三角形
label = Label(
    root, 
    text=final_text, 
    justify="center", # 這是呈現正三角形排版的關鍵
    padx=30,          # 增加左右邊距讓視窗比較好看
    pady=20           # 增加上下邊距
)
label.pack()

# 啟動視窗並進入事件迴圈
root.mainloop()