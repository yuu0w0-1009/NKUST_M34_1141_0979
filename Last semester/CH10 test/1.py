# file = open("檔案", "模式") 模式預設為讀檔

x = 0
data_in = [0]*50

# r : 讀取
file_in = open("input.txt","r", encoding="UTF-8")
# w : 新建檔案寫入
file_out = open("output.txt","w",encoding="UTF-8")

# 讀取全部字元
# print(file_in.read())

# 讀取一行,最後面會加上一個 \n
# ex : ['1', ' ', '1', '2', '\n']
# print(list(file_in.readline()))

# 傳回一list ，每一行文字最後面會加上   一個 \n 為一個list的資料項
# ex : ['1 12\n', '3\n', '4']
# print(file_in.readlines())

# 寫入二維list 依據行數
# ex : [[1, 12], [3], [4]]
for i in file_in.readlines():
    data_in[x] = list(map(int,i.split()))
    x += 1
print(data_in)

# file.close()#關檔
file_in.close()
file_out.close()