# Compare the results of the derivative function (in question 2) to actual expected derivative

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


dfoo = deriv(foo) # approximate 3x^2
ddfoo = deriv(dfoo) # approximate 6x


def compare(f, g, x_values):
    for x in x_values:
        print(f'{x=} {f(x)=} {g(x)=}')


def act1(x: int) -> int:
    """Actual derivative function of x^3: 3x^2

    Args:
        x (int): an integer

    Returns:
        int: the integer, raised to the second power, and multiplied by 3
    """
    return 3 * (x ** 2)


def act2(x: int) -> int:
    """Actual second derivative of x^3: 6x

    Args:
        x (int): an integer

    Returns:
        int: the integer multiplied by 6
    """
    return 6 * x


compare(dfoo, act1, range(-10, 10))
print()
compare(ddfoo, act2, range(-10, 10))