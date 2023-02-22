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

        self.surface_area = 0


    def solve_part1(self):
        """Solve Part 1 by calculating the surface area of the cubes

        Args: none (self)

        Returns: updates self.surface_area, the surface areas of the droplets
        """
        for x, y, z in self.cubes:
            for dx, dy, dz in self.deltas:
                if (x + dx, y + dy, z + dz) not in self.cubes:
                    self.surface_area += 1


# Question 1
lava = Lava(scan)
lava.solve_part1()

print(f"Answer 1: {lava.surface_area}")
