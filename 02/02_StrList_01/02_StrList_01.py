i = input()

sum1 = 0
for x in range(12):
  sum1 += (13-x) * int(i[x])

n12 = (11 - (sum1 % 11)) % 10 

print(i[0],i[1:5],i[5:10],i[10:12],n12)
