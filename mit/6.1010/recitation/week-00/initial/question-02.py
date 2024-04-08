#> Write code for function
def reverse_all(inp):
    """
    Given a list of lists, return a new list of lists
    but with all of the inner lists reversed, without
    modifying the input list
    """
    return [item[::-1] for item in inp]


#> Test case(s)
def test_reverse_all():
    #> Case given: the list of lists is correctly reversed
    x = [[1, 2], [3, 4]]
    
    result = reverse_all(x)
    expected = [[2, 1], [4, 3]]
    
    assert result == expected
    
    #> Additional case needed: the input list is not modified
    assert x != result


if __name__ == "__main__":
    test_reverse_all()
    print("done!")