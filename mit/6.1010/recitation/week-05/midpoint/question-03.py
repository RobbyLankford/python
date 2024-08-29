# Fill in the body of the `all_phrases` function below

grammar = {
    "sentence": [["noun", "verb"], ["noun", "never", "verb"]],
    "noun": [["pigs"], ["professors"]],
    "verb": [["fly"], ["think"]],
    "greeting": [["hi", "noun"]],
    "question": [["sentence", "?"]],
}

def all_phrases(grammar, root):
    """
    Using rule lists in the grammar dict, expand root into all possible
    phrases. Each phrase is a tuple of terminal word strings.
    Return a set of all valid phrases.
    """
    
    #> Base case: root is not a terminal word
    if root not in grammar:
        return {tuple([root])}

    #> Recursive case: iterate through each rule associated with the root
    phrases = set()
    for rules in grammar[root]:
        sub_phrases = {()}
        for rule in rules:
            rec_phrases = all_phrases(grammar, rule)
            sub_phrases = {x + y for x in sub_phrases for y in rec_phrases}
    
        phrases.update(sub_phrases)

    return phrases


all_phrases(grammar, "pigs")
all_phrases(grammar, "question")


assert all_phrases(grammar, "pigs") == {("pigs", )}

expected = {("pigs", "fly", "?"), ("pigs", "think", "?"),
    ("professors", "fly", "?"), ("professors", "think", "?"),
    ("pigs", "never", "fly", "?"), ("pigs", "never", "think", "?"),
    ("professors", "never", "fly", "?"), ("professors", "never", "think", "?"),
}
assert all_phrases(grammar, "question") == expected
