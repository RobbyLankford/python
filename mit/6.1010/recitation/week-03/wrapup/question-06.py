# How can we rewrite bacon_path in terms of actor_to_actor_path?

#> Simply put Kevin Bacon's ID number as actor_id_1 in actor_to_actor_path

def actor_to_actor_path(transformed_data, actor_id_1, actor_id_2):
    start_actor = actor_id_1
    
    if start_actor == actor_id_2:
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

                if coactor == actor_id_2:
                    return new_path

            visited.add(actor)
    
    return None


def bacon_path(transformed_data, actor_id):
    return actor_to_actor_path(transformed_data, actor_id_1=4724, actor_id_2=actor_id)