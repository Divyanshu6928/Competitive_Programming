n, k = map(int, input().split())
res=((n+k-1)//k)*k
if res > n :
    print(res)
else:
    print(res+k)