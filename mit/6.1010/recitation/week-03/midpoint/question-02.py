# Map: A dictionary, where key is a building number and values are buildings connected to key
# '26': {'36'} #> 26 connects to 36
# '36': {'26', '32'} #> 36 connects to 26 and 32

def can_reach(map: dict, start_building: str, goal_building: str) -> bool:
    """
    map: dictionary { `building` : set of the directly-connected neighbors }
    start_building: building to start from
    goal_building: building you're trying to reach
    
    returns True if and only if you can get from start_building
        to goal_building through directly-connected neighbors, i.e.
        without going outside
    """
    
    # helper function to get neighbors of building
    def get_neighbors(building: str) -> set:
        return map[building]

    # agenda: buildings still to explore
    agenda = [start_building]
    
    # visited: all buildings ever added to the agenda
    visited = set()
    
    # while there are still buildings to explore...
    while agenda:
        # remove a building from the agenda
        building = agenda.pop(0)
        
        if building == goal_building:
            return True
        
        visited.add(building)
        
        # add each neighbor to agenda
        for neighbor in get_neighbors(building):
            if neighbor not in visited:
                agenda.append(neighbor)
    
    return False


#> Test using small map
small_map = {
    '26': {'36'}, # 26 connects to 36
    '32': {'36'}, # 32 connects to 36
    '36': {'26', '32'}, # 36 connects to both of the others
    '76': set()
}

def test_can_reach_small() -> str:
    assert can_reach(small_map, '26', '32') is True
    assert can_reach(small_map, '36', '36') is True
    assert can_reach(small_map, '76', '32') is False
    
    print("All Correct!")

test_can_reach_small()
