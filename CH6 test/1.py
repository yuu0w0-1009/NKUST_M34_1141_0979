import time
t = int(input())
for i in range(t):
    print(t-i, end=" ", flush=True)
    time.sleep(1)