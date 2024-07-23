# How would you initialize the visited set and agenda for the function below?

def general_actor_path(transformed_data, start_actors, goal_test_function):
    # start actors is a set of actor ids representing valid start of path
    actor_map, _ = transformed_data
    
    visited = set()
    agenda = [[actor] for actor in start_actors]

    #> ...
