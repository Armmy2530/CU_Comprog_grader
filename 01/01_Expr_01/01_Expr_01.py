import math

n = int(input())

upper = math.sqrt(2*math.pi)*n**(n+0.5)*math.exp(-n+(1/(12*n+1)))
lower = math.sqrt(2*math.pi)*n**(n+0.5)*math.exp(-n+(1/(12*n)))

print(upper)
print(lower)