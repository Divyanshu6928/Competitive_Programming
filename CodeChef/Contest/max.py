import sys

def input():
    return sys.stdin.readline().rstrip()


t = int(input().strip())


for _ in range(t):
    n = int(input().strip())  
    
    # list banaya 
    l = list(range(1, n + 1))
    
    print(*l)
    
    mid = (n + 1) // 2
    l = l[mid:] + l[:mid]
    print(*l)
