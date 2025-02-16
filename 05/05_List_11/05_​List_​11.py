x = ["0","1","2","3","4","5","6","7","8","9"]

user = input()

for i in user:
    if i in x:
        x.remove(i)
    
if len(x) == 0:
    print("None")
else:
    if(len(x) == 1):
        print(x[0])
    else:
        for i in x[:-1]:
            print(i,end=",")
        print(x[-1])