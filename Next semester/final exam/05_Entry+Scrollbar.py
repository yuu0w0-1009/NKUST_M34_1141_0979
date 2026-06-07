from tkinter import * # 載入 Tkinter 函式庫
root = Tk()                # 建立一個視窗主物件
root.geometry("450x300+0+0") # 設定視窗大小為 450x300 像素，並強制出現在螢幕左上方 (0,0) 位置
root.title("新視窗")       # 設定視窗上方顯示的名稱

# # 核心概念：Entry 無法直接用 text 參數給予預設值，一定要透過 textvariable 綁定
# e = StringVar()
# entry = Entry(root, textvariable=e)
# e.set("請在此輸入文字...")              # 使用 set() 寫入初始預設文字
# entry.pack()
# # print(entry.get())                    # 方式一：直接從元件本體 get() 讀取內容
# # print(e.get())                        # 方式二：從綁定的字串變數 get() 讀取內容（完全相同）
# # 實用特殊設定
# # entry["state"] = "readonly"           # 設定輸入框為「唯讀狀態」，不可輸入修改
# # entry["show"] = "*"                   # 設定字元遮罩符號，任何輸入自動變 * 號（密碼框專用）

# #Text 多行文本組件基礎
# t = Text(root, height=10, width=40)
# for i in range(5):
#     t.insert("1.0", str(i) + "\t新的一行\n") # 一直從第一列最開頭插入新字串，舊內容會被往下推
# print(t.get("1.0", "1.2"))            # 讀取並列印出第一列的前兩個字元
# print(t.get("1.0", END))              # 讀取並列印出從頭到結尾(END)的所有文字內容
# t.pack()


# #Text+Scrollbar
# s = Scrollbar(root)                    # 1. 建立捲動軸
# t = Text(root, height=5, width=20)     # 2. 建立文字多行區
# s.pack(side=RIGHT, fill=Y)             # 3. 捲動軸放在右側，並且垂直方向填滿
# t.pack(side=LEFT, fill=BOTH, expand=1) # 4. 文字區放在左側，完全填滿剩餘空間
# s.config(command=t.yview)              # 5. 綁定動作：當拉動捲動軸時，改變 Text 的 y 軸視角
# t.config(yscrollcommand=s.set)         # 6. 綁定動作：當在 Text 內滾動滑鼠或換行時，同步更新捲動軸滑塊位置
# long_string = "大量長文本內容..."
# t.insert("1.0", long_string)

# 被綁定的事件函式必須接收一個 event 參數
def check_answer(event):
    user_input = entry.get()
    print(user_input)
    entry.delete(0, END)  # 答對後自動清空輸入框
entry = Entry(root)
entry.pack()
# <Return> 代表鍵盤上的 Enter 鍵
entry.bind("<Return>", check_answer) 

root.mainloop()            # 讓視窗持續執行，監聽事件