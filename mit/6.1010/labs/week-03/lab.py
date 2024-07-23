"""
6.101 Lab 3:
Bacon Number
"""

#!/usr/bin/env python3

import pickle

# NO ADDITIONAL IMPORTS ALLOWED!

# Constants
KEVIN_BACON_ID = 4724

# Helper/Development Functions
def get_name_from_id(id: int, db: dict[str: int]) -> str:
    """Extract the name of an actor given their ID number

    Args:
        id (int): the ID number of the actor
        db (dict): a dictionary mapping ID number to a name

    Returns:
        str: the name of the actor (or None if they are not in the database)
    """
    for name, idx in db.items():
        if idx == id:
            return name
    
    return None

def get_id_from_name(name: str, db: dict[str: int]) -> int:
    """Extract the ID number of an actor given their name

    Args:
        name (str): the name of the actor
        db (dict): a dictionary mapping ID number to a name

    Returns:
        int: the ID number of the actor (or None if they are not in the database)
    """
    return db.get(name)


# Transform Data
def transform_data(raw_data: list[tuple[int]]) -> dict[int: set[int]]:
    """Transform raw actor data

    Args:
        raw_data (list): a list of the form (actor1, actor2, film)

    Returns:
        dict: the input data rearranged to show a set of coactors for each actor
    """
    transformed_data = {}
    for actor1, actor2, film in raw_data:
        if actor1 not in transformed_data:
            transformed_data[actor1] = set()
        if actor2 not in transformed_data:
            transformed_data[actor2] = set()
        
        if actor1 == actor2:
            continue

        transformed_data[actor1].add(actor2)
        transformed_data[actor2].add(actor1)
    
    return transformed_data


# Acted Together
def acted_together(transformed_data: dict[int: set[int]], actor_id_1: int, actor_id_2: int) -> bool:
    """Determine if a set of actors has acted together

    Args:
        transformed_data (dict): The output of `transform_data()`
        actor_id_1 (int): the ID number of the first actor
        actor_id_2 (int): the ID number of the second actor

    Returns:
        bool: True, if the actors have been on-screen together, or False otherwise
    """
    if actor_id_1 == actor_id_2:
        return True
    
    for actor, coactors in transformed_data.items():
        if actor == actor_id_1 and actor_id_2 in coactors:
            return True
    
    return False


# Bacon Number
def actors_with_bacon_number(transformed_data: dict[int: set[int]], n: int) -> set[int]:
    """Find the set of all actors with a specific Bacon Number

    Args:
        transformed_data (dict): the output of `transform_data()`
        n (int): a specific Bacon Number (>= 0)

    Returns:
        set[int]: The set of all actor IDs that have the specified bacon number
    """
    if n == 0:
        return {KEVIN_BACON_ID}

    visited = set()
    visited.add(KEVIN_BACON_ID)

    queue = [(KEVIN_BACON_ID, 0)]
    while queue:
        actor, bacon_num = queue.pop(0)

        if bacon_num == n:
            result = {act for act, num in queue if num == n}
            result.add(actor)

            return result
        
        for coactor in transformed_data[actor]:
            if coactor not in visited:
                visited.add(coactor)
                queue.append((coactor, bacon_num + 1))

    return set()


# Bacon Path
def bacon_path(transformed_data: dict[int: set[int]], actor_id: int) -> list[int]:
    """Find the shortest list of actors that link a specific actor to Kevin Bacon

    Args:
        transformed_data (dict): The output of `transform_data()`
        actor_id (int): The ID number of an actor

    Returns:
        list[int]: The shortest possible list of Actor IDs that link Kevin Bacon to `actor_id`
    """
    start_actor = KEVIN_BACON_ID
    
    if start_actor == actor_id:
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

                if coactor == actor_id:
                    return new_path

            visited.add(actor)
    
    return None


# Actor to Actor Path
def actor_to_actor_path(transformed_data: dict[int: set[int]], actor_id_1: int, actor_id_2: int) -> list[int]:
    """Find the shortest list of actors that link a specific actor to another actor

    Args:
        transformed_data (dict): The output of `transform_data()`
        actor_id_1 (int): The ID number of an actor
        actor_id_2 (int): The ID number of another actor

    Returns:
        list[int]: The shortest possible list of Actor IDs that link Actor 1 to Actor 2
    """
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


