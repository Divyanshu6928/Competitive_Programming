n, k = map(int, input().split())
scores = list(map(int, input().split()))

# Initialize the count of participants advancing to the next round
count_advancing = 0

# Iterate through the scores to count participants who advance
for score in scores:
    # Check if the participant has a positive score and meets the k-th place condition
    if score > 0 and score >= scores[k - 1]:
        count_advancing += 1
    # If the score is 0 or less, break the loop (scores are non-increasing)
    else:
        break

# Output the result
print(count_advancing)

# 8 5
# 10 9 8 7 7 7 5 5

# 6

# n, k = map(int, input().split()):

# input().split(): Takes a line of space-separated input from the user.
# map(int, ...): Converts each element obtained from the split into an integer.
# n, k = ...: Unpacks the first two elements (assuming they are integers) into the variables n and k.


# scores = list(map(int, input().split())):

# input().split(): Takes another line of space-separated input from the user.
# map(int, ...): Converts each element obtained from the split into an integer.
# list(...) converts the map object into a list.
# scores = ...: Assigns the resulting list to the variable scores.