# Import Data
with open("day-09.txt", "r") as file:
    moves = file.readlines()


# Question 1
hx, hy = 0, 0
tx, ty = 0, 0
movements = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
positions = set((0, 0))

for move in moves:
    direction, spaces = move.split(' ')
    movement = movements[direction]
    
    ## Each *SINGLE SPACE* movement of the Head
    for i in range(int(spaces)):
        ### Move rope head one space in appropriate direction
        hx, hy = hx + movement[0], hy + movement[1]
        
        ### Move rope tail
        
        #### Check if H and T are too far apart
        dx = hx - tx
        dy = hy - ty
        x_too_far = abs(dx) > 1
        y_too_far = abs(dy) > 1
        
        ### If too far apart, move one space in appropriate direction
        if x_too_far or y_too_far:
            if dx != 0:
                tx += (dx / abs(dx))
            if dy != 0:
                ty += (dy / abs(dy))
            positions.add((tx, ty))

## Print Answer
print("Answer 1:", len(positions))


# Question 2
knots = [(0, 0)] * 10
positions = set((0, 0))

for move in moves:
    direction, spaces = move.split(' ')
    movement = movements[direction]
    
    ## Each *SINGLE SPACE* movement of the Head
    for i in range(int(spaces)):
        ### Move rope head one space in appropriate direction
        knots[0] = (knots[0][0] + movement[0], knots[0][1] + movement[1])
        
        ### Move rope tails
        for j in range(1, len(knots)):
            #### Check if H and current T are too far apart
            dx = knots[j-1][0] - knots[j][0]
            dy = knots[j-1][1] - knots[j][1]
            x_too_far = abs(dx) > 1
            y_too_far = abs(dy) > 1
            
            #### If too far apart, move one space in appropriate direction
            if x_too_far or y_too_far:
                x, y = knots[j][0], knots[j][1]
                
                if dx != 0:
                    x += (dx / abs(dx))
                if dy != 0:
                    y += (dy / abs(dy))
                
                knots[j] = (x, y)
        
        #### Add the position of the *LAST* tail
        positions.add(knots[-1])

## Print Answer (TODO (bug): have to subtract 1 to get corrent answer)
print("Answer 2:", len(positions) - 1)