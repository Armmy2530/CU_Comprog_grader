user = [int(x) for x in input().split()]
ripple = 0
for i in range(1, len(user)-1):
    if(user[i-1] < user[i] and user[i] > user[i+1]):
        ripple += 1
print(ripple)