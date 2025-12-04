while(1):
    N = int(input())
    if(N<=0)or(N%2==0):break
    win_time = (N+1)/2
    first_win = 0
    secand_win = 0
    while(1):
        if(first_win>=win_time):
            print("The first person wins the game")
            break
        elif(secand_win>=win_time):
            print("The second person wins the game")
            break
        data = list(map(str,input().split()))
        if(data[0]==data[1]):continue
        if(data[0]=='Y'):
            if(data[1]=='M'):secand_win += 1
            elif(data[1]=='O'):first_win += 1
        elif(data[0]=='M'):
            if(data[1]=='Y'):first_win += 1
            elif(data[1]=='O'):secand_win += 1
        elif(data[0]=='O'):
            if(data[1]=='Y'):secand_win += 1
            elif(data[1]=='M'):first_win += 1
