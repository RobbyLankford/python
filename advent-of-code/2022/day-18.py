# Import & Parse Data
with open("ex.txt", 'r') as file:
    scan = file.readlines()


# Classes and Functions
class Lava:
    def __init__(self, scan) -> None:
        self.cubes = set()

        #> Check if any of the cube faces are touching a cube right next to it
        self.deltas = [
            (1, 0, 0), (-1, 0, 0),
            (0, 1, 0), (0, -1, 0),
            (0, 0, 1), (0, 0, -1)
        ]

        for droplet in scan:
            x, y, z = list(map(int, droplet.split(',')))
            self.cubes.add((x, y, z))
        
        x_vals = [x for x, y, z in self.cubes]
        y_vals = [y for x, y, z in self.cubes]
        z_vals = [z for x, y, z in self.cubes]

        self.min_x, self.max_x = min(x_vals), max(x_vals)
        self.min_y, self.max_y = min(y_vals), max(y_vals)
        self.min_z, self.max_z = min(z_vals), max(z_vals)

        self.surface_area = 0
        self.external_surface_area = 0


    def solve_part1(self):
        """Solve Part 1 by calculating the surface area of the cubes

        Args: none (self)

        Returns: updates self.surface_area, the surface areas of the droplets
        """
        for x, y, z in self.cubes:
            for dx, dy, dz in self.deltas:
                if (x + dx, y + dy, z + dz) not in self.cubes:
                    self.surface_area += 1
    

    def can_be_reached(self, x, y, z):
        """ Uses Breadth First Search to determine if water and steam could reach cube

        Args: self, x-coordinate, y-coordinate, and z-coordinate of cube

        Returns: True if an external face is found, False if it is not
        """
        queue = []
        queue.append((x, y, z))
        visited = set()

        #> Idea is to search along cubes to see where an external face is

        while len(queue) > 0:
            x, y, z = queue.pop(0)

            #> If cube + delta has been visited before, skip (do not double-count)
            if (x, y, z) in visited:
                continue
                
            visited.add((x, y, z))

            #> If cube + delta is a cube, skip (water cannot reach it)
            if (x, y, z) in self.cubes:
                continue
            
            #> Check if cube + delta is outside of the group of cubes
            x_outside = x > self.max_x or x < self.min_x
            y_outside = y > self.max_y or y < self.min_y
            z_outside = z > self.max_z or z < self.min_z
            
            #> If it is, then it is an external face, so return True
            if x_outside or y_outside or z_outside:
                return True
            
            #> Update queue with where we can visit from current position
            for dx, dy, dz in self.deltas:
                queue.append((x + dx, y + dy, z + dz))
        
        #> If no external face is found, return False
        return False


    def solve_part2(self):
        """Solve Part 1 by calculating the external surface area of the cubes

        Args: none (self)

        Returns: updates self.external_surface_area, the external surface areas of the droplets
        """
        for x, y, z in self.cubes:
            for dx, dy, dz in self.deltas:
                if self.can_be_reached(x + dx, y + dy, z + dz):
                    self.external_surface_area += 1


# Question 1
lava = Lava(scan)
lava.solve_part1()

print(f"Answer 1: {lava.surface_area}")


# Question 2
lava = Lava(scan)
lava.solve_part2()

print(f"Answer 2: {lava.external_surface_area}")
