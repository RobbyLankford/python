# Import Data
with open("day-14.txt", 'r') as file:
    rock_path = file.readlines()


# Functions
def parse_input(input):
    """Parse AOC 2022 day 14's input

    Args:
        input (list): the raw input for Day 14 AOC 2022

    Returns:
        set: the cave grid as a set of coordinates
    """
    grid = set()
    
    for line in input:
        points = line.split(" -> ")
        
        previous = None
        for point in points:
            c, r = list(map(int, point.split(",")))
            if previous is not None:
                #> New point is in a different columm
                if c - previous[0] != 0:
                    #> Connect previous row to current row with a line up the columm
                    c_bottom = min(c, previous[0])
                    c_top = max(c, previous[0])
                    
                    #> Add all points from top to bottom of column
                    for i in range(c_bottom, c_top + 1):
                        grid.add((i, r))
                
                #> New point is in a different row
                elif r - previous[1] != 0:
                    #> Connect previous column to current column with a line across the row
                    r_left = min(r, previous[1])
                    r_right = max(r, previous[1])
                    
                    #> Add all points from left to right of row
                    for i in range(r_left, r_right + 1):
                        grid.add((c, i))
            
            #> Parsed point becomes new previous point
            previous = (c, r)
            
    return grid

def drop_sand(grid):
    """Drop grains of sand per instructions for AOC 2022 day 14 (part 1)

    Args:
        grid (set): The output of `parse_input()`

    Returns:
        int: the number of grains of sand for the answer to part 1
    """
    
    #> Highest point that sand can go
    bottom_row = max(g[1] for g in grid)
    
    #> Start dropping units of sand
    units = 0
    
    #> As units of sand continue to drop...
    while True:
        #> Sand always starts dropping from (500, 0)
        sand = (500, 0)
        
        #> A single unit of sand continues to fall...
        while True:
            #> Can sand continue downward?
            if (sand[0], sand[1] + 1) not in grid:
                sand = (sand[0], sand[1] + 1)
            
            #> Can sand go down and to the left?
            elif (sand[0] - 1, sand[1] + 1) not in grid:
                sand = (sand[0] - 1, sand[1] + 1)
            
            #> Can sand go down and to the right?
            elif (sand[0] + 1, sand[1] + 1) not in grid:
                sand = (sand[0] + 1, sand[1] + 1)
            
            #> If cannot move, sand piles up where it is
            else:
                grid.add(sand)
                break
            
            #> Sand at the bottom row has spilled over into the void
            if sand[1] == bottom_row:
                return units
        
        units += 1

def drop_sand2(grid):
    """Drop grains of sand per instructions for AOC 2022 day 14 (part 2)

    Args:
        grid (set): The output of `parse_input()`

    Returns:
        int: the number of grains of sand for the answer to part 2
    """
    
    #> Lowest point that sand can go (there is now a floor two rows below)
    bottom_row = max(g[1] for g in grid) + 1
    
    #> Start dropping units of sand
    units = 0
    
    #> As units of sand continue to drop...
    while True:
        #> Sand always starts dropping from (500, 0)
        sand = (500, 0)
        
        #> A single unit of sand continues to fall...
        while True:
            #> Can sand continue downward?
            if (sand[0], sand[1] + 1) not in grid:
                sand = (sand[0], sand[1] + 1)
            
            #> Can sand go down and to the left?
            elif (sand[0] - 1, sand[1] + 1) not in grid:
                sand = (sand[0] - 1, sand[1] + 1)
            
            #> Can sand go down and to the right?
            elif (sand[0] + 1, sand[1] + 1) not in grid:
                sand = (sand[0] + 1, sand[1] + 1)
            
            #> If cannot move, sand piles up where it is
            else:
                grid.add(sand)
                break
            
            #> Sand at the bottom row is now allowed to pile up there
            if sand[1] == bottom_row:
                grid.add(sand)
                break
        
        units += 1
        
        #> Sand falls until it comes to rest at the top of the pile
        if sand == (500, 0):
            return units


# Question 1
cave = parse_input(rock_path)
ans1 = drop_sand(cave)

print(f"Answer 1: {ans1}")


# Question 2
cave = parse_input(rock_path)
ans2 = drop_sand2(cave)

print(f"Answer 2: {ans2}")