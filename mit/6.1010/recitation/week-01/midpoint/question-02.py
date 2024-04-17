# Rewrite function to be more pythonic (also try it in one line)
def poly_evaluate(coefficients, x):
    """
    Parameters:
        coefficients: list of floats
        x: float
    
    Returns:
        The value of the polynomial
        coefficients[0]x ^ 0 + coefficients[1]x ^ 1 + ... coefficients[n-1]x ^ (n-1)
    """
    answer = 0
    for i in range(len(coefficients)):
        answer += coefficients[i] * x ** i
    
    return answer

def poly_evaluate_rewrite(coefficients, x):
    answer = 0
    for i, coefficient in enumerate(coefficients):
        answer += coefficient * x ** i
    
    return answer

def poly_evaluate_oneline(coefficients, x):
    return sum([(coefficient * x ** i) for i, coefficient in enumerate(coefficients)])

print(poly_evaluate([7, 1, 3], 2))
print(poly_evaluate_rewrite([7, 1, 3], 2))
print(poly_evaluate_oneline([7, 1, 3], 2))