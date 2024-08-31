t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != a[n - 1]:
        print('YES')
        print(a[n - 1], end=' ')
        for i in range(n - 1):
            print(a[i], end=' ')
        print()
    else:
        print('NO')
