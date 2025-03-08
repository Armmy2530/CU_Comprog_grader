n = int(input())
data = {}
for _ in range(n):
    f_name, s_name, phone = input().split()
    data[f_name+" "+s_name] = phone
    data[phone] = f_name+" "+s_name
n = int(input())
for _ in range(n):
    user = input()
    if(user in data.keys()):
        print(f'{user} --> {data[user]}')
    else:
        print(f'{user} --> Not found')
