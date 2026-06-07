from tkinter import * # 載入 Tkinter 函式庫
root = Tk()                # 建立一個視窗主物件
root.geometry("450x300+0+0") # 設定視窗大小為 450x300 像素，並強制出現在螢幕左上方 (0,0) 位置
root.title("新視窗")       # 設定視窗上方顯示的名稱

# #按鈕基本創建語法
# # rowspan 與 columnspan 參數可讓按鈕跨越多個橫列或直欄
# btn = Button(root, text="click!", bd=1, width=12, height=2).grid(row=0, column=0, rowspan=1, columnspan=2)
# btn2 = Button(root, text="click!2", bd=1, width=5, height=2).grid(row=0, column=2)
# btn3 = Button(root, text="click!3", bd=1, width=5, height=2).grid(row=1, column=0)
# btn4 = Button(root, text="click!4", bd=1, width=5, height=2).grid(row=1, column=1)

# # 1. 綁定基本無參數事件命令
# def b1_function():
#     print("使用者按下了 YES!")
# Button(root, text="YES!", command=b1_function).pack(side="left")

# # 2. 按鈕文字動態即時顯示 (使用 StringVar)
# def changeText():
#     if b["text"] == "text":
#         v.set("change")        # 變動字串變數設為 change
#     else:
#         v.set("text")          # 變動字串變數設為 text
# v = StringVar()                # 宣告一個 Tkinter 專用動態字串變數
# b = Button(root, textvariable=v, command=changeText)
# v.set("text")                  # 初始文字設為 text
# b.pack()

# # 3. 動態改變另一個按鈕的狀態 (config 方法應用)
# e = StringVar()                # 變動文字變數，用來即時連動按鈕2的文字
# e.set("可按")                   # 預設按鈕2顯示的文字為「可按」
# count = 0                      # 整數變數，當作狀態計數器（切換 0 或 1）
# def click():
#     global count               # 使用全域的 count 整數變數
#     if count == 0:
#         Button2.config(state="disabled")  # config可以用於動態修改元件的屬性
#         e.set("不可按")
#         count += 1
#     else:
#         Button2.config(state="active")
#         e.set("可按")
#         count = 0
# # 建立負責觸發狀態改變的控制按鈕
# Button1 = Button(root, text="change", command=click)
# Button1.pack()

# # 建立被動受控制狀態與文字的按鈕
# Button2 = Button(root, textvariable=e)
# Button2.pack()
# # 元件點擊後立即自行消失
# def hide_me(event):
#     event.widget.pack_forget() # 如果是用 pack 排版，使用 pack_forget() 擦除
#     # event.widget.grid_forget() # 如果是用 grid 排版，則使用 grid_forget() 
# b1 = Button(root, text="點我消失")
# b1.bind("<Button-1>", hide_me) # 綁定滑鼠左鍵點擊事件 (<Button-1>)
# b1.pack()

# # 正確的單一按鈕帶參數傳遞寫法
# def b_function(myinput):
#     print("您輸入的是:", myinput)
# Button(root, text="YES!", command=lambda: b_function(1)).pack(side="left")
# Button(root, text="NO!", command=lambda: b_function(2)).pack(side="right")

# # 正確的多按鈕帶參數傳遞寫法+毀視窗內的所有元件
# def b_function(r,c):
#     print(f"您按下了第 {r} 列，第 {c} 欄的按鈕")
# def clear_all():
#     for widget in root.winfo_children():
#         widget.destroy()
# for b in range(9):
#     myrow = int(b / 3)
#     mycol = b % 3
#     # 關鍵點：x=myrow, y=mycol 會在按鈕建立時將當前數值保存下來
#     Button(root, text=b, command=lambda x=myrow, y=mycol: b_function(x, y), width=5, height=2).grid(row=myrow, column=mycol)
# button_clear = Button(root, text="清除全部", command=clear_all, width=15, height=2).grid(row=3, column=0, columnspan=3)

# Button(root, text='隨著視窗自動放大填滿的按鈕', bg='green').pack(expand=1, fill=BOTH)

root.mainloop()            # 讓視窗持續執行，監聽事件