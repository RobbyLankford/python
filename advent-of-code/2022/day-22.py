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
        self.direction = "R"
        self.position = None
        self.max_row = 0
        self.max_col = 0
        self.moves = None
        
        self.parse_board(board)
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
    
    
    def move(self, times):
        """Move in a certain direction a specific number of times

        Args:
            times (int): how many times to move
        """
        for _ in range(times):
            row, col = self.position
            drow, dcol = self.movement[self.direction]
            next_space = self.board[(row + drow, col + dcol)]
            
            if next_space == ".":
                self.position = (row + drow, col + dcol)
            elif next_space == "#":
                return
            elif next_space == " ":
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


# Question 1
password = Password(board, moves)
ans1 = password.solve_part1()

print(f"Answer 1: {ans1}")