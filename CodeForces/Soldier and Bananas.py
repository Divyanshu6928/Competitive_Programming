k,n,w=map(int,input().split())
pr=0
for i in range(1,w+1):
    pr+=i*k
if(pr>n):
    print(pr-n)
else:
    print(0)