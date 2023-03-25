# Import Data
with open("day-24.txt", 'r') as file:
    map = file.readlines()


# Classes and Functions
class Blizzards:
    directions = {
        "^": (-1, 0), # Up
        "v": (1, 0),  # Down
        "<": (0, -1), # Left
        ">": (0, 1)   # Right
    }
    
    
    def __init__(self, map) -> None:
        self.map = map
        self.num_rows = len(map) - 2
        self.num_cols = len(map[0]) - 3
        self.start = (-1, map[0].index(".") - 1)
        self.stop = (self.num_rows, map[-1].index(".") - 1)
        self.times = {}
    
    
    def get_storms(self, time):
        """Update locations of blizzards based on how much time has elapsed

        Args:
            time (int): amount of time that has elapsed since the beginning

        Returns:
            set: a grid of where the storms are located at the specified time
        """
        #> Reduce repeated calculations since storms always go in the same patterns
        if time in self.times.keys():
            return self.times[time]
        
        #> Remove the upper and lower walls from the map
        no_horiz_walls = self.map[1:-1]
        storm_locations = set()
        
        for row, value in enumerate(no_horiz_walls):
            #> Remove the left and right walls from each row of the map
            no_vert_walls = value[1:-1]
            
            for col, char in enumerate(no_vert_walls):
                if char in "^v<>":
                    drow, dcol = self.directions[char]
                    
                    #> Use modulo because the storms wrap around when they reach a wall
                    new_row = (row + (drow * time)) % self.num_rows
                    new_col = (col + (dcol * time)) % self.num_cols
                    
                    storm_locations.add((new_row, new_col))
        
        #> Add to cache so that it does not have to be calculated again later
        if time not in self.times.keys():
            self.times[time] = storm_locations
        
        return storm_locations
    
    
    def solve_part1(self):
        """Solve Part 1 by finding the minimum amount of time it takes to traverse the blizzards

        Returns:
            int: the minimum number of minutes required
        """
        self.part1 = None
        
        #> Use Breadth-First-Search to try all possibilities
        queue = list()
        queue.append((0, self.start[0], self.start[1]))
        visited = set()
        
        while not self.part1:
            time, row, col = queue.pop(0)
            
            if (time, row, col) in visited:
                continue
            
            visited.add((time, row, col))
            
            storms = self.get_storms(time + 1)
            
            if (row, col) not in storms:
                queue.append((time + 1, row, col))
            
            for drow, dcol in self.directions.values():
                new_row = row + drow
                new_col = col + dcol
                
                #> Stop if we reach the end
                if (new_row, new_col) == self.stop:
                    self.part1 = time + 1
                    break
                
                #> Keep going if we are on the map and there is no storm in our way
                elif 0 <= new_row < self.num_rows and 0 <= new_col < self.num_cols and (new_row, new_col) not in storms:
                    queue.append((time + 1, new_row, new_col))
        
        return self.part1
    
    
    def solve_part2(self):
        self.part2 = None
        
        #> Use Breadth-First-Search to try all possibilities
        queue = list()
        queue.append((0, *self.start, 0))
        visited = set()
        
        #> Same as self.solve_part1, but include "trip" since the route is done 3 times
        while not self.part2:
            time, row, col, trip = queue.pop(0)
            
            if (time, row, col, trip) in visited:
                continue
            
            visited.add((time, row, col, trip))
            
            storms = self.get_storms(time + 1)
            
            if (row, col) not in storms:
                queue.append((time + 1, row, col, trip))
            
            for drow, dcol in self.directions.values():
                new_row = row + drow
                new_col = col + dcol
                
                #> If we reach the end of the path...
                if (new_row, new_col) == self.stop and trip in [0, 2]:
                    #> ... the first time, increment trip to 1 to turn around and go back
                    if trip == 0:
                        queue.append((time + 1, new_row, new_col, 1))
                    #> ... the second time, then record the time and end
                    else:
                        self.part2 = time + 1
                        break
                
                #> If we reach the start of the path, increment trip to 2 to turn around and go back
                elif (new_row, new_col) == self.start and trip == 1:
                    queue.append((time + 1, *self.start, 2))
                    break
                
                #> Keep going if we are on the map and there is no storm in our way
                elif 0 <= new_row < self.num_rows and 0 <= new_col < self.num_cols and (new_row, new_col) not in storms:
                    queue.append((time + 1, new_row, new_col, trip))
    
        return self.part2


# Question 1
blizzards = Blizzards(map)
ans1 = blizzards.solve_part1()

print(f"Answer 1: {ans1}")


# Question 2
blizzards = Blizzards(map)
ans2 = blizzards.solve_part2()

print(f"Answer 2: {ans2}")
