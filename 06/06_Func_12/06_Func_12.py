def is_prime(n):
     if n <= 1:
         return False
     for k in range(2,int(n**0.5)+1):
        if n%k == 0:
             return False
     return True
def next_prime(N):
    while True:
        N += 1
        if(is_prime(N)):
            return N
def next_twin_prime(N):
    prime_1 = next_prime(N)
    while True:
        prime_2 = next_prime(prime_1)
        if(prime_2 - prime_1 == 2):
            return(prime_1, prime_2)
        prime_1 = prime_2

exec(input().strip())