x = 0
data = [""]*50
char = ['零','一','二','三','四','五','六','七','八','九']

file_in = open("input.txt","r", encoding="UTF-8")
file_out = open("output.txt","w",encoding="UTF-8")

for i in file_in.readlines():
    data[x] = list(map(int, i.split()))       #[[12345],[6789]]
    data[x] = list(map(int, str(data[x][0]))) #[[1,2,3,4,5],[6,7,8,9]]
    data[x].reverse()                         #翻轉
    x += 1

for i in range(x):
    for j in range(len(data[i])):
        if(data[i][j] % 2 == 1):
            print(char[data[i][j]],end="")
            print(char[data[i][j]],file=file_out,end="")
    print()
    print(file=file_out)

file_in.close()
file_out.close()