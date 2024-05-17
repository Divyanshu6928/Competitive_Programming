t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    c=0
    flag=False
    vowel = ['a','e','i','o','u']
    for i in range(len(s)):
        if s[i] not in vowel:
            c+=1
        else:
            c=0
        
        if c>=4:
            flag=True
        
    if flag:
        print("NO")
    else:
        print("YES")