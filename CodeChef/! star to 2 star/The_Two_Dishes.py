t=int(input())
for i in range(t):
    n,s=map(int,input().split())
    if(s<=n):
        print(s)
    else:
        print(n-(s-n))