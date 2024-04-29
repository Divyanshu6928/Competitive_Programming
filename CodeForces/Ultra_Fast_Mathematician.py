n1=input()
n2=input()
l1=list(n1)
l2=list(n2)
s=n1
for i in range(len(l1)):
    if(l1[i]==l2[i]):
        l1[i]='0'
    elif(l1[i]!=l2[i]):
        l1[i]='1'
    else:
        continue

print(''.join(list(l1)))