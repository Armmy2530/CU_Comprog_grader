n = int(input())
for i in range(n):
    print(('.'*(n-i-1)) + '*' + (('.' if i != n-1 else '*') *((2*i)-1)) + ('*' if i > 0 else ''))