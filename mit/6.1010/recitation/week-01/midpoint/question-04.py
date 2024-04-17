# Rewrite functions in one line using sorted and string builtins

#> Function 1
def color_str(colors):
    """Takes a list of colors, sorts them alphabetically
    and places them in a string separated by spaces"""
    # how can we write this in one line?
    new_colors = colors.copy()
    new_colors.sort()
    result = " "
    for color in new_colors:
        result += color + " "
    
    while result[0] == " ":
        result = result[1:] # remove beginning spaces
    while result[-1] == " ":
        result = result[:-1] # remove trailing spaces
    
    return result

def color_str_oneline(colors):
    return ' '.join(sorted(colors))

# print(color_str(["red", "yellow", "green"]))
# print(color_str_oneline(["red", "yellow", "green"]))

# print()

#> Function 2
def word_lst(word_str):
    """Take a string of words separated by spaces and
    make a list of individual word strings"""
    # how can we write this in one line?
    words = []
    cur = ""
    for char in word_str:
        if char == " ":
            words.append(cur)
            cur = ""
        else:
            cur += char
    if cur:
        words.append(cur)
    return words

def word_lst_oneline(word_str):
    return word_str.split()

# print(word_lst("this is a sentence"))
# print(word_lst_oneline("this is a sentence"))

# print()

#> Function 3
def sort_word_len(word_lst):
    """Given a list of words, create a new list where the
    words are sorted from longest to shortest"""
    return sorted(word_lst, key=len, reverse=True)

# print(sort_word_len(['blue', 'chartreuse', 'green', 'periwinkle', 'red', 'yellow']))

#> Function 4
def sort_movies(movies, ratings):
    """
    Return a new list of movies sorted by the rating from
    lowest to highest
    """
    return [movie for rating, movie in sorted(zip(ratings, movies))]

# print(sort_movies(["Alien", "Barbie", "Clue", "Frozen", "Inception"], [7.3, 8.4, 7.2, 7.4, 8.5]))

# ---

def check(result, expected):
    if isinstance(expected, float):
        assert abs(result - expected) <= 1e-6, f'got {result=} but {expected=}'
    else:
        assert result == expected, f'got {result=} but {expected=}'

if __name__ == "__main__":
    movies = ["Alien", "Barbie", "Clue", "Frozen", "Inception"]
    ratings = [7.3,       8.4,     7.2,     7.4,       8.5]
    colors = ["red", "green", "blue", "yellow", "chartreuse", "periwinkle"]

    exp_str = 'blue chartreuse green periwinkle red yellow'
    check(color_str(colors), exp_str)
    
    exp_lst = ['blue', 'chartreuse', 'green', 'periwinkle', 'red', 'yellow']
    check(word_lst(exp_str), exp_lst)
    
    len_lst = ['chartreuse', 'periwinkle', 'yellow', 'green', 'blue', 'red']
    check(sort_word_len(colors), len_lst)
    
    exp_movies = ['Clue', 'Alien', 'Frozen', 'Barbie', 'Inception']
    check(sort_movies(movies, ratings), exp_movies)

    print("all correct!")