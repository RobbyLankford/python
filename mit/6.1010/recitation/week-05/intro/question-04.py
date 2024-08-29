# Write the body of the tree_depth function below

import trees

def tree_depth(tree, depth):
    """
    Given tree as a dict {'value': number, 'children': list of trees}
    return a sorted list of all the values found in the tree at the given depth 
    (where depth=0 represents the tree value, depth=1 represents the child values, etc.)
    If there are no values at the given depth, return None.
    """
    
    #> Base case: if depth=0, return the value of the current node
    if depth == 0:
        return [tree['value']]
    
    #> Recursive case: if depth > 0, check children
    depth_values = []
    for child in tree['children']:
        child_values = tree_depth(child, depth - 1)

        ##> If children have values...
        if child_values:
            depth_values.extend(child_values)
    
    return sorted(depth_values) if depth_values else None


tree_depth(trees.t1, depth=-1)
tree_depth(trees.t1, depth=0)
tree_depth(trees.t1, depth=1)

tree_depth(trees.t2, depth=0)
tree_depth(trees.t2, depth=1)
tree_depth(trees.t2, depth=199)

tree_depth(trees.t3, depth=0)
tree_depth(trees.t3, depth=1)
tree_depth(trees.t3, depth=2)
tree_depth(trees.t3, depth=3)


assert tree_depth(trees.t1, -1) is None
assert tree_depth(trees.t1, 0) == [3]
assert tree_depth(trees.t1, 1) is None
assert tree_depth(trees.t2, 0) == [9]
assert tree_depth(trees.t2, 1) == [2, 3, 7]
assert tree_depth(trees.t2, 199) is None
assert tree_depth(trees.t3, 0) == [9]
assert tree_depth(trees.t3, 1) == [2, 3]
assert tree_depth(trees.t3, 2) == [16, 42, 99]
assert tree_depth(trees.t3, 3) == [7]