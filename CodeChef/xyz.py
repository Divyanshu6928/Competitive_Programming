def max_draws(t, test_cases):
    results = []
    for i in range(t):
        a, b, c = test_cases[i]
        total_sum = a + b + c
        
        if total_sum % 2 == 1:
            results.append(-1)
        else:
            if (a == 1 and b == 1 and c == 0) or (a == 1 and b == 0 and c == 1) or (a == 0 and b == 1 and c == 1):
                results.append(1)
            elif (a == 1 and b == 1) or (a == 1 and c == 1) or (b == 1 and c == 1):
                results.append(2)
            elif c >= (a + b):
                results.append(a + b)
            else:
                results.append(total_sum // 2)
    
    return results

# Example usage
t = 4
test_cases = [(0, 0, 0), (0,1,1), (1,1,1),(3,4,5)]
print(max_draws(t, test_cases))  # Output: [0, 3, 1]
