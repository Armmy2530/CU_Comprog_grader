x = input()
x = str(x[1:-1]).split(",")
x = [float(i) for i in x]
y = input()
y = str(y[1:-1]).split(",")
y = [float(i) for i in y]
print(f"{x} + {y} = {[_x + _y for _x, _y in zip(x, y)]}")
