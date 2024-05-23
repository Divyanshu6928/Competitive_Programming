t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=""
    for i in range(n):
        if (a[i] <= k):
            s += "1"
            k -= a[i]
        else:
            s += '0'
            
    print(s)