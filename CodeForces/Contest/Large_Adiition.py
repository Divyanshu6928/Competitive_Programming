def can_be_sum_of_two_large_integers(x):
    while x > 0:
        digit = x % 10
        if digit < 10 or digit > 18:
            return False
        x //= 10
    return True

def solve():
    t = int(input().strip())
    
    results = []
    
    for _ in range(t):
        x = int(input().strip())
        if can_be_sum_of_two_large_integers(x):
            results.append("YES")
        else:
            results.append("NO")
    
    for result in results:
        print(result)

# Example usage:
solve()
