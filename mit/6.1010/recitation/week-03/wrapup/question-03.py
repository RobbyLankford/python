# Assuming transformed_data is a dictionary where keys are actor_ids and values are sets of co-start actor_ids

def get_neighbors(transformed_data, actor):
    """
    Gets a set of all of the actors that the provided actor id
    has acted with (not including the given actor).
    """
    coactors = set()
    for act, coacts in transformed_data.items():
        if act == actor:
            for coact in coacts:
                if coact != actor:
                    coactors.add(coact)
        
        if actor in coacts and act != actor:
            coactors.add(act)
    
    return coactors
    

# Check
def test_get_neighbors():
    tiny_db = {
               2876: {4724, 1532, 1640},
               4724: {2876, 1532},
               1532: {2876, 4724, 1532},
               1640: {2876},
    }

    def check(actor, expected):
        # an example of a useful closure function!
        result = get_neighbors(tiny_db, actor)
        assert result == expected, f"unexpected result for actor {actor}\n {result=} != {expected=}"

    check(2876, {4724, 1532, 1640})
    check(4724, {2876, 1532})
    check(1532, {2876, 4724})
    check(1640, {2876})
    check(1, set())
    
    print("All Correct!")

test_get_neighbors()