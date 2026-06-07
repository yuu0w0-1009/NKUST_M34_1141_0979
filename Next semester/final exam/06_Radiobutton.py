from tkinter import * # 載入 Tkinter 函式庫
root = Tk()                # 建立一個視窗主物件
root.geometry("450x300+0+0") # 設定視窗大小為 450x300 像素，並強制出現在螢幕左上方 (0,0) 位置
root.title("新視窗")       # 設定視窗上方顯示的名稱

# # 建立單選按鈕群組與取得選取值
# v = IntVar()                           # 建立一個共享的整數變數
# v.set(0)                               # 預設選中 value=0 的那個選項
# def show_choice():
#     print("目前使用者選中的項目編號是:", v.get())
# arr = ["電子系", "電機系", "資工系"]
# for i in range(3):
#     Radiobutton(root,
#         variable = v,          # 關鍵點：共享同一個變數
#         value = i,             # 關鍵點：每個選項的真實數值不同
#         text = arr[i],         # 畫面上顯示的文字
#         command = show_choice  # 點擊時即時觸發
#     ).pack()

# # 多個獨立 Radiobutton 群組
# v1 = IntVar(); v1.set(0)               # 第一組專用變數
# v2 = IntVar(); v2.set(0)               # 第二組專用變數
# # 建立第一組 (系所群組)
# for i in range(3):
#     Radiobutton(root, variable=v1, value=i, text="系所選項"+str(i)).pack()
# # 建立第二組 (性別/其他群組)
# for i in range(3):
#     Radiobutton(root, variable=v2, value=i, text="其他群組選項"+str(i)).pack()

# # 單選鈕偽裝成按鈕
# v = IntVar(); v.set(0)
# for i in range(3):
#     Radiobutton(root, 
#         variable=v, 
#         value=i, 
#         indicatoron=0,         # 關閉傳統圓圈指針指示符號
#         text="頁籤 " + str(i)
#     ).pack()

root.mainloop()            # 讓視窗持續執行，監聽事件