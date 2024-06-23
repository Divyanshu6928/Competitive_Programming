def find_left_index(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def find_right_index(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def count_in_range(arr, queries):
    arr.sort()
    results = []
    for l, r in queries:
        left_index = find_left_index(arr, l)
        right_index = find_right_index(arr, r)
        results.append(right_index - left_index)
    return results

# Read input
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
queries = [tuple(map(int, input().split())) for _ in range(k)]

# Get the results for all queries
results = count_in_range(arr, queries)

# Print the results
for result in results:
    print(result)
