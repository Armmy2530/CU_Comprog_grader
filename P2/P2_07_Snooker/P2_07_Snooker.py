score = [0,0]
c_data={
    "R" : 1,
    "Y" : 2,
    "G" : 3,
    "W" : 4,
    "B" : 5,
    "P" : 6,
    "K" : 7,
    "X" : 0
}

# Phase 1
while True:
    text = input().strip()
    player, player_balls = text[0],text[1:]
    for i in player_balls:
        score[int(player)-1] += c_data[i]
    if player_balls == "Y":
        break
        
# Phase 2
remain_round = 5
while remain_round > 0:
    text = input().strip()
    player, player_balls = text[0],text[1:]
    for i in player_balls:
        score[int(player)-1] += c_data[i]
        remain_round -= 1 if i != "X" else 0
        if i == "K":
            remain_round = 0

print(f"{score[0]} {score[1]}")
if (score[0] == score[1]):
    print("Tie")
elif (score[0] > score[1]):
    print("Player 1 wins")
else:
    print("Player 2 wins")
