def max_profit(N, C, M, markets):
    # Calculate the maximum profit at each town
    max_profit = [0] * (N + 1)

    for i in range(2, N + 1):
        for j in range(1, i):
            cost = C * abs(i - j)
            max_profit[i] = max(max_profit[i], max_profit[j] + markets[i][1] - cost)

    return max_profit[N]

# Read input
N, C, M = map(int, input().split())
markets = [(0, 0)]  # To align with 1-based indexing
for _ in range(M):
    T, P = map(int, input().split())
    markets.append((T, P))

# Calculate and print the answer
print(max_profit(N, C, M, markets))
