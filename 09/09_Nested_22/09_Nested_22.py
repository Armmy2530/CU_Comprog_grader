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
    if (len(B[0]) != len(A[0])): 
        B = [[B[j][i] for j in range(len(B))]for i in range(len(B[0]))]
    for i in A:
        temp = []
        for j in B:
            temp.append(sum([x*y for x,y in zip(i,j)]))
        ans.append(temp)
    return ans
            
exec(input().strip())
