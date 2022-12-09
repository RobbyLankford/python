import numpy as np

x = None
y = None

# If x cannot be coerced to a float, keep asking user to input a number
while x == None:
    x = input("Enter number x: ")
    try: 
        x_float = float(x)
    except:
        x = None

# If y cannot be coerced to a float, keep asking user to input a number
while y == None:
    y = input("Enter a number: ")
    try:
        y_float = float(y)
    except:
        y = None

# Coerce to integers to match desired output format
power_int = int(x_float ** y_float)
log_int = int(np.log2(x_float))

print("x**y = ", power_int)
print("log(x) = ", log_int)