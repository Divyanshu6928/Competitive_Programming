def check_conditions(grid):
    m = len(grid)
    n = len(grid[0])

    for i in range(m - 1):
        for j in range(n):
         
            if grid[i][j] != grid[i + 1][j]:
                return False

    for i in range(m):
        for j in range(n - 1):
            
            if grid[i][j] == grid[i][j + 1]:
                return False


    return True


grid = [[1,0,2],[1,0,2]]
print(check_conditions(grid))  
