# Import Data
with open("day-06.txt", "r") as file:
    buffer = file.read()

# Question 1
for i in range(0, len(buffer) - 3):
    ## Subset four characters at a time, use a set to get unique characters
    marker = buffer[i:i+4]
    unique = set(marker)
    
    ## As soon as we find four unique characters, break out of the loop
    if len(unique) == 4:
        ### Print Answer, which is i+4 b/c we want how many characters are fully processed
        print("Answer 1: ", i+4)
        break


# Question 2
for i in range(0, len(buffer) - 13):
    ## Subset fourteen characters at a time, use a set to get unique characters
    marker = buffer[i:i+14]
    unique = set(marker)
    
    ## As soon as we find fourteen unique characters, break out of the loop
    if len(unique) == 14:
        ### Print Answer, which is i+14 b/c we want how many characters are fully processed
        print("Answer 2: ", i+14)
        break