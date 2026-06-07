import tkinter as tk

# 建立主視窗
root = tk.Tk()
root.title("tk") # 設定視窗標題

# 建立一個變數，用來儲存與更新顯示區域的文字 (包含算式與結果)
display_var = tk.StringVar()

def button_click(item):
    """處理數字與運算符號的輸入，將按下的按鍵附加到算式後方"""
    current = display_var.get()
    display_var.set(current + str(item))

def button_clear():
    """清除鍵 (C)，將顯示區域清空"""
    display_var.set("")

def button_equal():
    """等於鍵 (=)，計算算式的結果"""
    try:
        # 使用 eval() 函數可以快速計算字串表示的數學算式 (例如 "9+6")
        result = str(eval(display_var.get()))
        display_var.set(result)
    except Exception:
        # 避免使用者輸入無效算式 (例如 "9+/6") 導致程式崩潰
        display_var.set("Error")

# --- 版面配置 (UI 設計) ---

# 顯示區域 (對應上方空白處顯示按下的按鍵及結果)
# 使用 bg 改變背景顏色模擬空白處，anchor="e" 讓文字靠右對齊
display_label = tk.Label(root, textvariable=display_var, height=2)
display_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

# 定義一個共用的按鍵樣式字典，讓後面的程式碼更簡短乾淨
btn_params = {'font': ("Arial", 12), 'width': 5, 'height': 2}

# 第一列：C, /, *, -
# 使用 lambda 匿名函式來傳遞參數給 button_click
tk.Button(root, text="C", command=button_clear, **btn_params).grid(row=1, column=0, sticky="nsew")
tk.Button(root, text="/", command=lambda: button_click("/"), **btn_params).grid(row=1, column=1, sticky="nsew")
tk.Button(root, text="*", command=lambda: button_click("*"), **btn_params).grid(row=1, column=2, sticky="nsew")
tk.Button(root, text="-", command=lambda: button_click("-"), **btn_params).grid(row=1, column=3, sticky="nsew")

# 第二列：7, 8, 9, + 
# 注意：根據圖片，加號 (+) 比較高，佔了兩列 (rowspan=2)
tk.Button(root, text="7", command=lambda: button_click("7"), **btn_params).grid(row=2, column=0, sticky="nsew")
tk.Button(root, text="8", command=lambda: button_click("8"), **btn_params).grid(row=2, column=1, sticky="nsew")
tk.Button(root, text="9", command=lambda: button_click("9"), **btn_params).grid(row=2, column=2, sticky="nsew")
tk.Button(root, text="+", command=lambda: button_click("+"), **btn_params).grid(row=2, column=3, rowspan=2, sticky="nsew")

# 第三列：4, 5, 6
tk.Button(root, text="4", command=lambda: button_click("4"), **btn_params).grid(row=3, column=0, sticky="nsew")
tk.Button(root, text="5", command=lambda: button_click("5"), **btn_params).grid(row=3, column=1, sticky="nsew")
tk.Button(root, text="6", command=lambda: button_click("6"), **btn_params).grid(row=3, column=2, sticky="nsew")

# 第四列：1, 2, 3, = 
# 注意：根據圖片，等號 (=) 比較高，也佔了兩列 (rowspan=2)
tk.Button(root, text="1", command=lambda: button_click("1"), **btn_params).grid(row=4, column=0, sticky="nsew")
tk.Button(root, text="2", command=lambda: button_click("2"), **btn_params).grid(row=4, column=1, sticky="nsew")
tk.Button(root, text="3", command=lambda: button_click("3"), **btn_params).grid(row=4, column=2, sticky="nsew")
tk.Button(root, text="=", command=button_equal, **btn_params).grid(row=4, column=3, rowspan=2, sticky="nsew")

# 第五列：0, .
# 注意：根據圖片，數字 0 比較寬，佔了兩欄 (columnspan=2)
tk.Button(root, text="0", command=lambda: button_click("0"), **btn_params).grid(row=5, column=0, columnspan=2, sticky="nsew")
tk.Button(root, text=".", command=lambda: button_click("."), **btn_params).grid(row=5, column=2, sticky="nsew")

# 執行主迴圈，讓視窗保持顯示狀態
root.mainloop()