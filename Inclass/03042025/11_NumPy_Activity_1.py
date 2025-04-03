import numpy as np
def f1(M, c):
    # M: a 2-D numpy array
    # c: float
    return M*c
def f2(U, V):
    # U and V: 1-D numpy arrays of equal size
    return np.sum(U*V)
def f3(M):
    # M: a 2-D numpy array
    return M.T
def f4(x, y, dx, dy, k, R):
    # x, y, dx, dy: 1-D numpy arrays of all equal size
    # k, R: float
    neighbors = [(x[i]-x[k])**2 + (y[i]-y[k])**2 <= R**2
                for i in range(len(x))]
    sx = sy = 0
    sx = np.sum(neighbors * dx)
    sy = np.sum(neighbors * dy)
    t = np.arctan2(sy, sx)
    return np.cos(t), np.sin(t)
#----- DON'T modify any of the following lines -----
for k in range(int(input())):
    exec(input().strip())
