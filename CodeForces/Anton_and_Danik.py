n=int(input())
s=input()
l=list(s)
a=l.count('A')
d=l.count('D')
if(a>d):
    print("Anton")
elif(a<d):
    print("Danik")
else:
    print("Friendship")