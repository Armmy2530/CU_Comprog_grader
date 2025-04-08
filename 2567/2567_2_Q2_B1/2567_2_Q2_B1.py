#
# 2567_2_Q2_B1: List Arrangement (v2.0)
#
def find_P(D):
    ans = []
    for i in range(len(D)):
        if i % 2 == 1:
            ans.append(D[len(D) - 1 - i])
        else:
            ans.insert(0,D[len(D) - 1 - i])
    return ans
def rearrange(D):
    P = find_P(D)
    ans = []
    pos = 1
    for i in range(len(D)):
        pos += P[i] 
        ans.append(D[(pos-1) % len(D)])
        D.pop((pos-1) % len(D))
    return ans
    
    
exec(input().strip()) # DON’T remove this line
