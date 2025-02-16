a = float(input())
L = 0
U = 0

temp_A = a
index = 0
while True:
    temp_A = temp_A // 10
    index += 1
    if(temp_A == 0):
        break
    
U = index
x = (L+U)/ 2
while(abs((10**x)-a) >= 10**(-10) * max(a,10**x)):
    if(10**x > a):
        U = x
    else:
        L = x
    x = (L+U)/ 2
print(round(x,6))
