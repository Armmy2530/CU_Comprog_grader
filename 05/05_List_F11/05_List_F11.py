def missing_digits(t):
    x = ["0","1","2","3","4","5","6","7","8","9"]
    for i in t:
        if i in x:
            x.remove(i)
    return [int(i) for i in x]
exec(input()) # DON'T remove this line