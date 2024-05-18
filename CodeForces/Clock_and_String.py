def check_intersection(a, b, c, d):
    # Sort the numbers in clockwise order
    numbers = sorted([a, b, c, d])

    # Check if the numbers form a "Z" or "N" shape
    if (numbers[0] < numbers[1] < numbers[2] and 
        numbers[2] < numbers[3] and 
        (numbers[1] - numbers[0]) * (numbers[3] - numbers[2]) < 0):
        return "YES"
    elif (numbers[0] < numbers[1] and 
          numbers[2] < numbers[3] < numbers[0] and 
          (numbers[1] - numbers[0]) * (numbers[3] - numbers[2]) < 0):
        return "YES"

    # If the numbers don't form a "Z" or "N" shape, the strings don't intersect
    return "NO"

import sys

test_cases = int(sys.stdin.readline())

for _ in range(test_cases):
    a, b, c, d = map(int, sys.stdin.readline().split())
    print(check_intersection(a, b, c, d))