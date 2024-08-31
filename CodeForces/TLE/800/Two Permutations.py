t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    if(a+b<=n-2 or (a==n and b==n)):
        print("Yes")
    else:
        print("No")