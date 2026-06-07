import tkinter as tk

# === 遊戲邏輯與狀態變數 ===
N = 3              # 預設為 3x3 的九宮格
current_player = 0 # 記錄目前玩家，0 代表玩家0，1 代表玩家1
board_state = []   # 用來記錄盤面狀態的二維陣列 (-1:空, 0:玩家0, 1:玩家1)
buttons = []       # 用來存放按鈕物件的二維陣列
empty_img = None   # 用來固定按鈕大小的空白圖片

def on_click(row, col):
    global current_player
    
    # 1. 如果該格已經被點擊過 (不是 -1)，則不執行任何動作
    if board_state[row][col] != -1:
        return

    # 2. 記錄該格是由哪位玩家下的
    board_state[row][col] = current_player
    
    # 3. 根據目前玩家，設定按鈕的內建圖示 (玩家0是 "O", 玩家1是 "X")
    bitmap_name = "O" if current_player == 0 else "X"
    buttons[row][col].config(text=bitmap_name, state=tk.DISABLED) # 設定圖示並停用按鈕
    
    # 4. 檢查是否有玩家獲勝
    if check_winner(current_player):
        status_label.config(text=f"玩家{current_player}獲得勝利")
        disable_all() # 遊戲結束，停用所有按鈕
        return
        
    # 5. 檢查是否平手 (全部格子都填滿了)
    if check_tie():
        status_label.config(text="平手!!!遊戲結束!!!")
        return
        
    # 6. 若無人獲勝且未平手，則切換玩家 (0變1，1變0)
    current_player = 1 - current_player
    status_label.config(text=f"換玩家{current_player}了")


def check_winner(player):
    # 檢查所有橫列是否有 N 個連線
    for i in range(N):
        win = True
        for j in range(N):
            if board_state[i][j] != player:
                win = False
                break
        if win: return True
            
    # 檢查所有直行是否有 N 個連線
    for j in range(N):
        win = True
        for i in range(N):
            if board_state[i][j] != player:
                win = False
                break
        if win: return True
            
    # 檢查左上到右下的對角線
    win = True
    for i in range(N):
        if board_state[i][i] != player:
            win = False
            break
    if win: return True

    # 檢查右上到左下的對角線
    win = True
    for i in range(N):
        if board_state[i][N - 1 - i] != player:
            win = False
            break
    if win: return True
        
    return False


def check_tie():
    # 檢查盤面上是否還有 -1 (代表還有空格)
    for i in range(N):
        for j in range(N):
            if board_state[i][j] == -1:
                return False
    return True


def disable_all():
    # 將所有按鈕設為停用狀態 (DISABLED)，防止遊戲結束後玩家繼續點擊
    for i in range(N):
        for j in range(N):
            buttons[i][j].config(state=tk.DISABLED)


def restart_game():
    # 重新開始「本關」，N 的大小不變
    init_board()


def next_level():
    global N
    # 進入下一關，將盤面大小 N 增加 1
    N += 1
    init_board()


def init_board():
    global current_player, board_state, buttons, status_label, empty_img
    
    # 初始化玩家與盤面狀態 None 代表該格為空)
    current_player = 0
    board_state = [[-1 for _ in range(N)] for _ in range(N)]
    
    # 清空視窗內所有的舊元件 (為了畫出新的大小)
    for widget in window.winfo_children():
        widget.destroy()
        
    # 建立上方的狀態提示標籤，橫跨 N 個欄位
    status_label = tk.Label(window, text="遊戲開始!!請玩家0先下", bg="yellow", height=2)
    status_label.grid(row=0, column=0, columnspan=N, sticky="we")
    
    # 建立一個隱形的圖片，用來強制把按鈕的大小固定為像素 (這樣圖示才不會讓按鈕縮小)
    empty_img = tk.PhotoImage()
    
    # 透過迴圈產生 N x N 個按鈕
    buttons = [[None for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # width=80, height=80 在有設定 image 的情況下，會以「像素」為單位
            buttons[i][j] = tk.Button(window, width=10, height=4,
            command=lambda r=i, c=j: on_click(r, c))
            buttons[i][j].grid(row=i+1, column=j)
            
    # 建立下方 Restart 按鈕 (跨越前面的欄位)
    restart_btn = tk.Button(window, text="Restart", height=4, command=restart_game)
    restart_btn.grid(row=N+1, column=0, columnspan=N-1, sticky="we")
    
    # 建立下方 下一關 按鈕 (放在最後一個欄位)
    next_btn = tk.Button(window, text="下一關", width=10, height=4, command=next_level)
    next_btn.grid(row=N+1, column=N-1, sticky="we")


# === 視窗與 UI 初始化設定 ===
window = tk.Tk()
window.title("進階版九宮格遊戲")

# 呼叫函式來畫出初始的遊戲盤面
init_board()

# 啟動視窗主迴圈
window.mainloop()