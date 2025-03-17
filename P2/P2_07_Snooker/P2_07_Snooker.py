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
remain_round = 2
remain_ball = 7
while remain_round > 0 and remain_ball > 0:
    text = input()
    player, player_balls = text[0],text[1:]
    for i in player_balls:
        score[int(player)-1] += c_data[i]
    if "X" in player_balls:
        remain_round -= 1
    else:
        remain_balls -= 1

# Phase 2
print(score)
remain_round = 7
while remain_round > 0:
    text = input()
    player, player_balls = text[0],text[1:]
    for i in player_balls:
        score[int(player)-1] += c_data[i]
        remain_round -= 1
    print(player,player_balls,score,remain_round)
print(score)
