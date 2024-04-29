# Function to calculate the minimum number of invitations needed
def min_invitations(n, p):
    invitations = [False] * n  # Initialize invitations sent to all friends as False
    count = 0  # Initialize count of invitations sent
    
    for i in range(n):
        if not invitations[i]:  # If an invitation has not been sent to friend i yet
            count += 1  # Increment the count of invitations sent
            friend = i  # Current friend
            while not invitations[friend]:  # Keep sending invitations until we reach a friend who has already received one
                invitations[friend] = True  # Send an invitation to the current friend
                friend = p[friend] - 1  # Send an invitation to the best friend of the current friend
    return count

# Input number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Input number of friends and their best friends
    n = int(input())
    p = list(map(int, input().split()))
    
    # Calculate and output the minimum number of invitations
    print(min_invitations(n, p))
