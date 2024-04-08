# #> Function given
# def poly_add(p1, p2):
#     """
#     Takes two polynomials as input and returns a
#     new polynomial representing their sum. Does not modify inputs.
#     """
#     out = p1.copy()
    
#     for i in range(len(p1)):
#         out[i] += p2[i]
    
#     return out


#> Rewrite function (and helper functions, if needed)
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


def poly_add(p1, p2):
    """
    Takes two polynomials as input and returns a
    new polynomial representing their sum. Does not modify inputs.
    """
    #> Need to make sure polynomial representations are the same length
    a, b = make_equal_length(p1, p2)
    
    return [coef1 + coef2 for coef1, coef2 in zip(a, b)]


def test_poly_add():
    """
    Test case checking that poly_add can add
    x^2 + 3x to 4x^3 + 7x - 8
    and get
    4x^3 + x^2 + 10x - 8
    """
    p1 = [0, 3, 1]
    p2 = [-8, 7, 0, 4]
    exp = [-8, 10, 1, 4]
    
    exp_p1 = p1.copy()
    exp_p2 = p2.copy()
    
    #> Test if polynomials are added correctly
    assert poly_add(p1, p2) == exp
    
    #> Test if inputs have been modified
    assert p1 == exp_p1
    assert p2 == exp_p2


if __name__ == "__main__":
    test_poly_add()
    print("done!")