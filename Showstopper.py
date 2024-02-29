n=int(input())
f=0
for i in range(n):
    r=int(input())
    for j in range(1,(r-1)):
        li1=list(map(int,input().split()))
        li2=list(map(int,input().split()))
    temp=li1[i]
    li1[i]=li2[i]
    li2[i]=temp
    maxi=max(li1)
    maxi2=max(li2)
    if(li1[r-1]==li1[i]):
        f+=1
        break
    else:
        f+=0
if(f==1):
    print("Yes")
else:
    print("No")

    