n,k=map(int,input().split())
n=list(map(int,input().split()))
k=list(map(int,input().split()))
for i in range(len(k)):
    x=k[i]
    l,r=0,len(n)-1
    flag=False
    while(l<=r):
        m=(l+r)//2
        if(n[m]==x):
            flag=True
            break
        elif(n[m]<x):
            l=m+1
        else:
            r=m-1
    
    if(flag):
        print("YES")
    else:
        print("NO")
