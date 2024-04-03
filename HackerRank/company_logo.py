

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    b=set(s)
    c=[]
    for i in range(len(b)):
       
        for j in range(len(s)):
            if(b[i] == s[j]):
                c+=1
        c[i].append(c)
        
    di=dict(zip(b,c))
    for i in range(len(di)):
        print(di)
    
       
        
