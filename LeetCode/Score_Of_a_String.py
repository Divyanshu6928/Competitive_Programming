s=input()
ct = 0
for i in range(len(s)-1):
    st=abs(ord(s[i])-ord(s[i+1]))
    ct+=st
print(ct)