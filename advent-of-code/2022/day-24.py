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
                    queue.append((time + 1, row + drow, col + dcol))
        
        return self.part1


# Question 1
blizzards = Blizzards(map)
ans1 = blizzards.solve_part1()

print(f"Answer 1: {ans1}")
