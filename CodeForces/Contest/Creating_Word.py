t = int(input())
for _ in range(t):
    a, b = input().strip().split()
    na = b[0] + a[1:]
    nb = a[0] + b[1:]
    print(na, nb)
