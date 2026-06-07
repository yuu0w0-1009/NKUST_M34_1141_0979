from tkinter import * # 載入 Tkinter 函式庫
app = Tk()              # 建立一個視窗主物件
app.geometry("400x150+0+0") # 設定視窗大小為 450x300 像素，並強制出現在螢幕左上方 (0,0) 位置
app.title("新視窗")       # 設定視窗上方顯示的名稱

# # 建立一個橘色帶凹陷效果的左側控制框架
# frame1 = Frame(app, bg="orange", bd=10, relief=SUNKEN)
# frame1.pack(side="left")
# # 將按鈕放入 frame1 中，而不是放入主視窗 app 
# button1 = Button(frame1, text="控制1").pack(side="top")
# button2 = Button(frame1, text="控制2").pack(side="bottom")

# # 建立一個右側格線排版的藍色資訊框架
# frame2 = Frame(app, bg="blue", bd=10, relief=RAISED)
# frame2.pack(side="right")
# button3 = Button(frame2, text="網格1").grid(row=0, column=0)
# button4 = Button(frame2, text="網格2").grid(row=0, column=1)

app.mainloop()            # 讓視窗持續執行，監聽事件