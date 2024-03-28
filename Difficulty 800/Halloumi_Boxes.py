t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    
    box=list(map(int,input().split()))
    if((sorted(box)==box) or k>1):
        print("YES")
    else:
        print("NO")