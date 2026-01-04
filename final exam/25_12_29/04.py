import time
from random import randint

x = 1
ans = [0]*4

while(1):
    print(f'第 {x} 次 :')
    t = randint(1,5)
    time.sleep(t)
    print("時間到!",end="")
    t1 = time.time()
    d = str(input())
    if(d == ''):
        t2 = time.time()
    ans[x] = t2-t1
    x += 1
    if x > 3:
        break
    time.sleep(3)

print(f'統計結果 : {ans[1]:.3f} {ans[2]:.3f} {ans[3]:.3f}')