def two(n):
    if(n==1):
        return True
    elif(n==0):
        return False
    else:
        while(n!=1):
            if(n%2!=0):
                return False
            n=n//2
        return True
    
n=int(input())
print(two(n))