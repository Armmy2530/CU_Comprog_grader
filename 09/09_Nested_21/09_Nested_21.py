def factor(N):
    ans = []
    while N != 1:
        error = True
        for i in range(2,N):
            if(N % i == 0):
                n = 0
                while True:
                    if(N%i == 0):
                        n += 1
                        N //= i
                    else:
                        error = False
                        break
                ans.append([i,n])                
                break
        if(error):
            ans.append([N,1])                
            break
    return ans            
exec(input().strip())
