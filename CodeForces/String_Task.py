li=["a","A","o","O","Y","y","e","E","u","U","i","I"]
s=input()
news= ""
for i in s:
    if(i not in li):
        if(i.isupper()):
            news +='.' + i.lower()
        else:
            news +='.'+ i

print(news)    