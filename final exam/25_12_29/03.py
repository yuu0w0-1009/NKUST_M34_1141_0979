import random as rd

ans = rd.sample(range(1, 6), 4)
print(int("".join(map(str, ans))),"(答案)",sep="")

while(1):
    data = list(map(int, str(input())))
    A = 0
    B = 0
    for x in range(4):
        if data[x] == ans[x]:
            A += 1
        elif data[x] in ans:
            B += 1
    if A == 4:
        print("4A0B 恭喜答對")
        break
    else:
        print(A,"A",B,"B",sep="")