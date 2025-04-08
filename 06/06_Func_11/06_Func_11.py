data = input().split()
for i,d in enumerate(data):
    data[i] = int(d,2)
print(f"{sum(data):b}")