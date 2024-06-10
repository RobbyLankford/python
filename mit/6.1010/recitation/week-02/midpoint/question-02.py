# Write a function that returns a function that approximates a derivative

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


def foo(x: int) -> int:
    """Exponentiate a value to the third power

    Args:
        x (int): an integer

    Returns:
        int: the integer raised to the third power
    """
    return x ** 3


dfoo = deriv(foo)
num = dfoo(2)
print(num)