def read_friends():
    dat = []
    N = int(input())
    for i in range(N):
        dat.append(tuple(input().strip().split()))
    return dat
def count_friends(data, names):
    names.sort()
    ans = []
    for i in names:
        temp = []
        for j in data:
            if i in j:
                j = sorted(j)
                if j not in temp:
                    temp.append(j)
        ans.append(tuple([i,len(temp)]))
    return ans
exec(input().strip())
