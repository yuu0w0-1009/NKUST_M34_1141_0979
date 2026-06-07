import tkinter as tk
import os

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("tk")
        
        # 資料儲存變數
        self.data = []           # 用來存放所有讀取到的資料清單
        self.current_index = 0   # 紀錄目前顯示的是第幾筆資料
        self.file_path = "data.txt"
        
        # UI 綁定的文字變數 (搭配 Entry 與 Radiobutton 使用)
        self.id_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.gender_var = tk.StringVar(value="男") # 預設為男
        self.dept_var = tk.StringVar()
        self.addr_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        
        self.setup_ui()
        self.load_data()
        
    def setup_ui(self):
        # 建立欄位標籤與輸入框
        labels = ["學號：", "姓名：", "", "系所：", "地址：", "電話："]
        
        # 學號 [cite: 4, 7]
        tk.Label(self.root, text="學號：").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.id_var).grid(row=0, column=1, sticky="w", padx=5, pady=5)
        
        # 姓名 [cite: 4, 7]
        tk.Label(self.root, text="姓名：").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.name_var).grid(row=1, column=1, sticky="w", padx=5, pady=5)
        
        # 性別 (使用 Radiobutton) [cite: 4, 6]
        gender_frame = tk.Frame(self.root)
        gender_frame.grid(row=2, column=1, sticky="w")
        tk.Radiobutton(gender_frame, text="男", variable=self.gender_var, value="男").pack(side="left", padx=5)
        tk.Radiobutton(gender_frame, text="女", variable=self.gender_var, value="女").pack(side="left", padx=5)
        
        # 系所 [cite: 4, 7]
        tk.Label(self.root, text="系所：").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.dept_var).grid(row=3, column=1, sticky="w", padx=5, pady=5)
        
        # 地址 [cite: 4, 7]
        tk.Label(self.root, text="地址：").grid(row=4, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.addr_var).grid(row=4, column=1, sticky="w", padx=5, pady=5)
        
        # 電話 [cite: 4, 7]
        tk.Label(self.root, text="電話：").grid(row=5, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(self.root, textvariable=self.phone_var).grid(row=5, column=1, sticky="w", padx=5, pady=5)
        
        # 建立底部按鈕區塊 [cite: 8, 17]
        btn_frame = tk.Frame(self.root)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=10)
        
        tk.Button(btn_frame, text="<<", width=5, command=self.prev_record).pack(side="left", padx=5)
        tk.Button(btn_frame, text="更新", width=5, command=self.update_record).pack(side="left", padx=5)
        tk.Button(btn_frame, text="刪除", width=5, command=self.delete_record).pack(side="left", padx=5)
        tk.Button(btn_frame, text="新增", width=5, command=self.add_record).pack(side="left", padx=5)
        tk.Button(btn_frame, text=">>", width=5, command=self.next_record).pack(side="left", padx=5)

    def load_data(self):
        """讀取 txt 檔案資料 """
        self.data = []
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split() # 預設以空白切割字串
                    if len(parts) >= 6:
                        self.data.append(parts)
        
        # 程式一開始顯示第一筆資料 [cite: 5, 13]
        if self.data:
            self.show_record(0)

    def save_data(self):
        """將記憶體中的資料寫回 txt 檔案"""
        with open(self.file_path, "w", encoding="utf-8") as file:
            for row in self.data:
                file.write(" ".join(row) + "\n")

    def show_record(self, index):
        """將指定 index 的資料顯示在畫面上"""
        if not self.data:  # 如果資料表是空的
            self.clear_entries()
            return
            
        # 防止 index 越界
        if index < 0:
            index = 0
        elif index >= len(self.data):
            index = len(self.data) - 1
            
        self.current_index = index
        row = self.data[index]
        
        # 設定畫面變數
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.gender_var.set(row[2])
        self.dept_var.set(row[3])
        self.addr_var.set(row[4])
        self.phone_var.set(row[5])

    def clear_entries(self):
        """清空畫面欄位"""
        self.id_var.set("")
        self.name_var.set("")
        self.gender_var.set("男")
        self.dept_var.set("")
        self.addr_var.set("")
        self.phone_var.set("")

    def prev_record(self):
        """上一筆 (<<) [cite: 8]"""
        if self.data and self.current_index > 0:
            self.show_record(self.current_index - 1)

    def next_record(self):
        """下一筆 (>>) [cite: 8]"""
        if self.data and self.current_index < len(self.data) - 1:
            self.show_record(self.current_index + 1)

    def add_record(self):
        """新增按鈕：清空畫面，準備讓使用者輸入新資料 """
        self.clear_entries()
        # 將 index 設定為資料長度，代表準備要在最後面新增一筆
        self.current_index = len(self.data)

    def update_record(self):
        """更新按鈕：儲存修改後的資料，或儲存新增的資料 [cite: 20, 26]"""
        # 收集畫面上輸入的資料
        new_row = [
            self.id_var.get(), self.name_var.get(), self.gender_var.get(),
            self.dept_var.get(), self.addr_var.get(), self.phone_var.get()
        ]
        
        # 簡單防呆：如果不填學號就不動作
        if not new_row[0]: return 

        # 判斷是「修改現有資料」還是「新增資料」
        if self.current_index >= len(self.data):
            self.data.append(new_row)  # 新增資料
        else:
            self.data[self.current_index] = new_row  # 修改現有資料
            
        self.save_data() # 同步寫入 txt [cite: 20]

    def delete_record(self):
        """刪除按鈕：刪除當前資料，並跳到下一筆 """
        if not self.data or self.current_index >= len(self.data):
            return
            
        self.data.pop(self.current_index) # 從清單中移除
        self.save_data() # 同步寫入 txt 
        
        # 刪除後顯示下一筆 (如果已經是最後一筆，則退回顯示新的最後一筆)
        if self.current_index >= len(self.data):
            self.current_index = len(self.data) - 1
            
        self.show_record(self.current_index)

# 主程式進入點
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()