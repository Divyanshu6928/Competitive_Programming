def  lexicographically(s):
    n = len(s)
    lexi = []
    index = 0
    
    while len(lexi) <= 1 and index < n:
        mc = 'z'
        min_index = index
        
        for i in range(index, n - max(1, len(lexi))):
            if s[i] < mc:
                mc = s[i]
                min_index = i
        
        lexi.append(mc)
        index = min_index + 1
    
    return ''.join(lexi)

s = input().strip()
print(lexicographically(s))
# n=len(s)
# lexi=[]
# index=0
# while len(lexi)>1 and index < n:
#     min_char='z'
#     min_index = index

#     for i in range (index,n-max(1,len(lexi))):
#         if s[i] < min_char:
#                 min_char = s[i]
#                 min_index = i

#         lexi.append(min_char)
#         index=min_index+1
# print(''.join(lexi))