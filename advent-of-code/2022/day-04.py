# Import Data
with open("day-04.txt", "r") as file:
    sections = [section for section in file.read().splitlines()]


# Question 1

overlaps = 0
for section in sections:
    ## Split into both assigned sections using the comma
    section_one, section_two = section.split(",")
    
    ## Coerce to int and extract values
    section_one = [int(i) for i in section_one.split("-")]
    section_two = [int(i) for i in section_two.split("-")]
    
    section_one_start = section_one[0]
    section_one_stop = section_one[1]
    section_two_start = section_two[0]
    section_two_stop = section_two[1]
    
    ## Check if either section fully contains the other
    
    ### Check if section two is contained in section one
    if (section_one_start <= section_two_start) and (section_one_stop >= section_two_stop):
        overlaps += 1
    
    ## Check if section one is contained in section two 
    ## Use elif to avoid double counting if both sections are equal
    elif (section_two_start <= section_one_start) and (section_two_stop >= section_one_stop):
        overlaps += 1

## Print Answer
print("Answer 1: ", overlaps)


# Question 2

overlaps = 0
for section in sections:
    ## Split into both assigned sections using the comma
    section_one, section_two = section.split(",")
    
    ## Coerce to int and extract values
    section_one = [int(i) for i in section_one.split("-")]
    section_two = [int(i) for i in section_two.split("-")]
    
    section_one_start = section_one[0]
    section_one_stop = section_one[1]
    section_two_start = section_two[0]
    section_two_stop = section_two[1]
    
    ## Check if any overlaps exist
    
    ### Check if any part of section one is within section two
    if (section_one_start in range(section_two_start, section_two_stop+1)) or (section_one_stop in range(section_two_start, section_two_stop+1)):
        overlaps += 1
    
    ### Check if any part of section two is within section one
    elif (section_two_start in range(section_one_start, section_one_stop+1)) or (section_two_stop in range(section_one_start, section_one_stop+1)):
        overlaps += 1
    
## Print Answer
print("Answer 2: ", overlaps)