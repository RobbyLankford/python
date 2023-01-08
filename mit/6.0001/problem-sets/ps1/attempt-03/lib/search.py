from . import calculate

def bisection_search(alist, item, salary, int_rate, increase=None, tolerance = 0):
    """Performs bisection search to find optimal savings rate

    Parameters
    ----------
    alist : list of floats
        A list of savings rate to search.
    item : float
        Down payment amount to find using teh savings rates.
    salary : float 
        Annual salary amount ($).
    int_rate : float 
        Annual interest rate (as a decimal).
    increase : None or float, optional
        Amount by which to increase salary each month (as a decimal). Defaults to None.
    tolerance int, optional
        Tolerance (+/-) to apply to the argument item. Defaults to 0.
    """
    ## Items to keep track of in each iteration
    left = 0
    right = len(alist) - 1
    found = False
    iterations = 0
    position = None
    
    ## While there is still a list of items that can be split in half
    while left <= right and not found:
        ### Count the additional iteration and take the midpoint of the remaining list
        iterations += 1
        midpoint = (left + right) // 2
        check = alist[midpoint]
        
        ### Calculate savings
        monthly_salary = salary / 12
        monthly_int_rate = int_rate / 12
        savings = calculate.calculate_savings(check, 36, int_rate, salary, increase)
        
        # savings = 0
    
        # ## For the specified number of months
        # ## 1. Every six months, increase salary by a specified percentage (optional)
        # ## 2. Increment current savings by (1) return on current investment and (2) additional money saved
        # for month in range(1, 36 + 1, 1):
        #     if increase is not None and month > 6 and month % 6 == 1:
        #         monthly_salary = monthly_salary * (1 + increase)

        #     savings += ( (savings * monthly_int_rate) + (check * monthly_salary))
        
        ### If the savings is between the tolerance, we have found our desired result
        ### Otherwise, we either need to check the left or right of the list and throw out the opposite side
        if savings >= (item - tolerance) and savings <= (item + tolerance):
            position = midpoint
            found = True
        elif savings > (item - tolerance):
            right = midpoint - 1
        elif savings < (item + tolerance):
            left = midpoint + 1
        else:
            break
    
    ## Print Results
    if found:
        print("Best savings rate:", alist[position])
        print("Steps in bisection search:", iterations)
    else:
        print("It is not possible to pay the down payment in three years.")