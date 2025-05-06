import numpy as np

def toCelsius(f):
    return (f-32)/1.8

def BMI(wh):
    return  wh[:,0] / (wh[:,1]/100)**2 

def distanceTo(p,Points):
    return ((Points[:,0]-p[0])**2 + (Points[:,1]-p[1])**2)**0.5

exec(input().strip())
# print(toCelsius(np.array([32,212])))
# print(BMI(np.array([[60,170],[50,160]])))
# print(distanceTo([0,0],np.array([[3,0],[0,4],[3,4]])))
