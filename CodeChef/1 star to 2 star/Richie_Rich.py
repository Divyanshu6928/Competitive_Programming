t=int(input())
for i in range(t):
    a,b,x=map(int,input().split())
    c=b-a
    k=c//x
    if c%x==0:
        print(k)
    else:
        print(k+1)