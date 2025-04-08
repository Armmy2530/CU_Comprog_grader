n = int(input())
ans = []
ans.append(int(n))
while n != 1:
    if n % 2 == 0:
        n = n/2
    else:
        n = 3*n + 1
    ans.append(int(n))

for i in ans[-15:-1]:
    print(i,end="->")
print(ans[-1])