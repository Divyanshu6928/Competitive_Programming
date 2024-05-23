# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    b=input()
    if(b.count('1')%2==0):
        print("YES")
    else:
        print("NO")