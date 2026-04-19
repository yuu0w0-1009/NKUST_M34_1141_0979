from tkinter import *

root = Tk()
root.title("圈圈叉叉遊戲")

User1 = "O"
User2 = "X"
now = 0
data = ["."] * 9
result = 0
buttons = []

def check_winner(board):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combo in win_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != '.':
            return board[a] + 3

    if '.' not in board:
        return 5  

    return 999  

def disable_all_buttons():
    for btn in buttons:
        btn.config(state="disabled")

def check(x):
    global now
    global result
    
    text = User1 if now == 0 else User2
    data[x] = now
    
    buttons[x].config(text=text, state="disabled")
    
    result = check_winner(data)
    
    if result != 999:
        set_sysT(result)
        disable_all_buttons()
    else:
        now = 1 if now == 0 else 0
        set_sysT(now + 1)

def start():
    global buttons
    Label(root, text="", font=("", 24)).grid(row=0, column=0, columnspan=3)
    
    buttons = []
    for i in range(9):
        r = (i // 3) + 1
        c = i % 3
        btn = Button(root, text="", width=10, height=5, bd=2, 
                     command=lambda i=i: check(i))
        btn.grid(row=r, column=c)
        buttons.append(btn)

def set_sysT(x):
    systrmText = ""
    Label(root, text="                             ", font=("", 24)).grid(row=0, column=0, columnspan=3)
    match (x):
        case 0:
            systrmText = "開始 玩家0先下"
        case 1:
            systrmText = "換玩家1"
        case 2:
            systrmText = "換玩家0"
        case 3:
            systrmText = "玩家0獲勝"
        case 4:
            systrmText = "玩家1獲勝"
        case 5:
            systrmText = "平手"
    Label(root, text=systrmText, font=("", 24)).grid(row=0, column=0, columnspan=3)

start()
set_sysT(0)
