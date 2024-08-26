# BFS with a visited list -
# states don't have to be hashable but
# large inputs are very slow!

def find_path(neighbors_function, start, goal_test):
    """
    Return the shortest path through a graph from a given starting state to any
    state that satisfies a given goal condition.

    Parameters:
      * neighbors_function(state) is a function which returns a list of legal
        neighbor states
      * start is the starting state for the search
      * goal_test(state) is a function which returns True if the given state is
        a goal state for the search, and False otherwise.

    Returns:
        A shortest path from start to a state satisfying goal_test(state)
        as a tuple of states, or None if no path exists.
    """

    agenda = [(start,)]
    visited = []

    if goal_test(start):
        return (start,)

    while agenda:
        this_path = agenda.pop(0)
        terminal_state = this_path[-1]

        for neighbor in neighbors_function(terminal_state):
            if neighbor not in visited:
                new_path = this_path + (neighbor,)

                if goal_test(neighbor):
                    return new_path

                agenda.append(new_path)
                visited.append(neighbor)
