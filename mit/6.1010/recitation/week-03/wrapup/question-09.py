# How would you initialize the visited set and agenda for the function below?

def super_general_actor_path(transformed_data, start_test_function, goal_test_function):
    '''
    start_test_function(actor_id) returns true if actor_id
    is a valid actor to start path from, false otherwise
    '''
    actor_map, _ = transformed_data

    visited = set()
    agenda = [actor for actor in actor_map if start_test_function(actor)]

    #> ...