n=int(input())
s=str(n)
for i in range(n+1,900000000):
    year=str(i)
    sety=set(year)
    if(len(year)==len(sety)):
        print(int(i))
        break
    else:
        continue