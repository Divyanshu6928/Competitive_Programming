from typing import List

def find_max_score(n: int, k: int, a: List[int], b: List[int]) -> int:
    # Create a list of tuples (value, index, can_increment)
    elements = [(a[i], i, b[i]) for i in range(n)]
    
    # Sort the elements based on their values
    elements.sort()
    
    # Initialize variables
    max_score = 0
    operations_left = k
    prefix_sum = sum(a)
    
    # Process each element
    for i, (val, idx, can_increment) in enumerate(elements):
        # Calculate the median of the array without the current element
        if i < n // 2:
            median = elements[n // 2][0]
        else:
            median = elements[(n - 1) // 2][0]
        
        # Calculate current score
        current_score = val + median
        max_score = max(max_score, current_score)
        
        # If we can perform operations on this element
        if can_increment:
            # Calculate how many operations we can perform
            operations = min(operations_left, 10**9 - val)
            
            # Update the score
            max_score = max(max_score, val + operations + median)
            
            # Perform the operations
            operations_left -= operations
            
            # If we've used all operations, we're done
            if operations_left == 0:
                break
    
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