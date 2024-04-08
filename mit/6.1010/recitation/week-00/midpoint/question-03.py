def make_equal_length(x, y):
    """
    Takes two lists as inputs and checks if they are the same length.
    If they are not the same length, the shorter list is padded with 0 until they are the same length.
    """
    len_x, len_y = len(x), len(y)
    diff = abs(len_x - len_y)
    
    a = x.copy()
    b = y.copy()
    
    if len_x > len_y:
        b.extend([0] * diff)
    elif len_x < len_y:
        a.extend([0] * diff)
    
    return a, b


def poly_subtract(p1, p2):
    """
    Takes two single variable polynomials as input and returns a
    new polynomial representing their p1 - p2. Does not modify inputs.
    Ex: (4x^3 + 7x - 8) - (x^2 + 3x) should result in a polynomial equivalent
    To 4x^3 - x^2 + 4x - 8
    """
    #> Need to make sure polynomial representations are the same length
    a, b = make_equal_length(p1, p2)
    
    return [coef1 - coef2 for coef1, coef2 in zip(a, b)]


def test_poly_subtract():
    """
    Test case checking that poly_add can subtract
    (x^2 + 3x) from (4x^3 + 7x - 8)
    and get
    4x^3 - x^2 + 4x - 8
    """
    p1 = [-8, 7, 0, 4]
    p2 = [0, 3, 1]
    exp = [-8, 4, -1, 4]
    
    exp_p1 = p1.copy()
    exp_p2 = p2.copy()
    
    #> Test if polynomials are subtracted correctly
    assert poly_subtract(p1, p2) == exp
    
    #> Test if inputs have been modified
    assert p1 == exp_p1
    assert p2 == exp_p2


if __name__ == "__main__":
    test_poly_subtract()
    print("done!")