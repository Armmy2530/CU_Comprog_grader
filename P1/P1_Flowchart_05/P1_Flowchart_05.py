import math
c = input()
if(c == 'S'):
    m = int(input())
    q, r, t, k, n, x, i, p = 1, 0, 1, 1, 3, 3, 0, " "
    while i<m:
        if(4*q + r - t < n*t):
            p = p + str(n)
            i = i + 1
            a = 10*(r - n*t)
            n = ((10*(3*q + r)) // t) - 10*n
            q = 10*q
            r = a
        else:
            a = (2*q + r)*x
            b = (7*q*k + 2 + x*r) // (x*t)
            q = k*q
            t = x*t
            x = x+2
            k = k+1
            n = b
            r = a
    p = p[1] + '.' + p[2:]
    print("pi =",p)
else:
    if(c == 'R'):
        n = int(input())
        p = 0
        for k in range(n+1):
            p += (-3)**(-k) / (2*k + 1)
        p = 12**0.5 * p
        p = round(p,12)
        print('pi =',p)
    else:
        if(c == 'P'):
            p = ((5**0.5 + 6)**0.5 + 7)**0.5
            p = round(p,6)
            print('pi =',p)
        else:
            print('Invalid')