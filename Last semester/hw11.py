while(1):
    data = list(map(int,input().split()))
    result = []
    if(data[0]<=0 or data[1]<=1 or data[1]>10):break

    while(1):
        if(data[0]==0):break
        a = data[0]//data[1]
        b = data[0]%data[1]
        data[0] = a
        result.append(b)

    result.reverse()
    
    for x in range(len(result)):print(result[x],end="")

    print()