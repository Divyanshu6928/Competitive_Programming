MOD = 998244353

def calculate_costs(n, a, b, c):
    # Initialize the result array
    results = [0] * n
    
    for length in range(1, n+1):
        # Initialize DP table for current length
        dp = [[[0] * length for _ in range(length+1)] for _ in range(length+1)]
        
        # Base case: one permutation of length 1
        dp[1][1][0] = a[1] * b[1] * c[0] % MOD
        
        for l in range(2, length+1):
            for prefix_max in range(1, l+1):
                for suffix_max in range(1, l+1):
                    for ascents in range(l):
                        # Transition from previous state
                        dp[prefix_max][suffix_max][ascents] = (dp[prefix_max][suffix_max][ascents] +
                                                               dp[prefix_max-1][suffix_max][ascents] +
                                                               dp[prefix_max][suffix_max-1][ascents] +
                                                               dp[prefix_max][suffix_max][ascents-1]) % MOD
        
        # Sum up all valid permutations for current length
        total_cost = 0
        for x in range(1, length+1):
            for y in range(1, length+1):
                for z in range(length):
                    total_cost = (total_cost + dp[x][y][z]) % MOD
        
        results[length-1] = total_cost
    
    return results

# Input Reading
n = int(input().strip())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
c = list(map(int, input().strip().split()))

# Calculate costs
results = calculate_costs(n, a, b, c)

# Output results
print(' '.join(map(str, results)))
