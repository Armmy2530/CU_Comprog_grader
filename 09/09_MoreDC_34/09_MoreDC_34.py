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

# print(pattern1(3,4))# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(pattern2(3,4))# [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
# print(pattern3(4))  # [[1, 2, 3, 4], [0, 5, 6, 7], [0, 0, 8, 9], [0, 0, 0, 10]]
# print(pattern4(4))  # [[1, 3, 6, 10], [0, 2, 5, 9], [0, 0, 4, 8], [0, 0, 0, 7]]
# print(pattern5(4))  # [[1, 5, 8, 10], [0, 2, 6, 9], [0, 0, 3, 7], [0, 0, 0, 4]]
# print(pattern6(4))  # [[1, 7, 8, 10], [0, 2, 6, 9], [0, 0, 3, 5], [0, 0, 0, 4]]
# print(pattern4(5))  # [[1, 3, 6, 10], [0, 2, 5, 9], [0, 0, 4, 8], [0, 0, 0, 7]]
# print(pattern5(5))  # [[1, 5, 8, 10], [0, 2, 6, 9], [0, 0, 3, 7], [0, 0, 0, 4]]
