def key(s):
    s=s.lower()
    c=0
    for i in range(len(s)-1):
        if(s[i]!=s[i+1]):
            c+=1
    return c

s=input("Enter the string: ")
print(key(s))