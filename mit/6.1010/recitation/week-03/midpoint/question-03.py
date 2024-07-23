def find_path(map: dict, start_building: str, goal_building: str) -> tuple:
    """
    same arguments as can_reach()
    returns path of directly-connected buildings from start_building to
    goal_building, or None if no possible path in map
    """
    
    # helper function to get neighbors of building
    def get_neighbors(building: str) -> set:
        return map[building]
    
    # agenda: buildings still to explore
    agenda = [start_building]
    
    # visited: all buildings ever added to the agenda
    visited = set()
    
    # path: keep track of (possible) directed path tracking from start to goal
    path = []
    
    # while there are still buildings to explore...
    while agenda:
        
        # remove a building from the agenda
        building = agenda.pop(0)
        path.append(building)
        
        if building == goal_building:
            return tuple(path)
        
        visited.add(building)
        
        # add each neighbor to agenda
        for neighbor in get_neighbors(building):
            if neighbor not in visited:
                agenda.append(neighbor)
    
    return None


#> Test using small map
small_map = {
    '26': {'36'}, # 26 connects to 36
    '32': {'36'}, # 32 connects to 36
    '36': {'26', '32'}, # 36 connects to both of the others
    '76': set()
}

def test_find_path_small():
    assert find_path(small_map, '26', '32') == ('26', '36', '32')
    assert find_path(small_map, '36', '36') == ('36',)
    assert find_path(small_map, '76', '32') == None
    
    print("All Correct!")
    
test_find_path_small()