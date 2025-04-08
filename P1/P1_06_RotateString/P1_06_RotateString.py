oparation = input()
numData = int(input())

error_flag = False 
data = []
for i in range(numData):
    data.append(list(input()))
    if(i != 0 and len(data[i]) != len(data[i-1])):
       error_flag = True

if(error_flag):
    print("Invalid size")
elif(oparation == "90"):
    for y in range(len(data[0])):
        for x in range(len(data)):
            print(data[len(data)-1-x][y],end='')
        print()
elif(oparation == "180"):
    for y in range(len(data)):
        for x in range(len(data[0])):
            print(data[len(data)-1-y][len(data[0])-1-x],end='')
        print()
else:
    for y in range(len(data)):
        for x in range(len(data[0])):
            print(data[y][len(data[0])-1-x],end='')
        print()