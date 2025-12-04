count = 0

for x in range(1,10):
    for y in range(1,10):
        if(x%2==1):
            if(y==9):print(x," x ",y," = ",x*y,sep="",end="\n")
            else:print(x," x ",y," = ",x*y,sep="",end="\t")

for x in range(1,10):
    for y in range(1,10):
        if(x%2==0)and(y%2==1):
            print(x," x ",y," = ",x*y,sep="",end="\t")
            if(count<8):count += 1
            else:
                count = 0
                print()

for x in range(1,10):
    for y in range(1,10):
        if(x%2==0)and(y%2==0):
            print(x," x ",y," = ",x*y,sep="",end="\t")
            if(count<8):count += 1
            else:
                count = 0
                print()
