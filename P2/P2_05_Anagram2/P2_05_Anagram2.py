def charCount(src):
    data ={}
    for i in src:
        if(i in "abcdefghijklmnopqrstuvwxyz-=_"):
            if (i in data.keys()):
                data[i] += 1
            else:
                data[i] = 1
    return data

def intersect_find(data1,data2):
    intersect = {}
    for i in data1.keys():
        for j in data2.keys():
            if(i == j):
                intersect[i] = min(data1[i],data2[i])
    return intersect
  
def Special_find(data):
    for i in data.keys():
        if i in "=-*_":
            return True
    return False

def Remove_nonIntersect(data,intersect_data):
    remove = {}
    int_sec = intersect_data.keys()
    for i in data.keys():
        if not(i in int_sec):
            remove[i] = data[i]
        else:
            if(data[i] != intersect_data[i]):
                remove[i] = data[i] - intersect_data[i]
    return sorted(remove.items(),key=lambda x:x[0])

text1 = input().strip()
text2 = input().strip()

data1 = (charCount(text1.lower()))
data2 = (charCount(text2.lower()))

intersect = intersect_find(data1, data2)
symbol = "'s"
print(text1)
if(Special_find(data1)):
    print(" - None")
else:
    remove_char = Remove_nonIntersect(data1,intersect)
    if (len(remove_char) == 0):
        print(" - None")
    else:
        for i in remove_char:
            print(f" - remove {i[1]} {i[0] + (symbol if i[1] > 1 else '')}")

print(text2)
if(Special_find(data2)):
    print(" - None")
else:
    remove_char = Remove_nonIntersect(data2,intersect)
    if (len(remove_char) == 0):
        print(" - None")
    else:
        for i in remove_char:
            print(f" - remove {i[1]} {i[0] + (symbol if i[1] > 1 else '')}")
