def read_data():
    dat = []
    R = int(input())
    for r in range(R):
        dat.append([int(e) for e in input().strip().split()])
    return dat
def count_peak(data):
    count = 0
    for i in range(1,len(data) - 1):
        for j in range(1,len(data[0]) - 1):
            points = [data[i-1][j], data[i+1][j], data[i][j+1], data[i][j-1]]
            if(data[i][j] > max(points)):
                count += 1
    return count
exec(input().strip()) # ต้องมีคำสังนี
