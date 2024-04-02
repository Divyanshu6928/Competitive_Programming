def minion_game(s):
    # your code goes here
    kevin = 0
    stuart = 0
    vowels = "AEIOU"
    l = len(s)
    for i in range(l):
        if s[i] in vowels:
            kevin += l-i
        elif s[i] not in vowels:
            stuart += l-i
    
    if kevin > stuart:
        print("Kevin",kevin)
    elif stuart > kevin:
        print("Stuart",stuart)
    else:
        print("Draw")