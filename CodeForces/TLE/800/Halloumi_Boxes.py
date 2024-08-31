t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    ar=list(map(int,input().split()))
    if(sorted(ar)==ar or k>1):
        print("YES")
    else:
        print("NO")