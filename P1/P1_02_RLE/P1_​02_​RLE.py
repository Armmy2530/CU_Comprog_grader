def str2RLE(x):
    count = 0
    char = x[0]
    result = ""
    for i in x:
        if char == i:
            count += 1
        else:
            result += char + " " + str(count) + " "
            count = 1
        char = i
    result += char + " " + str(count) + " "
    return result

def RLE2str(x):
    x = x.split()
    result = ""
    for i in range(0,len(x),2):
        result += x[i] * int(x[i+1])
    return result

mode = input()
if(mode == "str2RLE"):
    print(str2RLE(input()))
elif(mode == "RLE2str"):
    print(RLE2str(input()))
else:
    print("Error")