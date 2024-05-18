import bisect

def minutes_to_reach_point(n, k, a, b, d):
    # Calculate distances between consecutive points
    distances = [0] * (k + 1)
    for i in range(1, k + 1):
        distances[i] = distances[i - 1] + (a[i] - a[i - 1])
    
    # Binary search to find the interval where the car is located at minute t
    def find_interval(t):
        return bisect.bisect_right(b, t)
    
    # Calculate the distance traveled until minute t
    def distance_traveled(t):
        interval = find_interval(t)
        return distances[interval - 1] + (t - b[interval - 1])
    
    # Binary search to find the minute when the car reaches point d
    left, right = 0, b[-1]
    while left < right:
        mid = (left + right) // 2
        if distance_traveled(mid) < d:
            left = mid + 1
        else:
            right = mid
            
    return left

t = int(input())

for _ in range(t):
    n, k, q = map(int, input().split())
    a = [0] + list(map(int, input().split()))  # Add 0 as the starting point
    b = [0] + list(map(int, input().split()))  # Add 0 as the starting time
    
    for _ in range(q):
        d = int(input())
        print(minutes_to_reach_point(n, k, a, b, d))
