def c_strength(n, pairs):
    new_array = []
    strengths = []
    
    for i in range(n):
        count, value = pairs[i]
        new_array.extend([value] * count)
        
        strength = 0
        arr = new_array[:]
        while arr:
            strength += 1
            new_arr = []
            for i in range(1, len(arr)):
                if arr[i] == arr[i-1]:
                    new_arr.append(arr[i])
            arr = new_arr
        strengths.append(strength)
    
    return strengths

t = int(input())

for _ in range(t):
    n = int(input())
    
    pairs = []
    for _ in range(n):
        count, value = map(int, input().split())
        pairs.append((count, value))
    
    result = c_strength(n, pairs)
    
    print(*result)
