from typing import List, Optional

# Classes and Functions
class Document:
    def __init__(self, fname) -> None:
        with open(fname, 'r') as file:
            self.document = file.read().splitlines()
        
        self.num_name_to_digit = {
            'one': '1', 'two': '2', 'three': '3', 
            'four': '4', 'five': '5', 'six': '6', 
            'seven': '7', 'eight': '8', 'nine': '9'
        }
        
        self.lines = [Line(line) for line in self.document]
    
    def solve_part1(self) -> int:
        """Create a number by concatenating the left-most and right-most digit from a line

        Returns:
            int: a two-digit number
        """
        out = 0
        for line in self.lines:
            left_digit = line.get_leftmost_digit()
            right_digit = line.get_rightmost_digit()
            out += int(left_digit + right_digit)
        
        return out
    
    def solve_part2(self) -> int:
        """Create a number of examining a string for both digits and spelled-out digits
           then concatenating the left-most and right-most digit

        Returns:
            int: a two-digit number
        """
        out = 0
        for line in self.lines:
            line_length = line.get_length()
            
            nums = []
            for i in range(line_length):
                char = line.get_char(i)
                
                #> If a digit is found, nothing else is needed
                if char.isdigit():
                    nums.append(char)
                    
                #> If a digit is not found, check if the digit is spelled out
                else:
                    for num in self.num_name_to_digit:
                        #> Kinda hacky solution...
                        #> Check each sequential subset of a line for a spelled-out digit
                        line_subset = line.get_line(i)
                        
                        if line_subset.startswith(num):
                            nums.append(self.num_name_to_digit[num])
            
            out += int(nums[0] + nums[-1])
        
        return out

class Line:
    def __init__(self, line: List) -> None:
        self.line = line
        self.digits = [c for c in self.line if c.isdigit()]
    
    def get_leftmost_digit(self) -> str:
        """Return the left-most digit in a line

        Returns:
            str: the left-most digit in the line
        """
        return self.digits[0]

    def get_rightmost_digit(self) -> str:
        """Return the right-most digit in a line

        Returns:
            str: the right-most digit in the line
        """
        return self.digits[-1]
    
    def get_line(self, start: int = None, stop: int = None) -> str:
        """Return the underying line as a string
        
        Optional arguments are start and stop to return a subset of the string.
        If start is left as None, the entire string will be returned.
        If start is not None, but stop is left as None, it will return the entire string from the start point.

        Args:
            start (int, optional): The starting point of the string. Defaults to None.
            stop (int, optional): The stopping point of the string. Defaults to None.

        Returns:
            str: The line as a string
        """
        if start is None:
            return self.line
        else:
            if stop is None:
                stop = self.get_length()
            return self.line[slice(start, stop)]
    
    def get_char(self, idx: int) -> str:
        """Return a specific character in the line

        Args:
            idx (int): the index of the character in the string

        Returns:
            str: a single character
        """
        return self.line[idx]
    
    def get_length(self) -> int:
        """Return the length of a line

        Returns:
            int: The number of characters in the line
        """
        return len(self.get_line())


# Load Data
document = Document("day-01.txt")


# Part 1
part1 = document.solve_part1()
print(f"Part 1 Answer: {part1}")


# Part 2
part2 = document.solve_part2()
print(f"Part 2 Answer: {part2}")