months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
x = input()
x = x.split("/")
print(f"{months_list[int(x[1])-1]} {x[0]}, {x[2]}")