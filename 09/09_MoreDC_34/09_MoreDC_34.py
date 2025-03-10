def pattern1(nrows, ncols):
    return [[j+(4*i) for j in range(1,ncols+1)] for i in range(0,nrows)]
def pattern2(nrows, ncols):
    return [[i+(nrows*j) for j in range(0,ncols)] for i in range(1,nrows+1)]
def pattern3( N ): # N  0
    ans = []
    c = 1
    for j in range(N):
        temp = [0] * j
        for _ in range(N-j):
            temp.append(c)
            c += 1
        ans.append(temp)
    return ans
def pattern4( N ): # N  0
    pass
def pattern5( N ): # N  0
    pass
def pattern6( N ): # N  0
    pass

exec(input().strip())

# print(pattern1(3,4)) #[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(pattern2(3,4)) #[[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
# print(pattern3(100))