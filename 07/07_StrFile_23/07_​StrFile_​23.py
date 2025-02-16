data_path, year = input().split()
year = year[-2:]

ans = []
f = open(data_path)
for x in f:
    stu_y, stu_score = x.split()
    if(stu_y[0:2] == year):
        ans.append(float(stu_score))
        
if(len(ans) != 0):
    print(min(ans),max(ans),sum(ans)/len(ans))
else:
    print("No data")