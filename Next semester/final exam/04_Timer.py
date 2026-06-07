from tkinter import * # 載入 Tkinter 函式庫
from threading import Timer # 載入 Timer 函式庫
root = Tk()        # 建立一個視窗主物件
root.geometry("450x300+0+0") # 設定視窗大小為 450x300 像素，並強制出現在螢幕左上方 (0,0) 位置
root.title("新視窗")     # 設定視窗上方顯示的名稱

# #方法一：利用元件內建的 after() 方法 (非同步單執行緒)
# counter = 0
# def count():
#     global counter
#     counter += 1
#     label.config(text=str(counter))   # 更新標籤文字
#     label.after(1000, count)          # 延遲 1000 毫秒 (1秒) 後，再次遞迴呼叫自己
# label = Label(root, fg="green")
# label.pack()
# count()                               # 啟動計時

# #方法二：利用 threading 多執行緒核心 Timer (支援帶參數傳遞)
# t = None
# counter = 1
# def change_time(a, b):
#     global counter, t
#     counter += 1
#     labelText.set(str(counter))
#     # 每一秒在新執行緒中重複建立並啟動計時器，同時將參數累加傳入
#     t = Timer(1, change_time, [a+1, b+1])
#     print(f"目前參數狀態 A: {a+1}, B: {b+1}")
#     t.start()
# def pause():
#     global t
#     t.cancel()                        # 強制關閉並取消定時器執行緒，避免程式關閉後背後還在跑
#     root.destroy()
# labelText = StringVar()
# labelText.set(str(counter))
# Label(root, textvariable=labelText).pack()
# Button(root, text="安全退出並關閉執行緒", command=pause).pack()
# t = Timer(1, change_time, [1, 2])     # 初始建立：1秒後執行 change_time，傳入引數 [1, 2]
# t.start()                             # 啟動執行緒

root.mainloop()    # 讓視窗持續執行，監聽事件