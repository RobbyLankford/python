# Import Data
with open("day-12.txt", "r") as file:
    heightmap = file.read().splitlines()


# Question 1

## Iterate through data to put into a grid
rows = len(heightmap) - 1
cols = len(heightmap[0]) - 1
grid = {}
queue = []
visited = set()

for i, row in enumerate(heightmap):
    for j, char in enumerate(row):
        if char == 'S':
            grid[(i, j)] = 0
            queue.append((i, j, 0))
        elif char == 'E':
            grid[(i, j)] = 25
            target = (i, j)
        else:
            grid[(i, j)] = ord(char) - ord('a')

## Search the grid using BFS
while len(queue) > 0:
    i, j, steps = queue.pop(0)
    
    ### Find the target value
    if (i, j) == target:
        fewest = steps
        break
    
    ### Ignore if we have already visisted
    if (i, j) in visited:
        continue
    
    visited.add((i, j))

    ### Handle the literal edge cases of the grid
    if i == 0 and j == 0:
        checks = [(1, 0), (0, 1)]
    elif i == 0 and j == cols:
        checks = [(1, 0), (0, -1)]
    elif i == rows and j == 0:
        checks = [(-1, 0), (0, 1)]
    elif i == rows and j == cols:
        checks = [(-1, 0), (0, -1)]
    elif i == 0:
        checks = [(0, -1), (0, 1), (1, 0)]
    elif j == 0:
        checks = [(1, 0), (-1, 0), (0, 1)]
    elif i == rows:
        checks = [(0, -1), (0, 1), (-1, 0)]
    elif j == cols:
        checks = [(1, 0), (-1, 0), (0, -1)]
    else:
        checks = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    ### Check places we can visit from current position
    for r, c in checks:
        if grid[(i + r, j + c)] <= grid[(i, j)] + 1:
            queue.append((i + r, j + c, steps + 1))

## Print Answer
print("Answer 1:", fewest)


# Question 2

## Iterate through data to put into a grid
grid = {}
queue = []
visited = set()

for i, row in enumerate(heightmap):
    for j, char in enumerate(row):
        if char == 'S' or char == 'a':
            grid[(i, j)] = 0
            queue.append((i, j, 0))
        elif char == 'E':
            grid[(i, j)] = 25
            target = (i, j)
        else:
            grid[(i, j)] = ord(char) - ord('a')

## Search the grid using BFS
while len(queue) > 0:
    i, j, steps = queue.pop(0)
    
    ### Find the target value
    if (i, j) == target:
        fewest = steps
        break
    
    ### Ignore if we have already visisted
    if (i, j) in visited:
        continue
    
    visited.add((i, j))
    
    ### Handle the literal edge cases of the grid
    if i == 0 and j == 0:
        checks = [(1, 0), (0, 1)]
    elif i == 0 and j == cols:
        checks = [(1, 0), (0, -1)]
    elif i == rows and j == 0:
        checks = [(-1, 0), (0, 1)]
    elif i == rows and j == cols:
        checks = [(-1, 0), (0, -1)]
    elif i == 0:
        checks = [(0, -1), (0, 1), (1, 0)]
    elif j == 0:
        checks = [(1, 0), (-1, 0), (0, 1)]
    elif i == rows:
        checks = [(0, -1), (0, 1), (-1, 0)]
    elif j == cols:
        checks = [(1, 0), (-1, 0), (0, -1)]
    else:
        checks = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    ### Check places we can visit from current position
    for r, c in checks:
        if grid[(i + r, j + c)] <= grid[(i, j)] + 1:
            queue.append((i + r, j + c, steps + 1))

## Print Answer
print("Answer 2:", fewest)