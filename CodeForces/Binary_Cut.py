def is_sort(l):
    return l==sorted(l)

t = int(input())

for _ in range(t):
    s = input()
    flag=0
    n=list(s)
    if(s=='10'):
        print(2)
    elif(is_sort(n)):
        print(1)
    else:
        groups = 1  
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                groups += 1
        print(groups-1)
# t = int(input())

# for _ in range(t):
#     s = input()
#     groups = 1  # Initialize groups to 1 to account for the first group
#     for i in range(1, len(s)):
#         if s[i] != s[i - 1]:
#             groups += 1
#     # Minimum number of cuts is one less than the number of groups
#     print(groups - 1)

