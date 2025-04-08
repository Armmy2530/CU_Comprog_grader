def RLE(x):
    if(len(x) == 0):
        return []
    count = 0
    char = x[0]
    result = []
    for i in x:
        if char == i:
            count += 1
        else:
            result.append([char,count])
            count = 1
        char = i
    result.append([char,count])
    return result

exec(input())