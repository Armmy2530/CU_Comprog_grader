def convex_polygon_area(p):
    return 0.5*(sum([p[i][0]*p[i+1][1] for i in range(len(p)-1)])-sum([p[i][1]*p[i+1][0] for i in range(len(p)-1)]))
    pass
def is_heterogram(s):
    data = {}
    for i in s:
        if (i != " "):
            if(i in data.keys()):
                data[i] += 1
            else:
                data[i] = 1
            if(data[i] == 2):
                return False
    return True
def replace_ignorecase(s, a, b):
    pass
def top3(votes):
    pass

# for k in range(2):
#     exec(input().strip())

print(convex_polygon_area([[0,0], [0,3], [4,0]]))
print(convex_polygon_area([[0,0], [4,0], [0,3]]))
# 6.0
# 6.0
print(is_heterogram("The big dwarf only jumps."))
print(is_heterogram("Java"))
# True
# False
# print(replace_ignorecase("Python is hard", "Hard", "easy"))
# print(replace_ignorecase("AAabaAA", "Aa", "Aaa"))
# Python is easy
# AaaabAaaA
# v = {"A": 8888, "B": 6666, "C": 7777, "X":6666}
# print(top3(v))
# ['A', 'C', 'B']
