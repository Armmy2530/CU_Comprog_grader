def row_number(t, e): # return row number of t containing e (top row is row #0)
    pos = 0
    for i,data in enumerate(t):
        if e in data:
            pos = i
    return pos
def flatten(t): # return a list of ints converted from list of lists of ints t
    data = []
    for i in t:
        data += i
    data.remove(0)
    return data
def inversions(data): # return the number of inversions of list x
    inversion_found = 0
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if(data[i] > data[j]):
                inversion_found += 1
    return inversion_found
def solvable(t): # return True if tiling t (list of lists of ints) is solvable
    zero_pos = row_number(t,0)
    for i,data in enumerate(t):
        if 0 in data:
            zero_pos = i 
    inversions_even = inversions(flatten(t)) % 2 == 0
    if(len(t) % 2 == 1):
        if(inversions_even):
            return True
        else:
            return False  
    else:
        if(inversions_even):
            return zero_pos%2 == 1
        else:
            return zero_pos%2 == 0
# exec(input().strip()) # do not remove this line
print(row_number([[0,8,7],[6,5,4],[3,2,1]], 0)) 
print(flatten([[0,8,7],[6,5,4],[3,2,1]])) #[8, 7, 6, 5, 4, 3, 2, 1]
print(inversions([8,7,6,5,4,3,2,1])) #28
print(solvable([[0,8,7],[6,5,4],[3,2,1]])) #True
