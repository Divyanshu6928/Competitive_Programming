word=input()

a=65
b=97    
c=0
for i in range(26):
    flag1=False
    flag2=False
    for j in range(len(word)):
        if(ord(word[j])==a):
            flag1=True
        if(ord(word[j])==b):
            flag2=True
        
        if(flag1==True and flag2==True):
            c+=1

    a+=1
    b+=1

print(c)