data_in = list(map(str,input().split()))
L = int(data_in[0])
token1 = data_in[1]
token2 = data_in[2]
t1_c = 1
t2_c = L-1

for i in range(L):
    for j in range(t1_c):print(token1,end="")
    for k in range(t2_c):print(token2,end="")
    t1_c += 1
    t2_c -= 1
    print()