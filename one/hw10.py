#平均值
def get_mean_value(value):
    N = len(value)
    mean_value = 0
    for x in range(0,N):
        mean_value = mean_value + value[x]
    mean_value = int(mean_value/N)
    return mean_value

#中間值
def get_median(value):
    if(len(value)%2==1):N = int((len(value)+1)/2)
    else:N = int(len(value)/2)
    return value[N-1]

#變異數
def get_variance(value):
    N = len(value)
    temp = 0
    mean_value = get_mean_value(value)
    for x in range(0,N):
        temp = temp + pow((value[x]-mean_value),2)
    return int(temp/N)

while(1):
    data = list(map(int,input().split()))
    if data[0] == 0 : break
    else:del data[0] #移除data[0]
    data.sort() #排序
    median = get_median(data)
    variance = get_variance(data)
    print(median,variance)