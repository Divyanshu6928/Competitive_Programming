def four(n):
    if(n==1):
        return True
    elif(n==0):
        return False
    else:
        while(n!=1):
            if(n%4!=0):
                return False
            n=n//4
        return True
    
n=int(input())
print(four(n))