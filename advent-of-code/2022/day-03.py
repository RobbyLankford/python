# Import Data
with open("day-03.txt", "r") as file:
    rucksacks = [rucksack for rucksack in file.read().strip().split("\n")]

# Question 1

## Create List of Letters
letters_lower = [chr(i) for i in range(97, 123)]
letters_upper = [i.upper() for i in letters_lower]
letters = letters_lower + letters_upper

total = 0
for rucksack in rucksacks:
    ## Split Each Rucksack at Midpoint
    midpoint = len(rucksack) // 2
    left = rucksack[ :midpoint]
    right = rucksack[midpoint: ]
    
    ## Get Unique Values in Each Compartment
    left_unique = set(left)
    right_unique = set(right)

    ## Assign Priority
    for priority, letter in enumerate(letters):
        if letter in left_unique and letter in right_unique:
            total += (priority + 1)

## Print Answer
print("Answer 1: ", total)


# Question 2

## Take 3 Rucksacks at a Time
total = 0
for i in range(0, len(rucksacks), 3):
    rucksacks_subset = rucksacks[i:(i+3)]
    
    for priority, letter in enumerate(letters):
        if (letter in rucksacks_subset[0]) and (letter in rucksacks_subset[1]) and (letter in rucksacks_subset[2]):
            total += (priority + 1)

## Print Answer
print("Answer 2: ", total)