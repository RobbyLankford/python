def find_path(neighbors_function, start, goal_test):
    if goal_test(start):
        return (start, )

    agenda = [start]

    # every visited state is a key in visited_from, whose value is the state that led us to it
    # That way we can reconstruct the path from the final state by a series of
    # visited_from[state] lookups.
    visited_from = { start: None }
    def reconstruct_path_to(state):
        path = (state,)
        while visited_from[state]:
            state = visited_from[state]
            path = (state,) + path
        return path

    while agenda:
        state = agenda.pop(0)

        for neighbor in neighbors_function(state):
            if neighbor not in visited_from:
                visited_from[neighbor] = state

                if goal_test(neighbor):
                    return reconstruct_path_to(neighbor)

                agenda.append(neighbor)

