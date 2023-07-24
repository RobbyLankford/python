# 6.0002 Problem Set 1b: Space Change

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    total_eggs_int = 0
    
    for weight in reversed(egg_weights):
        current_eggs_int = target_weight // weight
        total_eggs_int += current_eggs_int
        target_weight -= (current_eggs_int * weight)
    
    return total_eggs_int

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights1 = (1, 5, 10, 25)
    egg_weights2 = (1, 5, 10, 20)
    n = 99
    
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 ((3 * 25) + (2 * 10) + (0 * 5) + (4 * 1) = 99)")
    print("Actual output:", dp_make_weight(egg_weights1, n))
    print()
    print("Egg weights = (1, 5, 10, 20)")
    print("n = 99")
    print("Expected output: 10 ((4 * 20) + (1 * 10) + (1 * 5) + (4 * 1) = 99)")
    print("Actual output:", dp_make_weight(egg_weights2, n))