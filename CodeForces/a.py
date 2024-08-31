x, y, k = map(int, input().split())

if k % 2 != 0:
    print(x, y)
    for i in range(1, k // 2 + 1):
        print(x - i, y - i)
    
    for i in range(1, k // 2 + 1):
        print(x + i, y + i)
else:
    for i in range(1, k // 2 + 1):
        print(x - i, y - i)
    
    for i in range(1, k // 2 + 1):
        print(x + i, y + i)
