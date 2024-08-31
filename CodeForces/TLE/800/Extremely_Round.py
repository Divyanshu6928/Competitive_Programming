t = int(input())
for _ in range(t):
    n = int(input())
    s = str(n)
    l = len(s)
    c = 0
    
    for i in range(1, 10):
        t = i
        for j in range(l + 1):
            if t <= n:
                c += 1
            t *= 10
    
    print(c)
