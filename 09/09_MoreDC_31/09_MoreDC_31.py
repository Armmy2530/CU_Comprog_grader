def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a
def is_coprime(a, b, c):
    return gcd(gcd(a,b), gcd(b,c)) == 1
def primitive_Pythagorean_triples(max_len):
    triple = []
    print(int(max_len**0.5))
    for m in range(2,int(max_len**0.5)+1):
        for n in range(1,m):
            if(gcd(m,n)==1 and (m % 2 == 0 or n % 2 == 0)):
                a,b,c = m**2-n**2,2*m*n,m**2+n**2
                if c <= max_len:
                    triple.append(sorted([a,b,c]))
    triple = sorted(triple , key = lambda x : (x[2],x[0]))
    return triple

exec(input().strip()) # ต้องมีคาสั่งนี้ ตรงนี้ ตอนส่งให้ Grader ตรวจ
