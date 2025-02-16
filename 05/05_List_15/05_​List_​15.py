user = {int(x) for x in input().split()}

print(len(user))
num_data = 9 if len(user) > 9 else len(user)-1
print("[",end="")
for i,data in enumerate(user):
    print(data,end="")
    if i == num_data:
        break
    print(", ",end="")
print("]")