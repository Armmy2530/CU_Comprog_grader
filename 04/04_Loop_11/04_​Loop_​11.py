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

print(str2RLE(input()))