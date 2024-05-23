# cook your dish here
t=int(input())
for _ in range(t):
    d=list(map(int,input().split()))
    s=list(map(int,input().split()))
    if(sum(d)>sum(s)):
        print("Dragon")
    elif(sum(d)<sum(s)):
        print("Sloth")
    else:
        if(d==s):
            print("Tie")
        elif(d[0]>s[0]):
            print("Dragon")
        elif(d[0]<s[0]):
            print("Sloth")
        elif(d[0]==s[0]):
            if(d[1]>s[1]):
                print("Dragon")
            if(d[1]<s[1]):
                print("Sloth")