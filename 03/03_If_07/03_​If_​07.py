value = input()

if(len(value) > 10):
    print(f"{int(value[0:-9])+1 if int(value[-9]) >= 5 else value[0:-9]}B")
elif(len(value) == 10):
    print(f"{value[0]}.{int(value[1])+1 if int(value[2]) >= 5 else value[1]}B")
elif(len(value) > 7):
    print(f"{int(value[0:-6])+1 if int(value[-6]) >= 5 else value[0:-6]}M")
elif(len(value) == 7):
    print(f"{value[0]}.{int(value[1])+1 if int(value[2]) >= 5 else value[1]}M")
elif(len(value) > 4):
    print(f"{int(value[0:-3])+1 if int(value[-3]) >= 5 else value[0:-3]}K")
elif(len(value) == 4):
    print(f"{value[0]}.{int(value[1])+1 if int(value[2]) >= 5 else value[1]}K")
else:
    print(value)