# Question 1

## Import Data
with open("day-05.txt", "r") as file:
    ## Split the stacks of crates and the instructions by the empty row
    stacks, instructions = (entry.splitlines() for entry in file.read().strip("\n").split("\n\n"))

## Grab the last line of the stacks, which are the stack ID numbers, and remove the spaces
stack_dict = {int(idx):[] for idx in stacks[-1].replace(" ", "")}

## The column indices (literally the characters in the text)
## The last row, when it is not a space, is the stack ID number
col_indices = [index for index, value in enumerate(stacks[-1]) if value != " "]

## Load the crates into a dictionary representation
for row in stacks[ :-1]:
    crate_num = 1
    for index in col_indices:
        if row[index] != " ":
            ### When a crate is found, insert it into the front of the list for that stack of crates
            ### Insert it in front because we are representing the front of the list as the bottom...
            ### .. since we are woorking our way down from the top of the stack to the bottom
            stack_dict[crate_num].insert(0, row[index])
        crate_num += 1

## Follow instructions
for instruction in instructions:
    instruction = instruction.replace("move", "").replace("from ", "").replace("to ", "")
    instruction = instruction.strip().split(" ")
    instruction = [int(i) for i in instruction]

    ### Number of crates to move
    num_crates = instruction[0] 
    
    ### Stack from which to move the crates
    stack_from = instruction[1] 
    
    ### Stack to which to move the crates
    stack_to = instruction[2]
    
    for crate in range(num_crates):
        ### Pop the crate from the end of the list (the top of the stack)
        removed_crate = stack_dict[stack_from].pop() 
        
        ### Append the crate to the end of the list (the top of the stack)
        stack_dict[stack_to].append(removed_crate) 

## Get the last row (the top of the stack) for each stack
top_of_stacks = ""
for idx in stack_dict:
    top_of_stacks += stack_dict[idx][-1]

## Print Answer
print("Answer 1: ", top_of_stacks)


# Question 2

## Import Data (Again)
with open("day-05.txt", "r") as file:
    ## Split the stacks of crates and the instructions by the empty row
    stacks, instructions = (entry.splitlines() for entry in file.read().strip("\n").split("\n\n"))

## Grab the last line of the stacks, which are the stack ID numbers, and remove the spaces
stack_dict = {int(idx):[] for idx in stacks[-1].replace(" ", "")}

## The column indices (literally the characters in the text)
## The last row, when it is not a space, is the stack ID number
col_indices = [index for index, value in enumerate(stacks[-1]) if value != " "]

## Load the crates into a dictionary representation
for row in stacks[ :-1]:
    crate_num = 1
    for index in col_indices:
        if row[index] != " ":
            ### When a crate is found, insert it into the front of the list for that stack of crates
            ### Insert it in front because we are representing the front of the list as the bottom...
            ### .. since we are woorking our way down from the top of the stack to the bottom
            stack_dict[crate_num].insert(0, row[index])
        crate_num += 1

## Follow instructions
for instruction in instructions:
    instruction = instruction.replace("move", "").replace("from ", "").replace("to ", "")
    instruction = instruction.strip().split(" ")
    instruction = [int(i) for i in instruction]
    
    ### Number of crates to move
    num_crates = instruction[0] 
    
    ### Stack from which to move the crates
    stack_from = instruction[1] 
    
    ### Stack to which to move the crates
    stack_to = instruction[2]
    
    ### Move the crates all at once, retaining their order
    
    #### In each stack, grab the number of crates to move...
    #### from the end of the list (top of the stack)
    crates_to_move = stack_dict[stack_from][-num_crates: ]
    
    #### Remove the crates from their original stack
    stack_dict[stack_from] = stack_dict[stack_from][ :-num_crates]
    
    #### Place the crates in their new stack (append to end of list/top of stack)
    for crate in crates_to_move:
        stack_dict[stack_to].append(crate)
    
## Get the last row (the top of the stack) for each stack
top_of_stacks = ""
for idx in stack_dict:
    top_of_stacks += stack_dict[idx][-1]

## Print Answer
print("Answer 2: ", top_of_stacks)