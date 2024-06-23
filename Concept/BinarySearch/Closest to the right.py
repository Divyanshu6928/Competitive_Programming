n,k=map(int,input().split())
n=list(map(int,input().split()))
k=list(map(int,input().split()))
for i in range(len(k)):
    x=k[i]
    l=-1                  # agar koi bhi naa mile to '-1' return krne ke liye
    r=len(n)
    while(r>l+1):
        m=(l+r)//2
        if(n[m]<x):
            l=m
        else:
            r=m

    print(r+1)