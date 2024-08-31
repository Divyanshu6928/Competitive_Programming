def is_prime(n, primes):
    if n < 2:
        return False
    if n in primes:
        return True
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return False
    return True

def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    p = 2
    while (p * p <= max_num):
        if (is_prime[p] == True):
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    primes = []
    for p in range(2, max_num + 1):
        if is_prime[p]:
            primes.append(p)
    return primes

def find_prime_triplet(N):
    if N < 12:  
        return False
    
    max_prime_candidate = int(N**0.5) + 1
    primes = sieve_of_eratosthenes(max_prime_candidate)
    
    for a in primes:
        if a * a >= N:
            break
        for b in primes:
            if b <= a:
                continue
            if a * a + b * b >= N:
                break
            c_square = N - a * a - b * b
            c = int(c_square**0.5)
            if c > b and c * c == c_square and is_prime(c, primes):
                return True
    return False

N = int(input())

if find_prime_triplet(N):
    print("Yes")
else:
    print("No")
