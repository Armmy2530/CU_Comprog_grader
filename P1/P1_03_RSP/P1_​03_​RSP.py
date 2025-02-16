win_count = int(input())

p1_score = 0
p2_score = 0

for i in range(win_count*3):
    player_input = input().split()

    if( (player_input[0] == "R" and player_input[1] == "S") or (player_input[0] == "S" and player_input[1] == "P") or (player_input[0] == "P" and player_input[1] == "R")):
        p1_score += 1
    elif( (player_input[1] == "R" and player_input[0] == "S") or (player_input[1] == "S" and player_input[0] == "P") or (player_input[1] == "P" and player_input[0] == "R")):
        p2_score += 1
    
    if(p1_score == win_count or p2_score == win_count):
        break

print(p1_score,p2_score)
if(p1_score == win_count or p2_score == win_count):
    if(p1_score > p2_score):
        print("Player 1 wins")
    elif(p1_score < p2_score):
        print("Player 2 wins")
else:
    print("Tie")