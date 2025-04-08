import math
x = input()
x = x.split(',')
a = int(x[0] + x[1] + x[2]) - int(x[0]+x[1])
b = 10**(len(x[1]) + len(x[2])) - 10**len(x[1])
gcb_val = math.gcd(a,b)
print(f'{a// gcb_val} / {b // gcb_val}')