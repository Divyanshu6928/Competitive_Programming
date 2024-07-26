def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_triplet(N):
    if N < 12:  # 2^2 + 3^2 + 5^2 = 38, so N must be at least 12
        return False
    
    for a in range(2, N):
        if is_prime(a):
            for b in range(a+1, N):
                if is_prime(b):
                    c_squared = N - a*a - b*b
                    if c_squared > 0:
                        c = int(c_squared**0.5)
                        if c*c == c_squared and is_prime(c) and c > b:
                            return True
    return False

# Read input
N = int(input())

# Check if a prime triplet exists
if find_prime_triplet(N):
    print("Yes")
else:
    print("No")