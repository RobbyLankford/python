# Import Data
with open("day-25.txt", 'r') as file:
    nums = file.read().splitlines()


# Classes and Functions
class SNAFU:
    dec_vals = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
    snafu_vals = {0: "0", 1: "1", 2: "2", 3: "=", 4: "-"}
    
    
    def __init__(self, nums) -> None:
        self.nums = nums
    
    
    def convert_from(self, num):
        """Convert from SNAFU base to base 10

        Args:
            num (str): a number to convert

        Returns:
            int: the same number in base 10
        """
        out = []
        
        #> Loop over each character, right to left, and convert
        for i, char in enumerate(reversed(num)):
            out.append(pow(5, i) * self.dec_vals[char])
        
        return sum(out)

    
    def convert_to(self, num):
        """Convert to SNAFU base from base 10

        Args:
            num (int): a number to convert

        Returns:
            str: the same number in SNAFU base
        """
        out = []
        
        #> Step 1. Convert to base 5 notation
        while num:
            #> Records each digit place, from right to left (backwards)
            out.append(num % 5)
            num //= 5
        
        #> Step 2. Convert to SNAFU notation
        for i in range(len(out)):
            #> Since used `% 5`, possible outcomes are: 0, 1, 2, 3, 4
            #> 3 and 4 map to "=" and "-", which requires "carrying" the digit (like going from 09 to 10)
            #> Since `self.convert_to` records the number backwards, "carry" to the next digit
            if out[i] in [3, 4]:
                out[i + 1] += 1
            
            out[i] = self.snafu_vals[out[i]]
        
        return "".join(reversed(out))
    
    
    def solve(self):
        """Solve Day 25 by converting SNAFU base numbers to decimal, summing, then converting the sum back to SNAFU

        Returns:
            str: the sum of the original numbers
        """
        #> Step 1. Convert to decimal and sum
        dec = 0
        
        for num in self.nums:
            dec += self.convert_from(num)
        
        #> Step 2. Convert sum back to SNAFU
        snafu = self.convert_to(dec)
        
        return snafu


# Solution
snafu = SNAFU(nums)
print(snafu.solve())