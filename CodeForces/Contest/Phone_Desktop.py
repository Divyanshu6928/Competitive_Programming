import math

def min_screens_needed(t, cases):
    results = []
    for case in cases:
        x, y = case
        total_cells = x + y * 4
        screens_needed = math.ceil(total_cells / 15)
        results.append(screens_needed)
    return results

# Reading input
t = int(input().strip())
cases = [tuple(map(int, input().strip().split())) for _ in range(t)]

# Calculating results
results = min_screens_needed(t, cases)

# Printing results
for result in results:
    print(result)
