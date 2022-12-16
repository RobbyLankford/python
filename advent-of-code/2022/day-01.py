# Import Data
with open("day-01.txt", "r") as file:
    items = [calories for calories in file.read().strip().split("\n")]


# Question 1

## Variables
cals = 0 #> Calorie counter
max = 0 #> Maximum calories seen

## Iterate Over Items
for item in items:
    ### New Elf indicated by '', reset calorie counter when found
    if item != '':
        cals += int(item)
    else:
        cals = 0
    
    ### Keep record of new maximum calories
    if cals > max:
        max = cals

## Print Answer
print("Answer 1: ", max)


# Question 2

## Variables
cals = 0 #> Calorie counter
max1 = 0 #> Elf with maximum calories
max2 = 0 #> Elf with second maximum calories
max3 = 0 #> Elf with third maximum calories

## Iterate Over Items
for item in items:
    ### New Elf indicated by '', reset calorie counter when found
    if item != '':
        cals += int(item)
    else:
        cals = 0
    
    ### New first largest: assign it and put old value as second largest, old second largest as third largest
    if cals > max1:
        max3 = max2
        max2 = max1
        max1 = cals
    
    ### New second largest: assign it and put old value to third largest
    elif cals > max2:
        max3 = max2
        max2 = cals
    
    ### New third largest: assign it
    elif cals > max3:
        max3 = cals

## Print Answer
print("Answer 2: ", max1 + max2 + max3)