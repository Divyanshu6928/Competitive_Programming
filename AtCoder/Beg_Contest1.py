n=int(input())
a=list(map(int,input().split()))
flag=0
for i in range(1,len(a)):
    if(a[i]>a[0]):
        print(i+1)
        flag=1
        break
    else:
        flag=0 

if(flag==0):
    print(-1)  