# Modules
from collections import defaultdict


# Import Data
with open("day-22.txt", 'r') as file:
    board, moves = file.read().strip('\n').split('\n\n')


# Classes and Functions
class Password:
    movement = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
    left_turn = {"U": "L", "D": "R", "R": "U", "L": "D"}
    right_turn = {"U": "R", "D": "L", "R": "D", "L": "U"}
    
    score = {"U": 3, "D": 1, "L": 2, "R": 0}
    
    def __init__(self, board, moves) -> None:
        self.board = defaultdict(lambda: " ")
        self.edges = {}
        self.direction = "R"
        self.position = None
        self.max_row = 0
        self.max_col = 0
        self.moves = None
        
        self.parse_board(board)
        self.parse_edges()
        self.parse_moves(moves)
    
    
    def parse_board(self, board):
        """Parse the map of the board

        Args:
            board (list): the map of the board (puzzle input)
        """
        for row, values in enumerate(board.split("\n")):
            for col, char in enumerate(values):
                self.board[(row, col)] = char
                
                if not self.position and char != " ":
                    self.position = (row, col)
            
            self.max_col = max(self.max_col, col)
        
        self.max_row = row
    
    
    def parse_edges(self):
        """For part 2, need to reorient when an edge is reached
        """
        #> Each face is 50 rows
        for i in range(50):
            #> Edges wrap around to a different face
            #> A mapping of where you end up when you walk off a specified edge
            self.edges[(0, 50 + i, "U")] = (150 + i, 0, "R")
            self.edges[(0, 100 + i, "U")] = (199, i, "U")
            self.edges[(100, i, "U")] = (50 + i, 50, "R")
            
            self.edges[(49, 100 + i, "D")] = (50 + i, 99, "L")
            self.edges[(149, 50 + i, "D")] = (150 + i, 49, "L")
            self.edges[(199, i, "D")] = (0, 100 + i, "D")
            
            self.edges[(i, 50, "L")] = (149 - i, 0, "R")
            self.edges[(50 + i, 50, "L")] = (100, i, "D")
            self.edges[(150 + i, 0, "L")] = (0, 50 + i, "D")
            self.edges[(149 - i, 0, "L")] = (i, 50, "R")
            
            self.edges[(50 + i, 99, "R")] = (49, 100 + i, "U")
            self.edges[(150 + i, 49, "R")] = (149, 50 + i, "U")
            self.edges[(i, 149, "R")] = (149 - i, 99, "L")
            self.edges[(149 - i, 99, "R")] = (i, 149, "L")
            
    
    def parse_moves(self, moves):
        """Parse the move instructions

        Args:
            moves (list): a list of instructions at the bottom of the map of the board (puzzle input)
        """
        result = [] 
        temp = ""
        
        for char in moves:
            if char in ["R", "L"]:
                if temp:
                    result.append(int(temp))
                    temp = ""
                
                result.append(char)
            
            elif char in ["0", "1" ,"2", "3", "4", "5", "6", "7", "8", "9"]:
                temp += char
        
        if temp:
            result.append(int(temp))
        
        self.moves = result
    
    
    def move(self, times, part2=False):
        """Move in a certain direction a specific number of times

        Args:
            times (int): how many times to move
            part2 (bool, optional): If this is for part 2. Defaults to False.
        """
        for _ in range(times):
            row, col = self.position
            drow, dcol = self.movement[self.direction]
            nrow, ncol = row + drow, col + dcol
            ndir = self.direction
            
            #> If part 2, must also wrap around edges into 3-D cube
            if part2 and (row, col, self.direction) in self.edges:
                nrow, ncol, ndir = self.edges[(row, col, self.direction)]
            
            if self.board[(nrow, ncol)] == ".":
                self.position = (nrow, ncol)
                self.direction = ndir
            elif self.board[(nrow, ncol)] == "#":
                return
            elif self.board[(nrow, ncol)] == " ":
                if self.direction == "U":
                    row = self.max_row
                elif self.direction == "D":
                    row = 0
                elif self.direction == "L":
                    col = self.max_col
                elif self.direction == "R":
                    col = 0
                
                while self.board[(row, col)] == " ":
                    row, col = row + drow, col + dcol

                if self.board[(row, col)] == ".":
                    self.position = (row, col)
                elif self.board[(row, col)] == "#":
                    return
    
    
    def turn(self, direction):
        """Turn to either the left or the right

        Args:
            direction (char): either 'R' for right or 'L' for left
        """
        if direction == "R":
            self.direction = self.right_turn[self.direction]
        elif direction == "L":
            self.direction = self.left_turn[self.direction]
    
    
    def solve_part1(self):
        """Solve Part 1 by taking steps and turning

        Returns:
            int: the resulting password after traversing the board
        """
        for move in self.moves:
            if move in ["R", "L"]:
                self.turn(move)
            else:
                self.move(move)
        
        row, col = self.position
        password = (row + 1) * 1000 + (col + 1) * 4 + self.score[self.direction]
        
        return password
    
    
    def solve_part2(self):
        """Solve Part 2 by taking steps and turning

        Returns:
            _type_: _description_
        """
        for move in self.moves:
            if move in ["R", "L"]:
                self.turn(move)
            else:
                self.move(move, part2=True)
        
        row, col = self.position
        password = (row + 1) * 1000 + (col + 1) * 4 + self.score[self.direction]
        
        return password

# Question 1
password = Password(board, moves)
ans1 = password.solve_part1()

print(f"Answer 1: {ans1}")


# Question 2
password = Password(board, moves)
ans2 = password.solve_part2()

print(f"Answer 2: {ans2}")