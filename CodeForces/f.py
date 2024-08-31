def find_max_score(n, k, a, b):
    # Sort the array
    sorted_a = sorted(a)
    median = sorted_a[(n-1)//2]
    
    max_score = 0
    operations_left = k
    
    for i in range(n):
        # Calculate current score
        current_score = a[i] + median
        
        # If we can perform operations on this element
        if b[i] == 1:
            # Calculate how many operations we can perform
            operations = min(operations_left, 10**9 - a[i])
            
            # Update the score
            current_score += operations
        
        max_score = max(max_score, current_score)
    
    return max_score

def solve_test_case():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    result = find_max_score(n, k, a, b)
    print(result)

# Read the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    solve_test_case()