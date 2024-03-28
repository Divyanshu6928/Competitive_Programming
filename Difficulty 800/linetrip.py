t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    gas=list(map(int,input().split()))
    if(n>1):
        print(x-n)
    else:
        print(gas[0])