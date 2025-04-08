number = int(input())

min_l, max_l, min_r, max_r = 0,0,0,0
for i in range(number):
    x = [int(d) for d in input().split()]
    if(i == 0):
        min_l, max_l = x[0], x[0]
        min_r, max_r = x[1], x[1]
    else:
        min_l = x[i%2] if min_l > x[i%2] else min_l
        max_l = x[i%2] if max_l < x[i%2] else max_l
        min_r = x[not(i%2)] if min_r > x[not(i%2)] else min_r
        max_r = x[not(i%2)] if max_r < x[not(i%2)] else max_r

mode = input()
if(mode == "Zig-Zag"):
    print(min_l,max_r)
else:
    print(min_r,max_l)