# def can_pay_exact_amount(A, B, C, D, E, F, X):
#     # Iterate through each store
#     for cost in X:
#         # Calculate the remaining amount to pay
#         remaining = cost
        
#         # Use the highest denomination coins first
#         for denom, num_coins in [(500, F), (100, E), (50, D), (10, C), (5, B), (1, A)]:
#             # Calculate the number of coins to use
#             num_to_use = min(remaining // denom, num_coins)
#             remaining -= num_to_use * denom
            
#             # Update the number of coins left
#             if denom == 500:
#                 F -= num_to_use
#             elif denom == 100:
#                 E -= num_to_use
#             elif denom == 50:
#                 D -= num_to_use
#             elif denom == 10:
#                 C -= num_to_use
#             elif denom == 5:
#                 B -= num_to_use
#             else:
#                 A -= num_to_use
                
#             # Check if exact payment can be made
#             if remaining == 0:
#                 break
#         else:
#             return "No"  # Unable to make exact payment
    
#     return "Yes"  # Able to make exact payment at all stores

# # Read input
# A, B, C, D, E, F = map(int, input().split())
# N = int(input())
# X = list(map(int, input().split()))

# # Check if Mr. AtCoder can pay the exact amount at each store
# print(can_pay_exact_amount(A, B, C, D, E, F, X))


from itertools import product

def can_pay_exact_amount(A, B, C, D, E, F, X):
    # Generate all possible combinations of coins for each store
    for cost in X:
        for a, b, c, d, e, f in product(range(A + 1), range(B + 1), range(C + 1), range(D + 1), range(E + 1), range(F + 1)):
            total = a + 5*b + 10*c + 50*d + 100*e + 500*f
            if total >= cost and total - cost <= a + 5*b + 10*c + 50*d + 100*e + 500*f - cost:
                break
        else:
            return "No"  # Unable to make exact payment
    
    return "Yes"  # Able to make exact payment at all stores

# Read input
A, B, C, D, E, F = map(int, input().split())
N = int(input())
X = list(map(int, input().split()))

# Check if Mr. AtCoder can pay the exact amount at each store
print(can_pay_exact_amount(A, B, C, D, E, F, X))
