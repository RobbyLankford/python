# Assuming transformed_data is a list of (actor_id_1, actor_id_2, film_id)

def get_neighbors(transformed_data, actor):
    """
    Gets a set of all of the actors that the provided actor id
    has acted with (not including the given actor).
    """
    actors = set()
    for act1, act2, film in transformed_data:
        if act1 == actor and act2 != actor:
            actors.add(act2)
        
        if act2 == actor and act1 != actor:
            actors.add(act1)
    
    return actors


# Check
def test_get_neighbors():
    tiny_db = [
        (2876, 4724, 617),
        (4724, 1532, 31932),
        (1532, 1532, 31932),
        (1532, 4724, 617),
        (1532, 2876, 31932),
        (2876, 1640, 617),
        (1640, 1640, 74881)
    ]

    def check(actor, expected):
        result = get_neighbors(tiny_db, actor)
        assert result == expected, f"unexpected result for actor {actor}\n {result=} != {expected=}"

    check(2876, {4724, 1532, 1640})
    check(4724, {2876, 1532})
    check(1532, {2876, 4724})
    check(1640, {2876})
    check(1, set())
    
    print("All Correct!")

test_get_neighbors()