def print_triangle(n):
    for i in range(n):
        print(('.'*(n-i-1)) + '*' + (('.' if i != n-1 else '*') *((2*i)-1)) + ('*' if i > 0 else ''))

exec(input()) # DON'T remove this line