s = input()
l="hello"
x = 0
for i in range(len(s)):
    if s[i] == l[x]:
        x+=1
        if x == 5:
            break
if x == 5:
    print('YES')
else:
    print("NO")