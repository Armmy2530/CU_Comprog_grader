def make_int_list(x):
    return [int(y) for y in x.split()]
def is_odd(e):
    return e%2 == 1
def odd_list(alist):
    return [data for data in alist if is_odd(data)]
def sum_square(alist):
    return sum([x*x for x in alist])
exec(input().strip())