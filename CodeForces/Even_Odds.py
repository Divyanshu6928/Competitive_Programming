n,k=map(int,input().split())
l=[]
for i in range(1,n+1):
    if(i%2!=0):
        l.append(i)

for i in range(1,n+1):
    if(i%2==0):
        l.append(i)

print(l[k-1])