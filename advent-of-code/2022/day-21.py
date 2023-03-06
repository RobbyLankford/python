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
    
    
    def solve_part1(self, monkey='root'):
        """Solve Part 1 by finding the number shouted by the monkey 'root'

        Args:
            monkey (str, optional): Which monkey to identify. Defaults to 'root'.

        Returns:
            int: the number the specified monkey will yell
        """
        job = self.monkeys[monkey]
        
        # If monkey does not have an integer to shout, recursively go through math operations
        try:
            return int(job)
        except ValueError:
            parts = job.split(" ")
            
            if parts[1] == '+':
                return self.solve_part1(parts[0]) + self.solve_part1(parts[2])
            if parts[1] == '-':
                return self.solve_part1(parts[0]) - self.solve_part1(parts[2])
            if parts[1] == '*':
                return self.solve_part1(parts[0]) * self.solve_part1(parts[2])
            if parts[1] == '/':
                return self.solve_part1(parts[0]) / self.solve_part1(parts[2])
    
    
    def solve_part2(self, monkey='root', humn=None):
        """Solve Part 2 by finding the number the `humn` needs to shout

        Args:
            monkey (str, optional): The name of the `root` monkey. Defaults to 'root'.
            humn (int, optional): A possible value the `humn` needs to shout. Defaults to None.

        Returns:
            int: the number shouted by the monkey `root`
        """
        if monkey == 'humn':
            return humn
        
        job = self.monkeys[monkey]
        
        # If monkey does not have an integer to shout, recursively go through math operations
        try:
            return int(job)
        except ValueError:
            parts = job.split(" ")
            
            # Need to check if the two values given to `root` are the same
            if monkey == 'root':
                value1 = self.solve_part2(parts[0], humn)
                value2 = self.solve_part2(parts[2], humn)
                return (value1 == value2, value1, value2)
            
            if parts[1] == '+':
                return self.solve_part2(parts[0], humn) + self.solve_part2(parts[2], humn)
            if parts[1] == '-':
                return self.solve_part2(parts[0], humn) - self.solve_part2(parts[2], humn)
            if parts[1] == '*':
                return self.solve_part2(parts[0], humn) * self.solve_part2(parts[2], humn)
            if parts[1] == '/':
                return self.solve_part2(parts[0], humn) / self.solve_part2(parts[2], humn)
    
    
    def bisection_search(self, hi, lo):
        """Run Bisection Search

        Args:
            hi (int): The upper bound to search
            lo (int): The lower bound to search

        Returns:
            int: Either the value that matches the condition, or None
        """
        mid = int((hi + lo) // 2)
        
        # Run a standard bisection search to find what number needs to be shouted by `humn`
        while True:
            equal, value1, value2 = self.solve_part2('root', mid)

            if mid <= lo or mid >= hi:
                return None
            elif equal:
                break
            elif value1 > value2:
                lo = mid
            else:
                hi = mid
            
            mid = int((hi + lo) // 2)
        
        return mid


# Question 1
monkeys = Monkeys(lines)
ans1 = monkeys.solve_part1()

print(f"Answer 1: {int(ans1)}")


# Question 2
monkeys = Monkeys(lines)
ans2 = monkeys.bisection_search(hi=1e20, lo=-1e20)

print(f"Answer 2: {ans2}")