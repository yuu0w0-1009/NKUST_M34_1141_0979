import tkinter as tk

def on_click(row, col):
    global current_player
    
    # 1. 禁止玩家點擊已經有符號的格子
    buttons[row][col].config(state=tk.DISABLED) # 點擊後立即停用該按鈕，防止重複點擊

    # 2. 根據目前玩家，設定按鈕的文字符號 (玩家0是 "O", 玩家1是 "X")
    symbol = "O" if current_player == 0 else "X"
    buttons[row][col].config(text=symbol)
    
    # 3. 檢查是否有玩家獲勝
    if check_winner(symbol):
        status_label.config(text=f"玩家{current_player}獲得勝利")
        disable_all() # 遊戲結束，停用所有按鈕
        return
        
    # 4. 檢查是否平手 (全部9格都填滿了)
    if check_tie():
        status_label.config(text="平手!!!遊戲結束!!!")
        return
        
    # 5. 若無人獲勝且未平手，則切換玩家 (0變1，1變0)
    current_player = 1 - current_player
    status_label.config(text=f"換玩家{current_player}了")


def check_winner(symbol):
    # 檢查 3 個橫列
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] == symbol:
            return True
            
    # 檢查 3 個直行
    for j in range(3):
        if buttons[0][j]['text'] == buttons[1][j]['text'] == buttons[2][j]['text'] == symbol:
            return True
            
    # 檢查 2 條對角線
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] == symbol:
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] == symbol:
        return True
        
    return False


def check_tie():
    # 檢查是否還有空格，如果有空格代表還沒平手
    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] == "":
                return False
    return True


def disable_all():
    # 將所有按鈕設為停用狀態 (DISABLED)，防止遊戲結束後玩家繼續點擊
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state=tk.DISABLED)


# === 視窗與 UI 初始化設定 ===
window = tk.Tk()
window.title("九宮格遊戲")

# 記錄目前玩家，0 代表玩家0，1 代表玩家1
current_player = 0 

# 建立上方的狀態提示標籤 (黃色背景，並橫跨3個欄位)
status_label = tk.Label(window, text="遊戲開始!!請玩家0先下", bg="yellow", height=2)
status_label.grid(row=0, column=0, columnspan=3, sticky="we")

# 建立一個 3x3 的串列來存放按鈕物件
buttons = [[None for _ in range(3)] for _ in range(3)]

# 透過迴圈產生 9 個按鈕
for i in range(3):
    for j in range(3):
        # 建立按鈕，並使用 lambda 傳遞當下按鈕的座標 (i, j) 給 on_click 函式
        buttons[i][j] = tk.Button(window, text="", width=10, height=4,command=lambda r=i, c=j: on_click(r, c))
        # 放置按鈕到視窗中 (row 從 1 開始，因為 row 0 已經給了上方的黃底標籤)
        buttons[i][j].grid(row=i+1, column=j)

# 啟動視窗主迴圈
window.mainloop()