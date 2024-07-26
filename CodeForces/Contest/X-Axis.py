# Reading input
t = int(input())
for _ in range(t):
    x1,x2,x3=map(int,input().split())
    p=[x1,x2,x3]
    p.sort()
    a=p[1]
    f_a=abs(a - p[0]) + abs(a - p[1]) + abs(a - p[2])
    print(f_a)