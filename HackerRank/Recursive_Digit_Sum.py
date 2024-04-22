def sod(newn):
    
    if(newn<10):
        return newn
    
    else:
        return newn%10 + sod(newn//10)

def superDigit(n, k):
    # Write your code here
    num=n*k
    newn=int(num)
    if(newn<10):
        return n
    return superDigit(sod(newn))

print(superDigit("987",4))