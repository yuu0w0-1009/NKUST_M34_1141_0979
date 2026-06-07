from tkinter import * # 載入 Tkinter 函式庫
from tkinter import filedialog # 載入 filedialog 函式庫
root = Tk()                # 建立一個視窗主物件
root.geometry("450x300+0+0") # 設定視窗大小為 450x300 像素，並強制出現在螢幕左上方 (0,0) 位置
root.title("新視窗")       # 設定視窗上方顯示的名稱

# # 下拉選單兩種宣告方式
# # 宣告型式一：直接列出所有選項字串
# v1 = StringVar(root)
# v1.set("電子系")                         # 設定初始被選中值
# om1 = OptionMenu(root, v1, "電子系", "電機系", "資工系")
# om1.pack()

# # 宣告型式二：利用 Python 串列展開語法 * (極度實用，講義第2頁)
# department = ["電子系", "電機系", "資工系", "機械系", "化工系"]
# v2 = StringVar(root)
# v2.set(department[0])
# om2 = OptionMenu(root, v2, *department) # * 號會自動將串列解包為個別的參數傳入
# om2.pack()

# # 即時事件回呼
# def on_select_change(selected_value):
#     print("用戶剛剛選擇切換到了:", selected_value)
# department = ["1a", "2b", "3c", "4d", "5e"]
# v = StringVar(root)
# v.set(department[0])
# om = OptionMenu(root, v, *department, command=on_select_change)
# om.pack()

# # 視窗頂部高階選單列 (Menubar) 標準架構模板
# # 1. 初始化最頂層的方塊總選單列主物件
# menubar = Menu(root)
# # 2. 初始化第一個下拉清單物件 (File 內部選單)
# filemenu = Menu(menubar, tearoff=0) # tearoff=0 可以關閉 Tkinter 預設的選單分離線
# filemenu.add_command(label="Open...", command=lambda: print("開啟檔案..."))
# filemenu.add_command(label="Exit", command=root.quit)
# # 將 File 下拉清單以級聯 (cascade) 方式掛載到總選單列上
# menubar.add_cascade(label="File", menu=filemenu)
# # 3. 初始化第二個下拉清單物件 (Help 內部選單)
# helpmenu = Menu(menubar, tearoff=0)
# helpmenu.add_command(label="About...", command=lambda: print("這是選單程式設計的範例說明"))
# menubar.add_cascade(label="Help", menu=helpmenu)
# # 4. 最重要的一步：將配置好的總選單列物件反向指派給 root 主視窗
# root["menu"] = menubar

# # 開檔函式
# def OpenFile():
#     # 參數說明：initialdir 預設開啟目錄, title 對話框上方名稱, filetypes 過濾檔案格式
#     file_path = filedialog.askopenfilename(
#         initialdir = "C:/",
#         title = "請選擇您的圖片檔案",
#         filetypes = (("jpeg 檔案","*.jpg"), ("全部檔案","*.*"))
#     )
#     if file_path:
#         print("使用者選擇的檔案路徑為：", file_path)
# # 彈出說明訊息的函式
# def About():
#     print("This is a simple example of a menu")
# menu = Menu(root)                # 初始化主選單列主物件
# # 初始化第一個下拉清單物件 (File 內部選單)
# filemenu = Menu(menu, tearoff=0)
# # 新增 Open... 與 Exit 選項至 File 方塊選項中，並綁定對應的函式
# filemenu.add_command(label="Open...", command=OpenFile)
# filemenu.add_command(label="Exit", command=root.quit)
# # 將 File 下拉清單以級聯 (cascade) 方式掛載到總選單列上
# menu.add_cascade(label="File", menu=filemenu)
# # 初始化第二個下拉清單物件 (Help 內部選單)
# helpmenu = Menu(menu, tearoff=0)
# helpmenu.add_command(label="About...", command=About)
# menu.add_cascade(label="Help", menu=helpmenu)
# root["menu"] = menu              # 將配置好的總選單列物件指派給 root 主視窗

root.mainloop()            # 讓視窗持續執行，監聽事件