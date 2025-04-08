import math
answer = 0
a,b,c= [int(x) for x in input().split()]
if  a<b:
    d=c
    x='B'
    if c != 0:
        while c > 0:
            r = c % 2
            x = str(r) + x
            c = c // 2
    else:
        x =  str(c) + x
    print(d,x)
else:
    if a>b:
        d = int(input())
        if a>c:
            a,b = b,a
            a,c = c,a
            a += 1
            b = b*2
        if b>d:
            b,d =  d,b
            a += 2
            b = b*3
        c = a+2*b
        d = c-3*a
        print(a,b,c,d)
    else:
        e = float(input())
        f = float(input())
        answer = e*((1+(f/(100*a)))**(a*c))
        print(round(answer,2))