t=input()
n,m=map(int,t.split())
a=input()
b=input()
arr=list(map(int,a.split()))
brr=list(map(int,b.split()))
arr.sort()
for i in range(m):
    from bisect import bisect_right
    c=bisect_right(arr,brr[i])
    print(c,end=" ")