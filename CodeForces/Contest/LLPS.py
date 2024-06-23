a = input()
ll = [0] * 27 

for char in a:
    ll[ord(char) - 96] += 1
    
for i in range(26, 0, -1):
    if ll[i] > 0:
        for _ in range(ll[i]):
            print(chr(96 + i), end='')
        break