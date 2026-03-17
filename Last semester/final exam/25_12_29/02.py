eng = ['0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while(1):
    N = int(input())
    if N<0 or N>26:break

    space = N-1
    char = 1

    for i in range(N):
        for j in range(space):
            print(" ",sep="",end="")

        for j in range(char):
            print(eng[char]," ",sep="",end="")

        print()
        space -= 1
        char += 1