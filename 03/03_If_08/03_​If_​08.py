d = int(input())
m = int(input())
y = int(input())

if(m > 11):
    d = d - 4
elif(m > 9):
    d = d - 3
elif(m > 6):
    d = d - 2
elif(m > 4):
    d = d - 1
    
y = y - 543
leap_year = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

print(d + ((m-1) * 31) + ((-2 if leap_year else -3) if m != 1 else 0 ))