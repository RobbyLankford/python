# Write the body of the tree_max function below

import trees

def tree_max(tree):
    """
    Given tree as a dict {'value': number, 'children': list of trees}
    return the maximum value found in the tree
    """
    
    #> Base Case: the tree has no children
    if not tree['children']:
        return tree['value']
    
    #> Recursive Case: the tree has children, get maximum value from them
    max_value = max(tree_max(child) for child in tree['children'])

    return max(tree['value'], max_value)


tree_max(trees.t1)
tree_max(trees.t2)
tree_max(trees.t3)


assert tree_max(trees.t1) == 3
assert tree_max(trees.t2) == 9
assert tree_max(trees.t3) == 99
