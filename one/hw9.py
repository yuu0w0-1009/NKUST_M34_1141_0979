import datetime

# 計算格式化日期
def check_t(y,m,d,nday):
    date = datetime.date(y,m,d) + datetime.timedelta(days=nday)
    return [date.strftime("%Y"),date.strftime("%B"),date.strftime("%A"),date.strftime("%d")]
# y , m , w , d

while(1):
    try:
        # 輸入
        x = list(map(str,input().split()))
        date_1 = list(map(int,x[0].split("/")))

        N = int(x[1])

        # 輸出1
        date_2 = check_t(date_1[0],date_1[1],date_1[2],0)
        print("The day of the week on ",date_2[1]," ",date_2[3],", ",date_2[0]," is ",date_2[2],sep="")

        # 輸出2
        date_2 = check_t(date_1[0],date_1[1],date_1[2],N)
        if(N>=0):
            print("The date after ",N," days is ",date_2[1]," ",date_2[3],", ",date_2[0],sep="")
        else:
            print("The date before ",abs(N)," days is ",date_2[1]," ",date_2[3],", ",date_2[0],sep="")

    # 輸入錯誤的日期
    except ValueError:break