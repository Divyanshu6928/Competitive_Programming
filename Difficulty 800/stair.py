t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if(a<b and b<c):
        print("STAIR")
    elif(a<b and b>c):
        print("PEAK")
    else:
        print("NONE")