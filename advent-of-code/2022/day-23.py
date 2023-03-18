# Modules
from collections import defaultdict


# Import Data
with open("day-23.txt", 'r') as file:
    scan = file.readlines()


# Classes and Functions
class Grove:
    directions = [
        #> North West, North, North East
        ((1, -1), (1, 0), (1, 1)),
        
        #> South West, South, South East
        ((-1, -1), (-1, 0), (-1, 1)),
        
        #> North West, West, South West
        ((1, -1), (0, -1), (-1, -1)),
        
        #> North East, East, South East
        ((1, 1), (0, 1), (-1, 1))
    ]
    
    
    def __init__(self, scan) -> None:
        self.elves = set()
        self.parse_scan(scan)
    
    
    def parse_scan(self, scan):
        for row, line in enumerate(scan):
            for col, char in enumerate(line):
                if char == '#':
                    self.elves.add((row, col))
    
    
    def check_no_neighbors(self, row, col):
        """Check if there is another elf on any of the eight sides of an elf

        Args:
            row (int): the row coordinate of the elf
            col (int): the column coordinate of the elf

        Returns:
            bool: True if the elf has no neighbors, False otherwise
        """
        check = 0
        
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if (row + dr, col + dc) in self.elves:
                    check += 1
        
        return check == 1
    
    
    def check_next_move(self, row, col, consider):
        """Check if there is a next move available to an elf

        Args:
            row (int): the row coordinate of the elf
            col (int): the column coordinate of the elf
            consider (list): all directions that the elf can consider moving

        Returns:
            bool: True if the elf has at least one valid available move, False otherwise
        """
        check = 0
        
        for dr, dc in consider:
            if (row + dr, col + dc) in self.elves:
                check += 1
        
        return check == 0
    
    
    def calc_empty_spaces(self):
        """Calculate the number of empty spaces in the smallest possible rectangle that surrounds all elves

        Returns:
            int: the number of empty spaces that do not contain an elf in the rectangle
        """
        min_row = min(row for row, col in self.elves)
        max_row = max(row for row, col in self.elves)
        min_col = min(col for row, col in self.elves)
        max_col = max(col for row, col in self.elves)
        
        return (max_row - min_row + 1) * (max_col - min_col + 1) - len(self.elves)
    
    
    def solve_part1(self, rounds=10):
        """Solve Part 1 by finding the number of empty spaces that do not contain an elf

        Args:
            rounds (int, optional): The number of rounds to play. Defaults to 10.

        Returns:
            int: the number of empty spaces that do not contain an elf in the rectangle
        """
        for round in range(rounds):
            moves = defaultdict(list)
            
            #> Each elf considers the next move
            for row, col in self.elves:
                ##> 1. Check for No Neighbors
                if self.check_no_neighbors(row, col):
                    continue
                
                ##> 2. Check for Next Move
                for move in range(4):
                    consider = self.directions[(move + round) % 4]
                    
                    ###> If a move is available, register the "to" as the key and the "from" as the value
                    if self.check_next_move(row, col, consider):
                        moves[(row + consider[1][0], col + consider[1][1])].append((row, col))
                        break
            
            #> Perform any next moves
            for move_to, move_from in moves.items():
                ##> Elf can move if only one of them wants to move to a certain spot
                if len(move_from) == 1:
                    self.elves.add(move_to)
                    self.elves.remove(move_from[0])
            
        return self.calc_empty_spaces()


# Question 1
grove = Grove(scan)
ans1 = grove.solve_part1()

print(f"Answer 1: {ans1}")