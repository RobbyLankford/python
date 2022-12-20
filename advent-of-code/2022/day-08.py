# Import Data
with open("day-08.txt", "r") as file:
    forest = [row.strip() for row in file.readlines()]


# Process Data

## Length and width of the forest
rows = len(forest)
cols = len(forest[0])

## Edges of the forest are all visible
edges = (rows * 2) + ((cols - 2) * 2)

## For Question 1, number of visible trees will be at least the edges
total = edges

## For Question 2
scenic_scores = []

## Iterate through the trees not on the edges
for row in range(1, rows - 1):
    for col in range(1, cols - 1):
        
        ### Current tree to be examined
        tree = forest[row][col]
        
        ### ALL trees to the left, right, above, and below the current tree
        left = [forest[row][col - i] for i in range(1, col + 1)]
        right = [forest[row][col + i] for i in range(1, cols - col)]
        above = [forest[row - i][col] for i in range(1, row + 1)]
        below = [forest[row + i][col] for i in range(1, rows - row)]
        
        ### Question 1
        
        #### Check if the height of all trees in any direction are less the height of the current tree
        if (max(left) < tree) or (max(right) < tree) or (max(above) < tree) or (max(below) < tree):
            total += 1
        
        ### Question 2
        
        #### Scenic score will be at least one
        scenic_score = 1
        
        #### Calculate scenic scores in all four directions
        for trees in (left, right, above, below):
            viewing_distances = 0
            
            for i in range(len(trees)):
                ##### If shorter than the current tree, increase viewing distance and continue
                if trees[i] < tree:
                    viewing_distances += 1
                
                ##### If same height or taller, view is blocked, increase and stop
                else:
                    viewing_distances += 1
                    break
                    
            ##### Multiply score in the current direction by the existing score
            scenic_score *= viewing_distances
        
        scenic_scores.append(scenic_score)


# Print Answers
print("Answer 1:", total)
print("Answer 2:", max(scenic_scores))