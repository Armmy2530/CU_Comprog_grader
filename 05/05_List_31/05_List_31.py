user_card = input().split()
operation = input()
num_card = len(user_card)
for i in operation:
    if i == 'C':
        user_card += user_card[0:num_card//2]
        del user_card[0:num_card//2]
    elif i == 'S':
        for i in range(num_card//2):
            user_card.append(user_card[i])
            user_card.append(user_card[i+ num_card//2])
        del user_card[0:len(user_card)//2]
for i in user_card:
    print(i, end=' ')