n_floor = int(input())

sneak_start = []
sneak_dest = []

leader_start = []
leader_dest = []

floor_plans = []
for j in range(n_floor):
    floor_plans.append(input())

width = 0
for j in floor_plans[0]:
    if(j in '.SL'):
        width += 1

finish = width * n_floor
player_pos = 0
start_index = n_floor*width if n_floor%2 == 0 else (n_floor-1)*width+1
direction = n_floor%2 == 1
# print(width,finish,start_index,direction)
# True = Plus 0 1 2 3
# False = Minus 3 2 1 0

for floor_index, floor_plan in enumerate(floor_plans):
    for i,d in enumerate(floor_plan):
        if(d == 'S'):
            sneak_start.append(start_index)
            if i+2 < len(floor_plan):
                if(floor_plan[i+2].isdigit()):
                    dest_no = (floor_plan[i+1:i+3])
                else:
                    dest_no = (floor_plan[i+1])
            else:
                dest_no = (floor_plan[i+1])
            sneak_dest.append(int(dest_no))
            start_index += 1 if direction else -1
        elif(d == 'L'):
            leader_start.append(start_index)
            if i+2 < len(floor_plan):
                if(floor_plan[i+2].isdigit()):
                    dest_no = (floor_plan[i+1:i+3])
                else:
                    dest_no = (floor_plan[i+1])
            else:
                dest_no = (floor_plan[i+1])
                    
            leader_dest.append(int(dest_no))
            start_index += 1 if direction else -1
        elif(d == '.'):
            start_index += 1 if direction else -1
    start_index += -(width+1) if direction else -(width-1)
    direction = not(direction)

user_dice = [int(x) for x in input().split()]
answer = []
for i in user_dice:
    player_pos += i
    if(player_pos >= finish):
        answer.append('win')
        break
    elif(player_pos in leader_start):
        player_pos = leader_dest[leader_start.index(player_pos)]
    elif(player_pos in sneak_start):
        player_pos = sneak_dest[sneak_start.index(player_pos)]
            
    if(player_pos >= finish):
        answer.append('win')
        break
    else:
        answer.append(str(player_pos))

print(" ".join(answer))