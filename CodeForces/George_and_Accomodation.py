n=int(input())
c=0
for i in range(n):
    p,q=map(int,input().split())
    if(p<q):
        if((q-p)>=2):
            c+=1
        else:
            continue
print(c)