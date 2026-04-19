# 📚 Python Tkinter 課程與作業程式碼總整理

## 一、 基礎視窗與排版 (對應 CH01、CH02-3)

建立所有的 GUI 程式，第一步都是建立主視窗，接著利用排版系統將元件放上去。作業中的九宮格、計算機都會大量用到 `grid()`。

### 1. 建立基本視窗
```python
from tkinter import *

root = Tk()                  # 建立主視窗
root.title("我的視窗")        # 設定視窗標題
# 設定大小與位置："寬度x高度+水平座標+垂直座標"
root.geometry("450x300+0+0") 
root.mainloop()              # 啟動事件循環 (必須放在程式最後一行)
```

### 2. 三大排版方式
* **`pack()`**: 依照上下左右方向依序擺放 (適合簡單排版)
* **`place()`**: 絕對座標擺放 (作業1 帕斯卡三角形可能會用到，用來微調位置變成正三角形)
* **`grid()`**: 網格排版 (作業2 計算機、作業3~5 九宮格與配對遊戲 **必用**)

```python
# --- pack 用法 ---
Label(root, text="Pack").pack(side=BOTTOM, padx=10, pady=10) # 靠下，設定外邊距

# --- place 用法 ---
Label(root, text="Place").place(x=80, y=50) # 絕對座標 x, y

# --- grid 用法 (作業最常用) ---
# row 控制列，column 控制行
Button(root, text="7").grid(row=0, column=0)
Button(root, text="8").grid(row=0, column=1)
```

### 3. Frame 容器與自適應大小
當作業畫面變得複雜（例如計算機上方顯示區、下方按鍵區），可以使用 `Frame` 來分區。
```python
# 建立一個 Frame
f = Frame(root, height=150, width=150, bg="red")
f.pack_propagate(0) # 讓 Frame 不會因為裡面的元件而自動縮小 (維持固定大小)
f.grid(row=0, column=0)

# 將按鈕塞滿整個 Frame (fill=BOTH, expand=1)
b = Button(f, text="按鈕")
b.pack(expand=1, fill=BOTH)
```

---

## 二、 核心元件 Label 與 Button (對應 CH02、CH03)

### 1. Label (標籤：用來顯示文字或圖片)
作業1 (帕斯卡三角形)、作業2 (計算機顯示結果) 會頻繁使用。
```python
# 基本建立
lbl = Label(root, text="Hello", bg="yellow", fg="black")
lbl.pack()

# 顯示內建圖示與文字位置
Label(root, text="警告", compound="bottom", bitmap="warning").pack()

# 動態更改 Label 的文字或顏色 (作業必備)
lbl.config(text="新的計算結果", bg="red")
```

### 2. Button (按鈕：用來點擊互動)
作業2~5 遊戲的核心元件。
```python
# 設定按鈕樣式：relief (FLAT, GROOVE, RAISED, RIDGE, SOLID, SUNKEN)
# 大小：width (字元寬), height (字元高)
btn = Button(root, text="Click", width=10, height=4, relief=RAISED)
btn.pack()
```

---

## 三、 事件綁定與回呼函式 Callback (對應 CH02-2)

這是所有作業（計算機、九宮格遊戲）的**靈魂核心**。當按鈕被按下時，程式需要知道「你按下了哪一個數字或哪一格」。

### 1. 基礎事件綁定 (Bind)
```python
def hide_me(event):
    # 點擊後隱藏被點擊的元件 (作業4、5 可能會用到)
    event.widget.grid_forget()

btn = Button(root, text="隱藏我")
btn.bind("<Button-1>", hide_me) # <Button-1> 代表滑鼠左鍵
```

### 2. 進階命令綁定與 Lambda (🌟 迴圈建立按鈕必備)
在利用 `for` 迴圈產生九宮格或計算機按鈕時，如果直接寫 `command=func(x)` 會在建立時就立刻執行。**必須使用 `lambda`** 來延遲執行並傳遞參數。

```python
def click_btn(r, c):
    print(f"你點擊了第 {r} 列，第 {c} 行")

# 利用迴圈產生 3x3 按鈕陣列 (作業2、3、4、5的基礎寫法)
for i in range(9):
    r = int(i / 3)  # 計算列 (0, 1, 2)
    c = i % 3       # 計算行 (0, 1, 2)
    
    # 🌟 重點：使用 lambda 捕捉當下的 r 與 c 值
    Button(root, text=str(i), width=5, height=2, 
           command=lambda r=r, c=c: click_btn(r, c)).grid(row=r, column=c)
```

---

## 四、 作業實戰技巧與動態變化提示

### 技巧 1：全域變數狀態管理 (Global Variables)
在圈圈叉叉 (作3, 作4) 或配對遊戲 (作5) 中，你需要記錄「現在是誰的回合」或「目前翻開了什麼」。
```python
player_turn = 1   # 1代表玩家一(O)，2代表玩家二(X)
click_count = 0   # 記錄點擊次數

def button_click(r, c):
    global player_turn, click_count  # 宣告使用全域變數
    
    if player_turn == 1:
        # 修改按鈕文字為 O
        buttons[r][c].config(text="O")
        player_turn = 2
    else:
        buttons[r][c].config(text="X")
        player_turn = 1
```

### 技巧 2：按鈕狀態控制 (State) -> 作業5 (配對遊戲)
當兩個數字配對成功時，你需要讓按鈕「失效」(不能再點擊)。
```python
# 讓按鈕無法被點擊 (變灰)
btn.config(state="disabled")  

# 恢復按鈕可以被點擊
btn.config(state="normal")
```

### 技巧 3：清除畫面重置 (Grid_forget / Destroy) -> 作業4 (進階九宮格)
按下「Restart」或「下一關擴大版面」時，你需要清空原本的畫面。
```python
# 方法一：隱藏元件 (CH02教的)
btn.grid_forget()

# 方法二：直接摧毀 Frame 裡面的所有元件並重新產生 (常見實戰作法)
for widget in root.winfo_children():
    widget.destroy()
# 接著再重新呼叫建立版面的 function
```

### 技巧 4：帕斯卡三角形算法提示 -> 作業1
要算出 $C(i, j)$ 的值，需要用到階乘。可以使用 Python 內建函式庫：
```python
import math
def pascal_value(i, j):
    # C(i, j) = i! / (j! * (i-j)!)
    return math.factorial(i) // (math.factorial(j) * math.factorial(i - j))
```
*排版建議：利用迴圈建立 `Label`，並使用 `pack()` 或 `grid()` 配合空白字元，或者直接用 `place()` 計算水平偏移量來達成正三角形。*