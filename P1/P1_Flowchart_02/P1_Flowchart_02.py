n, k = [int(x) for x in input().split()]
if(n % 2 == 1):
    sum_a, sum_b, sum_c, m = 0, 0, 0, 0
    while(m < k):
        a, b, c = [int(x) for x in input().split()]
        if(a == b):
            if(a == c):
                if(a+b > k):
                    sum_a += 1
                    sum_b += 2
                    sum_c -= 3
                else:
                    sum_a -= 3
                    sum_b -= 2
                    sum_c += 1
            else:
                sum_a += 2
                sum_b -= 3
        m += 1
    else:
        print(sum_a,sum_b,sum_c)
else:
    s, t = [int(x) for x in input().split()]
    x = s
    y = t
    if (s>t):
        x=s-t
    else:
        if(s<t):
            y = 2*(t-s)
    if(x+y > k):
        temp_x = x
        x = y
        y = temp_x
        x = y + s**2
    print(x,y)