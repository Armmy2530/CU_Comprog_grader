data = list(input())
for i, d in enumerate(data):
    if(d == '('):
        data[i] = '['
    elif(d == '['):
        data[i] = '('
    elif(d == ')'):
        data[i] = ']'
    elif(d == ']'):
        data[i] = ')'
print(''.join(data))
