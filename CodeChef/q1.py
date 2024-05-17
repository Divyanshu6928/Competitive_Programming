t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    w = 0
    pm = ''
    for move in a:
        if move == 'R':
            if pm != 'P':
                w += 1
                pm = 'P'
            else:
                pm = 'S'
        elif move == 'P':
            if pm != 'S':
                w += 1
                pm = 'S'
            else:
                pm = 'R'
        else:
            if pm != 'R':
                w += 1
                pm = 'R'
            else:
                pm = 'P'
    print(w)