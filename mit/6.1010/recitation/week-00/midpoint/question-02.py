def poly_mul(p1, p2):
    """
    Takes two single variable polynomials as input and returns a
    new polynomial representing their product. Does not modify inputs.
    
    Ex: multiplying 6x^7 + 2x^4 + 5x^3 by 4x^2 + 3x should result in the
    polynomial equivalent of 24x^9 + 18x^8 + 8x^6 + 26x^5 + 15x^4
    """
    len_p1, len_p2 = len(p1), len(p2)
    out = [0] * (len_p1 + len_p2 - 1)
    
    for i in range(len_p1):
        for j in range(len_p2):
            out[i + j] += (p1[i] * p2[j])
    
    return out


def test_poly_mul():
    """
    Test case checking that poly_mul can multiply
    6x^7 + 2x^4 + 5x^3 by 4x^2 + 3x
    and get
    24x^9 + 18x^8 + 8x^6 + 26x^5 + 15x^4
    """
    p1 = [0, 0, 0, 5, 2, 0, 0, 6]
    p2 = [0, 3, 4]
    exp = [0, 0, 0, 0, 15, 26, 8, 0, 18, 24]
    
    exp_p1 = p1.copy()
    exp_p2 = p2.copy()
    
    #> Test if polynomials are multiplied correctly
    assert poly_mul(p1, p2) == exp
    
    #> Test if inputs have been modified
    assert p1 == exp_p1
    assert p2 == exp_p2


if __name__ == "__main__":
    test_poly_mul()
    print("done!")