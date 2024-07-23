def first_occurrence(data: list[int]) -> list[int]:
    """
    Given a list of integers or strings, return a new list with the same
    set of items in the same order, but keeping only the first occurrence of
    each item.
    Example: first_occurrence([1, 9, 1, 1, 5, 3, 2, 9, 10]) == [1, 9, 5, 3, 2, 10]
    """
    out = []
    for item in data:
        if item not in out:
            out.append(item)
    
    return out

print(first_occurrence([1, 9, 1, 1, 5, 3, 2, 9, 10]))