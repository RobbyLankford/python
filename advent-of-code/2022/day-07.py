# Import Data
with open("day-07.txt", "r") as file:
    terminal = file.readlines()

path = "/"
dirs = {"/": 0}

# Process Data
for output in terminal:
    
    ## All commands start with '$'
    if output[0] == "$":
        
        ### Can ignore listing files
        if output[2:4] == "ls":
            pass
        
        ### Changing the directory is nuanced
        elif output[2:4] == "cd":
            
            #### Go back to the root directory
            if output[5:6] == "/":
                path = "/"

            #### Go back one level
            elif output[5:7] == "..":
                path = path[ :path.rfind("/")]

            #### Change the path to a new directory
            else:
                new_dir = output[5: ]
                path = path + "/" + new_dir
                dirs.update({path: 0})

    
    ## Can ignore listing directories
    elif output[0:3] == "dir":
        pass

    ## All other terminal outputs are file sizes and file names
    else:
        
        ### File sizes are listed first before the file name
        size = int(output[ :output.find(" ")])
        
        ### Each directory's size includes the directories inside of it
        dir = path
        for level in range(path.count("/")):
            dirs[dir] += size
            dir = dir[ :dir.rfind("/")]


# Question 1
total_dir_size = 0
max_dir_size = 100000

## Find all directories that are below the maximum size
for dir in dirs:
    if dirs[dir] <= max_dir_size:
        total_dir_size += dirs[dir]

## Print Answer
print("Answer 1: ", total_dir_size)


# Question 2
max_space = 70000000
needed_space = 30000000
small_dirs = []

## Directory Space Cutoff = Space Needed - Unused Space
space_limit = needed_space - (max_space - dirs["/"])

## Find all directories that are at least as large as the cutoff
for dir in dirs:
    if space_limit <= dirs[dir]:
        small_dirs.append(dirs[dir])

## Print Answer
print("Answer 2: ", min(small_dirs))