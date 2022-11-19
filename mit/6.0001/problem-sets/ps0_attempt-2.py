import numpy as np

# Get x,y and make sure that they can be coerced to floats
while True:
    try:
        x = float(input("Enter number x: "))
    except:
        print("Invalid number, please try again.")
    else:
        break

while True:
    try:
        y = float(input("Enter number y: "))
    except:
        print("Invalid number, please try again.")
    else:
        break

# Calculate desired values
power = x ** y
log = np.log2(x)

# Coerce to integers to match desired format
print("x**y = ", int(power))
print("log(x) = ", int(log))