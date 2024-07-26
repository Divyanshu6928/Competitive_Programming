def smallest_subsequence(s):
    n = len(s)
    result = []
    start = 0
    
    while len(result) < 2 and start < n:
        min_char = 'z'
        min_index = start
        
        # Find the smallest character, ensuring we leave at least one character
        for i in range(start, n - max(1, len(result))):
            if s[i] < min_char:
                min_char = s[i]
                min_index = i
        
        result.append(min_char)
        start = min_index + 1
    
    return ''.join(result)

# Test the function
s = input().strip()
print(smallest_subsequence(s))