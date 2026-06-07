from tkinter import * # 載入 Tkinter 函式庫
root = Tk()                # 建立一個視窗主物件
root.geometry("450x300+0+0") # 設定視窗大小為 450x300 像素，並強制出現在螢幕左上方 (0,0) 位置
root.title("新視窗")       # 設定視窗上方顯示的名稱

# # 範例一：透過 for 迴圈與 pack 快速建立 5 個垂直排列的 Label
# for i in range(5):
#     Label(root, text="pack" + str(i)).pack()

# # 範例二：設定不同的方向對齊排列
# loc = [RIGHT, BOTTOM, LEFT, TOP]
# for i in range(4):
#     Label(root, text="pack" + str(i)).pack(side=loc[i])

# # 範例三：設定各種方向的內外顏色及間距
# Label(root, text="pack1", bg="yellow").pack(side=LEFT, padx=0)
# Label(root, text="pack2", bg="green").pack(expand=0, side=LEFT, padx=10) # 水平差 10 單位
# Label(root, text="pack3", bg="red").pack(side=BOTTOM, padx=30)          # 水平差 30 單位
# Label(root, text="pack4", bg="white").pack(side=BOTTOM, pady=30)        # 垂直差 30 單位

# # 語法基礎
# Label(root, text="Label1").place(x=0, y=0)

# # 綜合範例：利用 for 迴圈每隔 80 像素橫向擺放一個標籤
# for i in range(5):
#     Label(root, text="Label" + str(i)).place(x=80 * i)

# #如同 Excel 表格，如果不指定橫列與直欄，預設會從 row=0, column=0 開始擺放。
# lb0 = Label(root, text="Label0")
# lb1 = Label(root, text="Label1")
# lb2 = Label(root, text="Label2")

# lb0.grid()                   # 預設位置：row=0, column=0
# lb1.grid(row=0, column=1)    # 右側：row=0, column=1
# lb2.grid(row=1, column=0)    # 下方：row=1, column=0

# # grid + for 
# x = 65 # ASCII 碼表中，A 的十進位值為 65
# for i in range(5):
#     for j in range(5):
#         Label(root, text=chr(x)).grid(row=i, column=j)
#         x += 1 # 每次迴圈結束後，將 x 的值加 1，以便顯示下一個字母

# label = Label(root, text="welcome to KUAS", bg="yellow", anchor="s", justify="left", font=("arial", 20, "italic")).pack()
# # 設定字型為 arial、大小 20 像素、斜體 (italic) 效果
# # 效果可用：normal, bold, italic, underline, overstrike

# # 多行長文字自動換行設定
# Label(root, text="歡迎來到這門進階視窗程式設計課程", 
#     width=10, height=10, 
#     wraplength=60,     # 設定每隔 60 個單位寬度自動強制換行
#     justify="left",   # 多行文字靠左對齊
#     anchor="s"         # 整塊文字區對齊標籤底部
# ).pack()

#載入外部圖片
# logo = PhotoImage(file="C:/KUAS.gif")            # 載入圖片檔案
# Label(root, image=logo).pack(side="right")       # 將圖片塞入標籤並靠右排列
# Label(root, text="校徽說明").pack(side="left")

root.mainloop()            # 讓視窗持續執行，監聽事件