# Movie Path
def actor_to_actor_movie_path(raw_data: list[tuple[int]], actor_id_1: int, actor_id_2: int, movies: dict[int: str]) -> list[str]:
    """Find the shortest list of movies that link a specific actor to another actor

    Args:
        raw_data (list[tuple[int]]):  a list of the form (actor1, actor2, film)
        actor_id_1 (int): The ID number of an actor
        actor_id_2 (int): The ID number of another actor
        movies (dict): A dictionary of movie information that maps a movie ID number to its name

    Returns:
        list[str]: The shortest possible list of movie names that link Actor 1 to Actor 2
    """
    path = actor_to_actor_path(transform_data(raw_data), actor_id_1, actor_id_2)

    films = []
    for i in range(len(path) - 1):
        act1 = path[i]
        act2 = path[i + 1]

        for actor1, actor2, film in raw_data:
            if (act1 == actor1 or act1 == actor2) and (act2 == actor1 or act2 == actor2):
                for film_name, film_id in movies.items():
                    if film_id == film:
                        films.append(film_name)
    
    return films


# Generalized Actor Path
def actor_path(transformed_data: dict[int: set[int]], actor_id_1: int, goal_test_function: callable) -> list[int]:
    """A generalized method of creating a list of actors that meet some specific requirement

    Args:
        transformed_data (dict): The output of `transform_data()`
        actor_id_1 (int): The ID number of an actor
        goal_test_function (callable): Some function that takes in an actor ID number and returns True or False

    Returns:
        list[int]: The shortest possible list of actors from Actor 1 to an actor that satisfies the supplied function
    """
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


if __name__ == "__main__":
    # 2. Introduction
    
    ## 2.1 The Film Database
    with open("resources/tiny.pickle", "rb") as f:
        tinydb = pickle.load(f)
    
    with open("resources/small.pickle", "rb") as f:
        smalldb = pickle.load(f)
    
    with open("resources/large.pickle", "rb") as f:
        largedb = pickle.load(f)
    
    ## 2.2 The Names Database
    with open("resources/names.pickle", "rb") as f:
        names = pickle.load(f)
    
    # print(names.get("Samir Bannout")) #> 35708
    # print(list(names.keys())[list(names.values()).index(94500)]) #> Jason Hervey

    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used, for example, to generate the results for the online questions.


    # 3. Transforming the Data
    tinydb_transformed = transform_data(tinydb)
    smalldb_transformed = transform_data(smalldb)
    largedb_transformed = transform_data(largedb)
    
    
    # 4. Acting Together
    # print(get_id_from_name("Tony Shalhoub", names)) #> 4252
    # print(get_id_from_name("Daphne Rubin-Vega", names)) #> 9209
    # print(acted_together(smalldb_transformed, 4252, 9209))
    
    # print()
    
    # print(get_id_from_name("Jean-Marc Roulot", names)) #> 931399
    # print(get_id_from_name("Noureddine El Ati", names)) #> 1190299
    # print(acted_together(smalldb_transformed, 931399, 1190299))
    
    
    # 5. Bacon Number
    # print(actors_with_bacon_number(tinydb_transformed, n=0))
    # print(actors_with_bacon_number(tinydb_transformed, n=1))
    # print(actors_with_bacon_number(tinydb_transformed, n=2))
    # print(actors_with_bacon_number(tinydb_transformed, n=3))
    
    # print()
    
    # print(actors_with_bacon_number(largedb_transformed, n=6))
    
    
    # 6. Paths
    
    ## 6.1 Bacon Paths
    # print(bacon_path(largedb_transformed, actor_id=1204))
    
    # print(bacon_path(tinydb_transformed, actor_id=1604))
    
    # print(get_id_from_name("Nilo Mur", db=names)) #> 31389
    # print(bacon_path(largedb_transformed, 31389))
    
    ## 6.2 Arbitrary Paths
    # print(get_id_from_name("Daniel McCabe", names)) #> 1288959
    # print(get_id_from_name("Jessica James", names)) #> 75195
    # print(actor_to_actor_path(largedb_transformed, 1288959, 75195))
    
    
    # 7. Movie Paths
    with open("resources/movies.pickle", "rb") as f:
        movies = pickle.load(f)

    # print(get_id_from_name("Dustin Hoffman", names)) #> 4483
    # print(get_id_from_name("Anton Radacic", names))  #> 1345461
    # print(actor_to_actor_movie_path(largedb, 4483, 1345461, movies))
    