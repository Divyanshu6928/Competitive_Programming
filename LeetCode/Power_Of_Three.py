def three(n):
    if(n==1):
        return True
    elif(n==0):
        return False
    else:
        while(n!=1):
            if(n%3!=0):
                return False
            n=n//3
        return True
    
n=int(input())
print(three(n))