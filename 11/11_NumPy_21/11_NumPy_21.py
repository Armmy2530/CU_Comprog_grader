import numpy as np

def sum_2_rows(M):
    return M[::2]+M[1::2]

def sum_left_right(M):
    return M[:,:M.shape[1]//2] + M[:,M.shape[1]//2:]

def sum_upper_lower(M):
    return M[:M.shape[0]//2] + M[M.shape[0]//2:]

def sum_4_quadrants(M):
    M1,M2 = M[:M.shape[0]//2,:M.shape[1]//2], M[:M.shape[0]//2,M.shape[1]//2:]
    M3,M4 = M[M.shape[0]//2:,:M.shape[1]//2], M[M.shape[0]//2:,M.shape[1]//2:]
    return M1+M2+M3+M4

def sum_4_cells(M):
    M1,M2 = M[::2 ,::2] ,M[::2 ,1::2]
    M3,M4 = M[1::2,::2] ,M[1::2,1::2]
    return M1+M2+M3+M4

def count_leap_years(years):
    years -= 543
    return np.sum(((years % 4 == 0) & (years%100 != 0)) | (years % 400 == 0))

exec(input().strip())
# print(sum_2_rows(np.arange(36).reshape(6,6)))
# # [[ 6  8 10 12 14 16]
# # [30 32 34 36 38 40]
# # [54 56 58 60 62 64]]
# print(sum_left_right(np.arange(36).reshape(6,6)))
# # [[ 3  5  7]
# # [15 17 19]
# # [27 29 31]
# # [39 41 43]
# # [51 53 55]
# # [63 65 67]]
# print(sum_upper_lower(np.arange(36).reshape(6,6)))
# # [[18 20 22 24 26 28]
# # [30 32 34 36 38 40]
# # [42 44 46 48 50 52]]
# print(sum_4_quadrants(np.arange(36).reshape(6,6)))
# # [[42 46 50]
# # [66 70 74]
# # [90 94 98]]
# print(sum_4_cells(np.arange(36).reshape(6,6)))
# # [[ 14  22  30]
# # [ 62  70  78]
# # [110 118 126]]
# print(count_leap_years(np.array([2543,2559,2560])))
# # 2
