i = input()

character = ['A','B','C','D','E','F','G','H','I','J']

x1 = int(i[3::7])
x2 = int(i[7::5])

y = str(x1+x2+10000)
y = y[-4:-1]

z = str(int(y[0])+int(y[1])+int(y[2]))

w = int(z[-1])

print(f"{y}{character[w]}")
