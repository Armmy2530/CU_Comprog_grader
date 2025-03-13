def convolute(M, K):
    return sum([sum([M[i][j] * K[i][j] for j in range(len(M[0]))]) for i in range(len(M))])
exec(input().strip()) #ต้องมีบรรทัดนี้เมื่อส่งไป grader
