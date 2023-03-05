# Import Data
with open("day-20.txt", 'r') as file:
    encryption = list(map(int, file.readlines()))


# Classes and Functions
class Decrypt:
    def __init__(self, encryption, key = 1) -> None:
        self.encryption = list((i, n * key) for i, n in enumerate(encryption))
        self.grove_coords = [0, 0, 0]
    
    
    def mix(self):
        """Mix the encryption by moving the individual numbers by their values
        
        Args: none (self)
        
        Returns: updates self.encryption and self.grove_coords
        """
        length = len(self.encryption)
        
        for i in range(length):
            while True:
                if self.encryption[0][0] == i:
                    break
                self.encryption.append(self.encryption.pop(0))
            
            current = self.encryption.pop(0)
            move_by = current[1] % (length - 1)
            
            for _ in range(move_by):
                self.encryption.append(self.encryption.pop(0))
            self.encryption.append(current)
        
        while self.encryption[0][1] != 0:
            self.encryption.append(self.encryption.pop(0))
        
        for i in range(3):
            coord_idx = (i + 1) * 1000
            coordinate = self.encryption[coord_idx % len(self.encryption)]
            self.grove_coords[i] = coordinate[1]
    
    
    def solve(self, times=1):
        """Solve Part 1 and Part 2 by finding the grove coordinates
        
        Args:
            times (int): the number of times to mix

        Returns:
            int: self.grove_coords
        """
        for _ in range(times):
            self.mix()
        
        return self.grove_coords


# Question 1
decrypt = Decrypt(encryption)
grove_coords = decrypt.solve()

print(f"Answer 1: {sum(grove_coords)}")


# Question 2
decrypt = Decrypt(encryption, key=811589153)
grove_coords = decrypt.solve(times=10)

print(f"Answer 2: {sum(grove_coords)}")