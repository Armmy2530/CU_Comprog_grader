N = int(input())
data = {}
for _ in range(N):
    name, nickname = input().split()
    data[name] = nickname
    data[nickname] = name  # Store reverse mapping

print(data)
M = int(input())
for _ in range(M):
    user = input()
    if user in data:
        print(data[user])
    else:
        print('Not found')
