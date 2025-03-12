def convex_polygon_area(p):
    a = [p[i][0] * p[i+1 if i < len(p)-1 else 0][1] for i in range(len(p))]
    b = [p[i][1] * p[i+1 if i < len(p)-1 else 0][0] for i in range(len(p))]
    return abs(0.5*(sum(a)-sum(b)))
def is_heterogram(s):
    data = {}
    for j in s.split():
        j = j.lower()
        for i in j:
            if (i in "abcdefghijklmnopqrstuvwxyz"):
                if(i in data.keys()):
                    data[i] += 1
                else:
                    data[i] = 1
                if(data[i] == 2):
                    return False
    return True
def replace_ignorecase(s, a, b):
    ans = ""
    index = 0
    a = a.lower()
    while True:
        s_lower = s.lower()
        index_found = s_lower[index:].find(a)
        if(index_found != -1):
            ans += s[index:index_found+index] + b
        else:
            ans += s[index:]
            break
        index += index_found + len(a)
    return ans

def top3(votes):
    rank = sorted(votes.items(),key = lambda x:(-x[1],x[0]))
    return [i[0] for i in rank[:3]]

for k in range(2):
  exec(input().strip())
