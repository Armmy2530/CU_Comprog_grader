import numpy as np

def mult_table(nrows, ncols):
    return np.arange(1,ncols+1) * np.arange(1,nrows+1).reshape(nrows,1)
    
exec(input().strip())
# print(mult_table(12,12))
