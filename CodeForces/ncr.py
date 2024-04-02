def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    
n=int(input())
r=int(input())
m=int(input())
ncr=(fact(n)/(fact(r)*fact(n-r))%m)
print(int(ncr))
# print((fact(n))/(fact(r))*(fact(n-r)))