def peaks(x):
    ripple = []
    for i in range(1, len(x)-1):
        if(x[i-1] < x[i] and x[i] > x[i+1]):
            ripple.append(i)
    return ripple
exec(input()) # DON'T remove this line