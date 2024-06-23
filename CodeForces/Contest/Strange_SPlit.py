t=int(input())
for _ in range(t):
    n=int(input())
    ar=list(map(int,input().split()))
    results = []
    colors = ['R'] * n
    colors[0] = 'B'
    colors[-1] = 'R'
    if n >= 3:
                
        for i in range(1, n-1):
            colors[i] = 'B'
        
        results.append("YES")
        results.append("".join(colors))
    else:
        print("NO")

    for result in results:
        print(result)
        