player_data = input()
frame_position = int(input())

frame_index = 0
score = [0] * 10

def toScore(char):
    if(char == 'X'):
        return 10
    elif(char == '/'):
        return 11
    else:
        return int(char)

i = 0
while(frame_index < 10):
    if(player_data[i] == 'X'):
        score[frame_index] += 10
        if(player_data[i+2] == '/'):
            score[frame_index] += 10
        else:
            score[frame_index] += toScore(player_data[i+1]) + toScore(player_data[i+2])
        i += 1
    else:
        if(player_data[i+1] == '/'):
            score[frame_index] += 10 + toScore(player_data[i+2])
        else:
            score[frame_index] += toScore(player_data[i]) + toScore(player_data[i+1])
        i += 2
    frame_index += 1
                           
if(frame_position >= 1 and frame_position <= 11):
    print(score[frame_position-1])
else:
    print(sum(score))
