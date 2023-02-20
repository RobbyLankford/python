# Import & Parse Data
with open("ex.txt", 'r') as file:
    pattern = file.read().strip()


# Classes and Functions
class Simulation:
    def __init__(self, pattern) -> None:
        self.pattern = pattern
        self.pattern_step = 0

        self.cave = set()

        #> Cave is 8 units wide, including the walls
        for x in range(9):
            self.cave.add((x, 0))

        self.rock = set()
        self.rock_id = 0
        self.pile_height = 0
    
    
    def get_new_rock(self):
        """Defines and instantiates the five rocks as described in the puzzle description.

        Args: none

        Returns: updates class attributes for a new rock.
        """

        self.rock = set()
        rock_num = self.rock_id % 5 #> Five types of rocks that repeat in order

        #> Rock start 2 units away from left wall (0) and 3 units above highest rock or floor

        #> Rock Shape: ####
        if rock_num == 0:
            for x in range(3, 7):
                self.rock.add((x, self.pile_height + 4))
        
        #>              .#.
        #> Rock Shape:  ###
        #>              .#.
        elif rock_num == 1:
            self.rock.add((3, self.pile_height + 5))
            self.rock.add((5, self.pile_height + 5))

            for y in range(4, 7):
                self.rock.add((4, self.pile_height + y))
        
        #>              ..#
        #> Rock Shape:  ..#
        #>              ###
        elif rock_num == 2:
            for x in range(3, 6):
                self.rock.add((x, self.pile_height + 4))
            for y in range(5, 7):
                self.rock.add((5, self.pile_height + y))
        
        #>        #
        #> Rock   #
        #> Shape: # 
        #>        #
        elif rock_num == 3:
            for y in range(4, 8):
                self.rock.add((3, self.pile_height + y))
        
        #> Rock   ##
        #> Shape: ##
        else:
            for x in range(3, 5):
                for y in range(4, 6):
                    self.rock.add((x, self.pile_height + y))
        
        self.rock_id += 1


    def drop_a_rock(self):
        """Drop a single rock (loops through a single rock falling until it stops)

        Args: none

        Returns: nothing, updates class attributes
        """
        self.get_new_rock()
        
        while True:
            #> Step 1: Rock Pushed Left or Right
            jet_pattern = self.pattern[self.pattern_step]

            if jet_pattern == '>':
                self.push(dir='right')
            else:
                self.push(dir='left')
            
            #> Step 2: Rock Falls
            can_fall = self.fall()

            if not can_fall:
                break
            
    
    def push(self, dir='right'):
        """Push rock left or right one unit, if possible

        Args: none

        Returns: nothing, updates class attributes
        """
        #> Push right (+) one unit or left (-) one unit
        dx = 1 if dir == 'right' else -1

        #> Check if rock is against wall or rock is on top of the pile
        x_dir_clear = all(0 < x + dx < 8 for x, y in self.rock)
        y_dir_clear = all((x + dx, y) not in self.cave for x, y in self.rock)

        #> If the rock can move left or right, update self.rock with new coords
        if x_dir_clear and y_dir_clear:
            self.rock = set((x + dx, y) for x, y in self.rock)
        
        #> Increment pattern step counter (use % b/c entire pattern can repeat)
        self.pattern_step = (self.pattern_step + 1) % len(self.pattern)
    

    def fall(self):
        """Move rock down one unit, if possible.

        Args: none

        Returns: True if rock can continue falling, False if it cannot
        """
        #> If rock can fall, move all coords down and return False
        y_dir_clear = all((x, y - 1) not in self.cave for x, y in self.rock)

        if y_dir_clear:
            self.rock = set((x, y - 1) for x, y in self.rock)
            return True
        
        #> If rock cannot fall, add final in coords to cave grid and return True
        self.pile_height = max([y for x, y in self.rock] + [self.pile_height])

        for x,y in self.rock:
            self.cave.add((x, y))

        return False


# Question 1
simulation = Simulation(pattern)

rocks_to_drop = 2022

for _ in range(rocks_to_drop):
    simulation.drop_a_rock()

print(f"Answer 1: {simulation.pile_height}")