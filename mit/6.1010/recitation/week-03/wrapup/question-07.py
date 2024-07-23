# How can we rewrite actor_to_actor_path in terms of actor_path?

#> Write the goal_test_function as a function that returns True if the input is actor_id_2

def actor_path(transformed_data, actor_id_1, goal_test_function):
    start_actor = actor_id_1

    if goal_test_function(start_actor):
        return [start_actor]
    
    visited = set()

    queue = [[start_actor]]
    while queue:
        path = queue.pop(0)
        actor = path[-1]

        if actor not in visited:
            for coactor in transformed_data[actor]:
                new_path = list(path)
                new_path.append(coactor)
                queue.append(new_path)

                if goal_test_function(coactor):
                    return new_path
                
            visited.add(actor)
    
    return None


def actor_to_actor_path(transformed_data, actor_id_1, actor_id_2):
    return actor_path(transformed_data, actor_id_1, lambda p: p == actor_id_2)