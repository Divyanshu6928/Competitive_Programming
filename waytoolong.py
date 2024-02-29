# Input
n = int(input())
words = [input() for i in range(n)]

# Process each word
for word in words:
    # Check if the word is too long (length strictly more than 10)
    if len(word) > 10:
        # Abbreviate the word
        abbreviated_word = word[0] + str(len(word) - 2) + word[-1]
        print(abbreviated_word)
    else:
        # Print the original word (not too long)
        print(word)