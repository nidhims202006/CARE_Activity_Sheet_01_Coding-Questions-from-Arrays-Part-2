grid = [    [1,1,0],
    [0,1,0],
    [1,0,1] ]
n = len(grid)
m = len(grid[0])
visited = []
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(False)
    visited.append(temp)
groups = []
def d(i, j):
    if i < 0 or j < 0 or i >= n or j >= m:
        return 0

    if visited[i][j] == True or grid[i][j] == 0:
        return 0
    visited[i][j] = True
    count = 1
    count += d(i+1, j)
    count += d(i-1, j)
    count += d(i, j+1)
    count += d(i, j-1)
    return count
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and visited[i][j] == False:
            groups.append(d(i, j))

groups.sort(reverse=True)

print(groups[1])
