n = int(input())  
a = []  

for i in range(n):
    a.append(input())

co = {}  

for i in range(n - 1, -1, -1):
    if a[i] not in co:
        print(a[i])  
        co[a[i]] = 1  
    else:
        co[a[i]] += 1      