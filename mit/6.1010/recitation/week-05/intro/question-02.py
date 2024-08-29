# Write the body of the tree_sum function below

import trees

def tree_sum(tree):
    """
    Given tree as a dict {'value': number, 'children': list of trees}
    return the sum of all the values found in three
    """

    # Base case: tree has no children, just a value
    if not tree['children']:
        return tree['value']

    # Recursive case: the tree has children, sum the value from each child
    return tree['value'] + sum(tree_sum(child) for child in tree['children'])


tree_sum(trees.t1)
tree_sum(trees.t2)
tree_sum(trees.t3)


assert tree_sum(trees.t1) == 3
assert tree_sum(trees.t2) == 21
assert tree_sum(trees.t3) == 178
