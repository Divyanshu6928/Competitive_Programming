n = int(input())
x, y = map(int, input().split())
u = max(x - 1, y - 1)
v = max(n - x, n - y)
if u <= v:
    ans = "White"  
else:
    ans = "Black"
print()