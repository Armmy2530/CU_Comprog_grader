def pattern1(nrows, ncols):
    return [[j+(ncols*i) for j in range(1,ncols+1)] for i in range(0,nrows)]
def pattern2(nrows, ncols):
    return [[i+(nrows*j) for j in range(0,ncols)] for i in range(1,nrows+1)]
def pattern3( N ): 
    ans = []
    c = 1
    for j in range(N):
        temp = [0] * j
        for _ in range(N-j):
            temp.append(c)
            c += 1
        ans.append(temp)
    return ans
def pattern4( N ):
    ans = [[0]*N for _ in range(N)]
    c = 1
    for i in range(N):
        for j in range(i+1,0,-1):
            ans[j-1][i] = c
            c += 1
    return ans
def pattern5( N ): 
    ans = [[0]*N for _ in range(N)]
    c = 1
    for i in range(N):
        for j in range(N-i):
            ans[j][j+i] = c
            c += 1
    return ans
def pattern6( N ): 
    ans = [[0]*N for _ in range(N)]
    flip = False
    c = 1
    for i in range(N):
        for j in range(N-i):
            if flip:
                ans[(N-i-1)-j][N-j-1] = c
            else :
                ans[j][j+i] = c
            c += 1
        flip = not(flip)
    return ans

exec(input().strip())
