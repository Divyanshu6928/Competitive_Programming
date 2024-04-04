def fibonacci(N):
        s=2
        a=1
        b=2
        for i in range(3,N+1):
            c=a+b
            a=b
            b=c
            if c<N:
                if c%2==0:
                    s+=c
            else:
                break
        return s


T=int(input())
for i in range(T):
    N=int(input())
    print(fibonacci(N))