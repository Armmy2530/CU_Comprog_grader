def distance1(x1, y1, x2, y2):
    return ((y2 - y1)**2 + (x2 - x1)**2)**0.5
def distance2(p1, p2):
    return ((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)**0.5
def distance3(p1, p2):
    distance = ((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)**0.5
    return ( distance , p1[2]+p2[2] >= distance)
def perimeter(x):
    distance = 0
    for i in range(len(x)):
        distance += distance2(x[i],x[i+1 if i != len(x)-1 else 0])
    return distance
    
exec(input().strip())