t = int(input())
for i in range(t):
    n = int(input())
    if n == 3:
        print(3,2,1)
        continue
    elif n == 4:
        print(3,2,1,4)
        continue
    print(n-1,n-3, end=" ")
    for j in range(n-4,0,-1):
        print(j,end=" ")
    print(n-2,n)    