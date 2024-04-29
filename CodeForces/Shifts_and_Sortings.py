# Function to calculate the minimum total cost
def min_total_cost(s):
    n = len(s)
    cost = 0
    i = 0
    
    while i < n:
        j = i
        while j < n - 1 and s[j] <= s[j + 1]:  # Find increasing subsequence
            j += 1
        
        # Calculate cost of sorting this increasing subsequence
        cost += (j - i + 1) * (j - i + 2) // 2
        
        i = j + 1
    
    return cost

# Input number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Input the binary string
    s = input()
    
    # Calculate and output the minimum total cost
    print(min_total_cost(s))
