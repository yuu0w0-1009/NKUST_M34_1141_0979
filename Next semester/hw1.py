from tkinter import *
import math

root = Tk()
root.title("")

n = int(input(""))

for i in range(n + 1):
    temp = []
    for j in range(i + 1):
        num = math.comb(i, j)
        temp.append(str(num))
    ans = "\t".join(temp)
    Label(root, text=ans).pack()
root.mainloop()