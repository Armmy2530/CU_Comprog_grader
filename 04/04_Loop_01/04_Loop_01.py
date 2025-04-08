index = 0
sum1 = 0
while True:
    i = input()
    if(i == 'q'):
        if(index == 0):
            print('No Data')
        else:
            print(round(sum1/index,2))
        break
    else:
        sum1 += float(i)
        index += 1