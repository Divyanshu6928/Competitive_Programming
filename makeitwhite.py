n=int(input())
for i in range(1,n):
    a=int(input())
    s=input()
    for j in range(a):
        if(s[j]=="B"):
            s.replace("B","W")
            