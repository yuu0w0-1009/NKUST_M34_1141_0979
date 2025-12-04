count = 0

while(count<10):

    x = list(map(int,input().split()))

    O = x[0]
    d1 = x[1]
    d2 = x[2]
    data1 = []
    result = []

    temp = 0

    match O:
        case 1:
            for temp in range(1,100):
                if(d1%temp==0):
                    data1.append(temp)
            temp = 0
            for temp in range(1,100):
                if((d2%temp==0) and (temp in data1)):
                    print(temp,end=" ")
            print("")
        case 2:
            for temp in range(1,100):
                if(d1*temp>100):break
                else:data1.append(d1*temp)
            temp = 0
            for temp in range(1,100):
                if(d2*temp>100):break
                elif((d2*temp in data1)):result.append(temp*d2)
            temp = 0

            if(len(result)==0):
                print("None",end=" ")
            else:
                for temp in range(0,len(result)):
                    print(result[temp],end=" ")

            print("")

    # print(count)

    count += 1