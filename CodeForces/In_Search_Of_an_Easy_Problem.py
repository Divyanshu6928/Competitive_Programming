n=int(input())
a=list(map(int,input().split()))
for l in a:
    if(l==1):
        flag=1
        break
    else:
        flag=0
    
if(flag==1):
    print("HARD")
else:
    print("EASY")