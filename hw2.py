count = 0
while(1):
    if(count<10):count += 1
    else:break

    result = 0
    #1 = The first man wins the game
    #2 = The second man wins the game
    #3 = A tie

    data = list(map(int,input().split()))
    if (data[0] == data[1]):result=3
    else:
        if(data[0]==1):
            if(data[1]==2):result=2
            elif(data[1]==3):result=1
        elif(data[0]==2):
            if(data[1]==1):result=1
            elif(data[1]==3):result=2
        elif(data[0]==3):
            if(data[1]==1):result=2
            elif(data[1]==2):result=1

    match(result):
        case 1:
            print("The first man wins the game")
        case 2:
            print("The second man wins the game")
        case 3:
            print("A tie")