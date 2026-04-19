from tkinter import *

text = []
ans = 0

def c_c():
    Label(root,text = "                                      ",font=("",12)).grid(row = 0,column = 0,columnspan= 4)
    global text
    text = []
    Label(root,text = str(0),font=("",12)).grid(row = 0,column = 0,columnspan= 4)

def dis():
    global aaa
    aaa = "".join(text)
    Label(root,text = aaa,font=("",12)).grid(row = 0,column = 0,columnspan= 4)

def c_div():
    global text
    text.append("/")
    dis()

def c_mul():
    global text
    text.append("*")
    dis()

def c_sub():
    global text
    text.append("-")
    dis()

def c_add():
    global text
    text.append("+")
    dis()

def c_0():
    global text
    text.append("0")
    dis()

def c_1():
    global text
    text.append("1")
    dis()

def c_2():
    global text
    text.append("2")
    dis()

def c_3():
    global text
    text.append("3")
    dis()

def c_4():
    global text
    text.append("4")
    dis()

def c_5():
    global text
    text.append("5")
    dis()

def c_6():
    global text
    text.append("6")
    dis()

def c_7():
    global text
    text.append("7")
    dis()

def c_8():
    global text
    text.append("8")
    dis()

def c_9():
    global text
    text.append("9")
    dis()

def c_dot():
    global text
    text.append(".")
    dis()

def c_cul():
    Label(root,text = "                                      ",font=("",12)).grid(row = 0,column = 0,columnspan= 4)
    global text
    global temp
    global ans
    temp = "".join(text)
    ans = eval(temp)
    Label(root,text = ans,font=("",12)).grid(row = 0,column = 0,columnspan= 4)

root = Tk()

Label(root,text = ans,font=("",12)).grid(row = 0,column = 0,columnspan= 4)
Button(root, text =  "C", width = 5,height = 2, bd=2, command=c_c).grid(row = 1,column = 0)
Button(root, text =  "/", width = 5,height = 2, bd=2, command=c_div).grid(row = 1,column = 1)
Button(root, text =  "*", width = 5,height = 2, bd=2, command=c_mul).grid(row = 1,column = 2)
Button(root, text =  "-", width = 5,height = 2, bd=2, command=c_sub).grid(row = 1,column = 3)
Button(root, text =  "7", width = 5,height = 2, bd=2, command=c_7).grid(row = 2,column = 0)
Button(root, text =  "8", width = 5,height = 2, bd=2, command=c_8).grid(row = 2,column = 1)
Button(root, text =  "9", width = 5,height = 2, bd=2, command=c_9).grid(row = 2,column = 2)
Button(root, text =  "+", width = 5,height = 4, bd=2, command=c_add).grid(row = 2,column = 3,rowspan= 2,sticky="ns")
Button(root, text =  "4", width = 5,height = 2, bd=2, command=c_4).grid(row = 3,column = 0)
Button(root, text =  "5", width = 5,height = 2, bd=2, command=c_5).grid(row = 3,column = 1)
Button(root, text =  "6", width = 5,height = 2, bd=2, command=c_6).grid(row = 3,column = 2)
Button(root, text =  "1", width = 5,height = 2, bd=2, command=c_1).grid(row = 4,column = 0)
Button(root, text =  "2", width = 5,height = 2, bd=2, command=c_2).grid(row = 4,column = 1)
Button(root, text =  "3", width = 5,height = 2, bd=2, command=c_3).grid(row = 4,column = 2)
Button(root, text =  "=", width = 5,height = 4, bd=2, command=c_cul).grid(row = 4,column = 3,rowspan= 2,sticky="ns")
Button(root, text =  "0", width = 12,height = 2, bd=2, command=c_0).grid(row = 5,column = 0,columnspan= 2,sticky="ns")
Button(root, text =  ".", width = 5,height = 2, bd=2, command=c_dot).grid(row = 5,column = 2)



root.mainloop()