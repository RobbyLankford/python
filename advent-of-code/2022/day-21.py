# Import Data
with open("day-21.txt", 'r') as file:
    lines = file.readlines()


# Classes and Functions
class Monkeys:
    def __init__(self, lines) -> None:
        self.monkeys = {}
        
        for line in lines:
            monkey, job = line.strip().split(": ")
            self.monkeys[monkey] = job
    
    
    def get_value(self, monkey = 'root'):
        """Recursively determine what value any given monkey will yell

        Args:
            monkey (str, optional): Which monkey to identify. Defaults to 'root'.

        Returns:
            int: the number the specified monkey will yell
        """
        job = self.monkeys[monkey]
        
        # Monkey values are either an integer or a computation
        try:
            return int(job)
        except ValueError:
            # If not an integer, must be either +, -, *, or / of two numbers
            parts = job.split(" ")
            
            if parts[1] == '+':
                return self.get_value(parts[0]) + self.get_value(parts[2])
            if parts[1] == '-':
                return self.get_value(parts[0]) - self.get_value(parts[2])
            if parts[1] == '*':
                return self.get_value(parts[0]) * self.get_value(parts[2])
            if parts[1] == '/':
                return self.get_value(parts[0]) / self.get_value(parts[2])
    
    
    def solve_part1(self):
        """Solve Part 1 by finding the number shouted by the monkey 'root'

        Args: none (self)

        Returns:
            int: the number shouted by the monkey 'root'
        """
        return int(self.get_value(monkey='root'))


# Question 1
monkeys = Monkeys(lines)
ans1 = monkeys.solve_part1()

print(f"Answer 1: {ans1}")