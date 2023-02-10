# Import & Parse Data
with open("day-16.txt", 'r') as file:
    scan = file.readlines()

flows = {}
valves = {}

for line in scan:
    info = line.split(' ')
    valve = info[1]
    flows[valve] = int(info[4].split('=')[1].strip(';'))
    valves[valve] = [t.strip(',\n') for t in info[9:]]


# Functions

#> Dictionary to hold previously calculated pressures to speed up recursion
pressures = {} 

def calculate_pressure(pos, time, opened, part2=False):
    """Recursively calculate pressure released along every path taken from value to value

    Args:
        pos (str): Valve position.
        time (int): Number of minutes to traverse paths.
        opened (frozenset): A frozenset to keep track of which valves have been opened.
        part2 (bool, optional): If part 2 is being solved. Defaults to False.

    Returns:
        int: amount of pressure released along the optimal path
    """
    #> Base Case
    if time == 0:
        if part2:
            #> Run everything again, this time with the elephant (same as part 1, but with 26 minutes)
            return calculate_pressure("AA", 26, opened)
        return 0

    #> Check if the point on the path has been visited before (save computation time)
    if (pos, time, opened, part2) in pressures.keys():
        return pressures[(pos, time, opened, part2)]

    #> Check every path that could be taken and find the maximum pressure that could be released
    pressure = max(calculate_pressure(n, time - 1, opened, part2) for n in valves[pos])

    #> If valved is not open, open it and continue along the path
    if flows[pos] > 0 and pos not in opened:
        #> Have to use frozensets, which are hashable: https://stackoverflow.com/questions/23577724/type-error-unhashable-typeset
        #> Hacky way to append to a frozenset using a set
        opened_to_add = set(opened)
        opened_to_add.add(pos)
        
        pressure = max(
            pressure, 
            ((time - 1) * flows[pos]) + calculate_pressure(pos, time - 1, frozenset(opened_to_add), part2)
        )

    #> If point on the path has not been visted yet, add it to the dictionary (save computation time)
    if (pos, time, opened, part2) not in pressures.keys():
        pressures[(pos, time, opened, part2)] = pressure
    
    return pressure


# Question 1
ans1 = calculate_pressure("AA", 30, frozenset())
print(f"Answer 1: {ans1}")


# Question 2
ans2 = calculate_pressure("AA", 26, frozenset(), part2=True)
print(f"Answer 2: {ans2}")
