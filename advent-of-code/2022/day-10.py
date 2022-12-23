# Import Data
with open("day-10.txt", "r") as file:
    instructions = file.readlines()

# Process Data

## Variables
cycle = 0
x = 1
strength = 0
pixels = {}

## For each instruction...
for instruction in instructions:
    
    ### noop takes 1 cycle, addx takes 2 cycles
    if instruction.startswith("noop"):
        num_cycles = 1
    else:
        num_cycles = 2
    
    for _ in range(num_cycles):
        ### Each row is 40 pixels wide and there are only 6 rows
        row = cycle // 40
        col = cycle % 40
        
        cycle += 1
        
        ### If the 3-pixel-wide sprite is on the column, it is lit (#)
        if (x - 1) <= col <= (x + 1):
            pixels[(row, col)] = "#"
        
        ### Otherwise, it is dark (.)
        else:
            pixels[(row, col)] = "."
        
        ### Find signal strength on cycle 20, 60, 100, 140, 180, and 220
        if (((cycle - 20) % 40) == 0):
            strength += (cycle * x)
    
    ### addx increments X register by v
    if (instruction.startswith("addx")):
            v = int(instruction.split(' ')[1])
            x += v

# Question 1
print("Answer 1:", strength)

# Question 2
for i in range(6):
    for j in range(40):
        print(pixels[(i, j)], end='')
    print()