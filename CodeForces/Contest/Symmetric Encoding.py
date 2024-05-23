t = int(input())

for _ in range(t):
    n = int(input())
    si = input()

    r = sorted(set(si))
    s = ""
    for i in range(n):
        index = r.index(si[i])
        s += r[len(r) - 1 - index]

    print(s)
