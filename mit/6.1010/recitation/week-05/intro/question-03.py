# Write the body of the tree_list function below

import trees

def tree_list(tree):
    """
    Given tree as a dict {'value': number, 'children': list of trees}
    return a list of all the values found in the tree (sorted from smallest to largest).
    """
    
    #> Start with the current node's value (may be empty list)
    values = [tree['value']]

    #> Recursively add all values from the children
    for child in tree['children']:
        values.extend(tree_list(child))
    
    return sorted(values)


tree_list(trees.t1)
tree_list(trees.t2)
tree_list(trees.t3)


assert tree_list(trees.t1) == [3]
assert tree_list(trees.t2) == [2, 3, 7, 9]
assert tree_list(trees.t3) == [2, 3, 7, 9, 16, 42, 99]
