count = 0

while(count < 3):

    inputstr = input()
    z = 0
    data1 = []
    data2 = [0] * 26
    data3 = [0] * 26

    for x in range(0,len(inputstr)):
        data1.append(ord(inputstr[x]))

    for x in range(0,len(data1)):
        for y in range(97,122):
            if(data1[x]==y):
                z = y - 97
                data2[z] += 1

    for x in range(0,len(data1)):
        for y in range(65,90):
            if(data1[x]==y):
                z = y - 65
                data3[z] += 1

    for x in range(0,26):
        if(data2[x]>0):
            print(chr(x+97),end=" ")
            for y in range(0,data2[x]):
                print("*",end="")
            print(end=" ")

    for x in range(0,26):
        if(data3[x]>0):
            print(chr(x+65),end=" ")
            for y in range(0,data3[x]):
                print("*",end="")
            print(end=" ")

    print()

    count += 1