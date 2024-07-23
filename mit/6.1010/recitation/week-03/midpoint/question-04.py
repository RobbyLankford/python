# Write can_read() in terms of find_path()
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


def can_reach(map: dict, start_building: str, goal_building: str) -> bool:
    """Implementation of can_read() by using find_path()

    Args:
        map (dict): a dictionary that represents buildings and their neighbors
        start_building (str): the building to start
        goal_building (str): to the building to reach

    Returns:
        bool: True, if the goal building can be reached directly from the start building, False otherwise
    """
    path = find_path(map, start_building, goal_building)
    
    return path is not None


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