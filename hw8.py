while(1):
    L = int(input())
    if(L<=0):break
    token = list(map(str,input().split()))
    size = 2 * L - 1
    for r in range(size):
        for c in range(size):
            dist = max(abs(r - L + 1),abs(c - L + 1))
            print(token[dist%3],end=" ")
        print()