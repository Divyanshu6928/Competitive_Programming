def checkerboard(n):
    board = ""
    for i in range(1 * n):
        if i % 4 < 2:
            board += "#"
        else:
            board += "."
        if i % n == n - 1:
            board += "\n"
    return board

print(checkerboard(4))