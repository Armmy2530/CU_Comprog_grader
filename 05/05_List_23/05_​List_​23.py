num = int(input())
distance = []
for i in range(num):
    x, y = [float(j) for j in input().split()] 
    distance.append([i,x,y,(x**2 + y**2) ** 0.5])
distance.sort(key=lambda x: x[3])
print(f"#{distance[2][0]+1}: ({distance[2][1]}, {distance[2][2]})")