# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    s=0
    
    c=n//9
    r=n%9
    s+=c*45+((r*(r+1))//2)
    
    
    print(s)