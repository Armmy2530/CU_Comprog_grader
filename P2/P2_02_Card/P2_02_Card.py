def charToValue(src):
    if(src == "A"):
        return 1
    elif(src == "J"):
        return 11
    elif(src == "Q"):
        return 12
    elif(src == "K"):
        return 13
    elif(src == "T"):
        return 10
    else:
        return int(src)
def symbolToValue(src):
    if (src == 'C'):
        return 1
    elif(src == 'D'):
        return 2
    elif(src == "H"):
        return 3
    else:
        return 4

player_hand = input().strip()
player_hand = [player_hand[i:i+2] for i in range(0,len(player_hand),2)]
text = ""
for i in range(len(player_hand)-1):
    if(player_hand[i][0] != player_hand[i+1][0]):
        num = charToValue(player_hand[i][0]) - charToValue(player_hand[i+1][0])
        if num > 0:
            text += "+" + str(num)
        else:
            text += str(num)
    else:
        num = symbolToValue(player_hand[i][1]) - symbolToValue(player_hand[i+1][1])
        if num > 0:
            text += "+" + str(num)
        else:
            text += str(num)
print(text)
