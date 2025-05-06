import numpy as np

def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data 

def report_lower_than_mean(weight,data):
    sum = np.sum(weight * data[:,1:],axis=1)
    avg = np.mean(sum)
    below_avg = data[sum < avg, 0]
    below_avg = np.array(below_avg,str)
    if(len(below_avg) != 0):
        print(", ".join(below_avg))
    else:
        print("None")
    
exec(input().strip())
