# Write a function that returns a function that approximates the n-th derivative

def deriv(f: callable, dx:float = 0.001) -> callable:
    """
    Given a function f of one variable (which takes a float value
    and returns a float value)

    Returns a function that approximates the derivative df/dx.

    Optional parameter dx > 0 is the width of the approximation
    """
    def df(x: float) -> float:
        """Approximates the derivative of a function evaluated at a value.
           
           f'(x) = (f(x + h) - f(x - h)) / 2h

        Args:
            x (float): an input number to evaluate

        Returns:
            float : the approximated derivative
        """
        return (f(x + dx) - f(x - dx)) / (2 * dx)
    
    return df


def nth_derivative(f: callable, n: int) -> callable:
    """
    Given a function f of one variable (takes a float value and
    returns a float value)
    returns a function that approximates the nth derivative of f.
    """
    if n == 0:
        return f
    
    dfunc = deriv(f)
    for _ in range(n - 1):
        dfunc = deriv(dfunc)
    
    return dfunc


def foo(x: int) -> int:
    """Exponentiate a value to the third power

    Args:
        x (int): an integer

    Returns:
        int: the integer raised to the third power
    """
    return x ** 3


deriv0 = nth_derivative(foo, 0)
print(deriv0(2)) #> x^3: 2^3 = 8

deriv1 = nth_derivative(foo, 1)
print(deriv1(2)) #> 3x^2: 3(2^2) = 12

deriv2 = nth_derivative(foo, 2)
print(deriv2(2)) #> 6x: 6(2) = 12

deriv3 = nth_derivative(foo, 3)
print(deriv3(2)) #> 6

deriv4 = nth_derivative(foo, 4)
print(deriv4(2)) #> 0