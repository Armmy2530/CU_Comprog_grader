user = input().strip()
user = user.lower()
data = {}
for i in user:
    if i in "abcdefghijklmnopqrstuvwhyxz":
        if i in data.keys():
            data[i] -= 1
        else:
            data[i] = -1

ans = sorted(data.items(),key = lambda x:(x[1], x[0]))
for i in ans:
    print(f'{i[0]} -> {i[1]*-1}')
