data = {}

for _ in range(int(input())):
    name,user_data = input().split()
    user_data = user_data.split(',')
    data[name] = set(user_data)

while True:
    ops = input()
    if(ops == 'q'):
        break
    name1, name2 = ops.split()
    sport1, sport2 = data[name1],data[name2]
    result_sport = sport1.intersection(sport2)
    print(sorted(list(result_sport)))
