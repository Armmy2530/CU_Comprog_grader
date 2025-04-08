
#
# 2567_2_Q2_A3: Snake & Ladder (flipped version)
#

n = int(input())

map_data = []
for i in range(n):
    text = input().split()
    if i % 2 == 1:
        text = text[::-1]
    map_data += text

player_move = [int(x) for x in input().split()]

player_pos = 0
player_data = []
for i in player_move:
    player_pos += i
    if(player_pos >= len(map_data)):
        player_data.append('win')
        break
    if(map_data[player_pos-1] != '.'):
        player_pos = int(map_data[player_pos-1][1:])
    if(player_pos >= len(map_data)):
        player_data.append('win')
        break
    player_data.append(str(player_pos))

print(" ".join(player_data))
