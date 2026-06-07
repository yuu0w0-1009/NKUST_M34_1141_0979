import tkinter as tk
import random

class VocabularyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("tk")
        # 設定視窗大小
        self.root.geometry("250x350")
        
        self.words = []
        self.current_word = ""
        self.score = 0
        
        self.load_words()
        
        self.lbl_english = tk.Label(root, text="英文： ", font=("Arial", 12))
        self.lbl_english.pack(pady=20)
        
        self.lbl_chinese = tk.Label(root, text="中文： ", font=("Arial", 12))
        self.lbl_chinese.pack(pady=20)
        
        self.lbl_score = tk.Label(root, text="答對數目： 0", font=("Arial", 12))
        self.lbl_score.pack(pady=20)
        
        self.entry_answer = tk.Entry(root, font=("Arial", 12), width=18)
        self.entry_answer.pack(pady=10)
        
        self.btn_submit = tk.Button(root, text="確定", command=self.check_answer, font=("Arial", 10))
        self.btn_submit.pack(pady=5)
        
        self.root.bind('<Return>', lambda event: self.check_answer())
        
        self.next_question()

    def load_words(self):
        try:
            with open("words.txt", "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(maxsplit=1) 
                    if len(parts) == 2:
                        self.words.append((parts[0], parts[1]))
        except FileNotFoundError:
            self.words = [
                ("appear", "出現"),
                ("application", "應用；申請書"),
                ("appreciation", "欣賞；感謝"),
                ("approach", "接近；著手處理"),
                ("appropriate", "適當的"),
                ("April", "四月")
            ]

    def mask_word(self, word):
        num_to_mask = int(len(word) * 0.8)
        indices_to_mask = random.sample(range(len(word)), num_to_mask)
        
        masked = list(word)
        for i in indices_to_mask:
            masked[i] = '*'
            
        return "".join(masked)

    def next_question(self):
        if not self.words:
            self.lbl_english.config(text="請檢查 words.txt")
            return
            
        word_pair = random.choice(self.words)
        self.current_word = word_pair[0]
        chinese_hint = word_pair[1]
        
        masked_str = self.mask_word(self.current_word)
        
        self.lbl_english.config(text=f"英文：  {masked_str}")
        self.lbl_chinese.config(text=f"中文：  {chinese_hint}")

    def check_answer(self):
        user_input = self.entry_answer.get().strip()
        
        if user_input == self.current_word:
            self.score += 1
            self.lbl_score.config(text=f"答對數目： {self.score}")
            
        self.entry_answer.delete(0, tk.END)
        self.next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = VocabularyApp(root)
    root.mainloop()