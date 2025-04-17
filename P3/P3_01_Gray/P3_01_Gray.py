n_bit = input()
max_n = input()

error = [False,False]
try:
    n_bit = int(n_bit)
    if(n_bit < 0):
        error[0] = True
except:
    error[0] = True

try:
    max_n = int(max_n)
    if(max_n < 0):
        error[1] = True
except:
    error[1] = True

def gray_code(n):
    ans = ['0','1']
    new_ans = []
    for i in range(n-1):
        for j in ans:
            new_ans.append('0'+j)
        for j in ans[::-1]:
            new_ans.append('1'+j)
        ans = new_ans.copy()
        new_ans = []
    return ans
if(error == [True,True]):
    print('Invalid n and k')
elif(error == [True,False]):
    print('Invalid n')
elif(error == [False,True]):
    print('Invalid k')
else:
    data = gray_code(n_bit)
    for i in range(1,max_n):
        print(str(i)+"-"*(n_bit+1-len(str(i))),end='')
    print(str(max_n)+"-"*(n_bit-len(str(max_n))),end='')
    print()
    for i in range((len(data) // max_n) + (1 if len(data) % 10 != 0 else 0)):
        print(",".join(data[i*max_n:i*max_n + max_n]))
