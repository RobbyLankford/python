def how_old(data: list[int]) -> list[int]:
    """
    Given a list of integers or strings, returns a list of the same length
    where the ith entry is the distance of the ith entry in the input list
    to the last occurrence of the same value in the input list,
    or None if there was no previous occurrence.
    Example: how_old([1, 2, 1, 1, 2]) == [None, None, 2, 1, 3]
    """
    out = []
    track = {}
    for idx, item in enumerate(data):
        if item not in track.keys():
            out.append(None)
            track[item] = idx
        else:
            out.append(idx - track[item])
            track[item] = idx
    
    return out

print(how_old([1, 2, 1, 1, 2]))