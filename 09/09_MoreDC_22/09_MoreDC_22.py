def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return m
def mult_c(c, A):
    return [[x*c for x in y] for y in A]
def mult(A, B):
    ans = []
    for i in range(len(B)):
            
            
exec(input().strip())
