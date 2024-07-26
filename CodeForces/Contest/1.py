t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=[]
    if n==1:
        print(0)
        break
    elif n>1:
        for i in range(1,k+1):
            for j in range(1,i+1):
                if(i+j == k):
                    s.append(i)
                    s.append(j)