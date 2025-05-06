import numpy as np

def p(x):
    return 1 / (1+np.exp(-(-3.98+0.1*x[:,0]+0.5*x[:,1])))
   
exec(input().strip())
# print(p(np.array([[100,4.00]])))
# print(p(np.array([[80,2.5],[1,4.0]])))
