import math

while(1):

    data = list(map(int,input().split()))

    r = 0
    k = data[0]
    d1 = data[1]
    d2 = data[2]
    d3 = data[3]
    if((k<=0)or(d1<=0)or(d2<=0)or(d3<=0)):break

    for x in range(1,k+1):
        r = x*math.lcm(d1,d2,d3) #math.lcm = 最小公倍數
        print(r,end=" ")

    r = math.gcd(d1,d2,d3) #math.gcd = 最大公因数
    print(r,end=" ")

    #找因数
    for i in range(2, min(d1,d2,d3) + 1):
        if (d1%i==0)and(d2%i==0)and(d3%i==0):
            print(i,end=" ")

    print("")