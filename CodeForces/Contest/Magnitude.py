def maximize_c(t, test_cases):
    results = []

    for i in range(t):
        n = test_cases[i][0]
        a = test_cases[i][1]

        c = 0
        negative_sum = 0
        
        for num in a:
            if num >= 0:
                c += num
            else:
                # If adding the negative number keeps c positive or zero, add it
                if c + num >= 0:
                    c += num
                else:
                    # Otherwise, add the absolute value of the negative number
                    c += abs(num)
        
        results.append(c)
    
    return results

# Example usage:
if __name__ == "__main__":
    t = int(input().strip())
    test_cases = []

    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().strip().split()))
        test_cases.append((n, a))
    
    results = maximize_c(t, test_cases)
    for result in results:
        print(result)