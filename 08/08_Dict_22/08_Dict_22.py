ice_data = {}
n = int(input())
for i in range(n):
    ice_name, ice_price = input().split()
    ice_data[ice_name] = int(ice_price)
ice_rank = {}
n = int(input())
for i in range(n):
    item_name, item_n = input().split()
    item_n = int(item_n)
    if item_name in ice_data.keys():
        if item_name in ice_rank.keys():
            ice_rank[item_name] += -item_n * ice_data[item_name]
        else:
            ice_rank[item_name] = -item_n * ice_data[item_name]
        
ice_rank_sorted = sorted(ice_rank.items(), key=lambda x:(x[1],x[0]))
if(len(ice_rank_sorted) != 0):
    print(f'Total ice cream sales: {-sum(ice_rank.values()):.1f}')
    most_price = ice_rank_sorted[0][1]
    name_top = []
    for i in ice_rank_sorted:
        if i[1] == most_price:
            name_top.append(i[0])
        else:
            break
    print(f'Top sales: {", ".join(name_top)}')
else:
    print('No ice cream sales')
