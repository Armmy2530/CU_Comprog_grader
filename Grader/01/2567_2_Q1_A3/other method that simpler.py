N=int(input())
X=[]
for i in range(N,0,-1) :
    if i%2==0 :
        X+=input().split()
    else :
        X+=input().split()[::-1]
print(X)
X=X[::-1]
print(X)
        
t=[int(e) for e in input().split()]
l=0
A=""

for e in t :
    l+=e
    if l>=len(X) :
        A+="win"
        break
    if X[l-1]!="." :
        l=int(X[l-1][1:])
    if l==len(X) :
        A+="win"
        break
    A+=str(l)+" "
print(A)