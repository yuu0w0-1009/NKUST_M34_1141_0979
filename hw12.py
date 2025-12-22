data1 = [0]*100 #id
data2 = [0]*100 #name
data3 = [0]*100 #phone
data4 = [0]*100 #birthday

while True:
    data_in = list(map(str,input().split()))
    match(data_in[0]):
        case '*': #end
            break
        case '@': #add
            id = int(data_in[1])
            name = data_in[2]
            phone = (data_in[3])
            birthday = (data_in[4])

            if(data1[id]==1):print("Exist")
            else:
                data1[id] = 1
                data2[id] = name
                data3[id] = phone   
                data4[id] = birthday
        case '#': #del
            id = int(data_in[1])

            if(data1[id]==0):print("None")
            else:
                data1[id] = 0
                data2[id] = 0
                data3[id] = 0
                data4[id] = 0
        case '!': #modify
            id = int(data_in[1])

            if(data1[id]==0):print("None")
            else:
                mode = int(data_in[2])
                match(mode):
                    case 0:data2[id] = data_in[3]
                    case 1:data3[id] = data_in[3]
                    case 2:data4[id] = data_in[3]

        case '$': #find
            id = int(data_in[1])
            
            if(data1[id]==0):print("None")
            else:
                mode = int(data_in[2])
                match(mode):
                    case 0:print(data2[id])
                    case 1:print(data3[id])
                    case 2:print(data4[id])