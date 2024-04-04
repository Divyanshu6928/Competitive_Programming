t = int(input())

for i in range(t):
    d,l,r = map(int, input().strip().split())
    if d<l:
        print("Too Early")
    elif d>r:
        print("Too Late")
    else:
        print("Take second dose now")