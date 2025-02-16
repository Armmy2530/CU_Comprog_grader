num = int(input())
x = []
LastAppend = True
for i in range(num):
    y = int(input())
    if(LastAppend):
        x.append(y)
    else:
        x.insert(0,y)
    LastAppend = not(LastAppend)

user = [int(x) for x in input().split()]
if len(user) != 0:
    for i in user:
        if(LastAppend):
            x.append(i)
        else:
            x.insert(0,i)
        LastAppend = not(LastAppend)
    
while True:
    user = int(input())
    if(user == -1):
        break
    else:
        if(LastAppend):
            x.append(user)
        else:
            x.insert(0,user)
        LastAppend = not(LastAppend)

print(x)