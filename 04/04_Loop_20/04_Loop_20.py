min_l, max_l, min_r, max_r = 0,0,0,0
i = 0
while True:
    user_input = input()
    if(user_input == "Zig-Zag"):
        print(min_l,max_r)
        break
    elif(user_input == "Zag-Zig"):
        print(min_r,max_l)
        break
        
    x = [int(d) for d in user_input.split()]

    if(i == 0):
        min_l, max_l = x[0], x[0]
        min_r, max_r = x[1], x[1]
    else:
        min_l = x[i%2] if min_l > x[i%2] else min_l
        max_l = x[i%2] if max_l < x[i%2] else max_l
        min_r = x[not(i%2)] if min_r > x[not(i%2)] else min_r
        max_r = x[not(i%2)] if max_r < x[not(i%2)] else max_r
    i += 1
