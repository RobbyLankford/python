# Import Data
with open("day-15.txt", 'r') as file:
    lines = file.readlines()


# Functions
def distance(x1, y1, x2, y2):
    """Calculate Manhattan Distance
    
    Args:
        x1 (int): the first X coordinate
        y1 (int): the first Y coordinate
        x2 (int): the second X coordinate
        y2 (int): the second Y coordinate
    
    Returns:
        int: the Manhattan Distance between (x1, y1) and (x2, y2)
    """
    return abs(x1 - x2) + abs(y1 - y2)

def check_dist(x, y, sensors):
    """Check if a single point could contain the distress beacon

    Args:
        x (int): the (potential) X coordinate of the distress beacon
        y (int): the (potential) Y coordinate of the distress beacon
        sensors (set): the (x, y) coordinates of all sensors from the puzzle input
    
    Returns:
        bool: True if the beacon at (x, y) is the distress signal, False otherwise
    """

    #> If at least one sensor is located where it could detect the beacon, flag it as True
    for sx, sy, d in sensors:
        if distance(x, y, sx, sy) <= d:
            return False
    
    return True

def get_tuning_freq(sensors, limit):
    """Calculate the tuning frequency as described in AOC 2022 Day 15 Part 2

    Args:
        sensors (set): the (x, y) coordinates of all sensors from the puzzle input
        limit (int): largest x/y coordinate of the distress beacon
    
    Returns:
        int: the tuning frequency of the distress beacon's signal
    """
    for sx, sy, d in sensors:
        
        #> Check each sensor a distance of d+1 since beacon was not found at d
        for dx in range(d + 2):
            ##> Back out dy using Manhattan Distance
            dy = d + 1 - dx

            ##> Define the expanded search space
            up = (sx + dx, sy + dy)
            left = (sx + dx, sy - dy)
            right = (sx - dx, sy + dy)
            down = (sx - dx, sy - dy)
            
            ##> x, y must be greater than 0 and less than a certain limit
            for x, y in [up, left, right, down]:
                if not (0 <= x <= limit and 0 <= y <= limit):
                    continue

                if check_dist(x, y, sensors):
                    return 4_000_000 * x + y


#> Parse Input
row_target = 2_000_000
row_empty_spaces = set()
row_beacons_spaces = set()
sensors = set()

for line in lines:
    tokens = line.split(' ')

    ##> Get x, y coordinates for the sensor
    sensor_x = int(tokens[2][2:-1])
    sensor_y = int(tokens[3][2:-1])

    ##> Get x, y coordinates for the beacon
    beacon_x = int(tokens[8][2:-1])
    beacon_y = int(tokens[9][2:])

    ##> Calculate Manhattan Distance between the sensor and beacon
    dist = distance(sensor_x, sensor_y, beacon_x, beacon_y)

    ##> Record the position of each sensor and its distance from the beacon
    sensors.add((sensor_x, sensor_y, dist))

    ##> Since Manhattan Distance, X can only be what is left over after traveling from sensor to target row in Y direction
    y_dist = abs(sensor_y - row_target)
    x_dist = dist - y_dist

    ##> If smaller than leftover X, then the sensor cannot be there and the coordinates on the target row are empty
    x_range_left = sensor_x - x_dist
    x_range_right = sensor_x + x_dist
    for x in range(x_range_left, x_range_right + 1):
        row_empty_spaces.add(x)
    
    ##> If the beacon is on the target row, record it
    if beacon_y == row_target:
        row_beacons_spaces.add(beacon_x)


# Question 1
ans1 = len(row_empty_spaces) - len(row_beacons_spaces)

print(f"Answer 1: {ans1}")


# Question 2
ans2 = get_tuning_freq(sensors, limit=4_000_000)

print(f"Answer 2: {ans2}")