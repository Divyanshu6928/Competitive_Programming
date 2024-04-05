def swap_case(s):
    l=[]
    for i in range(len(s)):
        if(s[i].isupper()):
            r=s[i].lower()
            l.append(r)
        elif(s[i].islower()):
            r=s[i].upper()
            l.append(r)
        else:
            l.append(s[i])
            
    return ''.join(l)
    
    


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)