def left(arr,x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

    return l+1

def right(arr,x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo


n=int(input())
ar=list(map(int,input().split()))
k=int(input())
result=[]
ar.sort()
for _ in range(k):
    a,b=map(int,input().split())
    left_index=left(ar,a)
    right_index=right(ar,b)
    result.append(right_index-left_index)

for results in result:
    print(results,end=" ")
