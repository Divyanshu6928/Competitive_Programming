n=int(input())
sum,sub=0,0
for i in range(1,n+1):
    if(i%2==0):
        sum+=i
    else:
        sub+=i
print(sum-sub)
