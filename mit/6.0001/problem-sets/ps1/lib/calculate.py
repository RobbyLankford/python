def calculate_months(salary, down_payment, save_rate, int_rate, increase=None):
    """Calculates the number of months to save a specified amount

    Parameters
    ----------
    salary : float 
        Annual salary amount ($).
    down_payment : float
        Down payment amount ($).
    save_rate : float 
        Percentage of salary saved each month (as a decimal).
    int_rate : float 
        Annual interest rate (as a decimal).
    increase : None or float, optional
        Amount by which to increase salary each month (as a decimal). Defaults to None.

    Returns
    -------
    int
        Number of months required to save down payment.
    """
    monthly_int_rate = int_rate / 12
    monthly_salary = salary / 12
    
    savings = 0
    months = 0
    
    ## Until current savings is greater than or equal to the down payment amount
    ## 1. Increment current savings by (1) return on current investment and (2) additional money saved
    ## 2. Increment number of months that have been spent saving money
    while savings < down_payment:
        savings += ( (savings * monthly_int_rate) + (save_rate * monthly_salary) )
        months += 1
        
        if increase is not None:
            if months > 6 and months % 6 == 1:
                monthly_salary = monthly_salary * (1 + increase)
    
    return int(months)


def calculate_savings(salary, months, save_rate, int_rate, increase=None):
    """Calculates the savings amount accumulated over a specified number of months

    Parameters
    ----------
    salary : float 
        Annual salary amount ($).
    months : int
        Number of months in which to save.
    save_rate : float 
        Percentage of salary saved each month (as a decimal).
    int_rate : float 
        Annual interest rate (as a decimal).
    increase : None or float, optional
        Amount by which to increase salary each month (as a decimal). Defaults to None.

    Returns
    -------
    float
        Amount of money saved.
    """
    monthly_salary = salary / 12
    monthly_int_rate = int_rate / 12
    
    savings = 0
    
    ## For the specified number of months
    ## 1. Every six months, increase salary by a specified percentage (optional)
    ## 2. Increment current savings by (1) return on current investment and (2) additional money saved
    for month in range(1, months + 1, 1):
        if increase is not None and month > 6 and month % 6 == 1:
            monthly_salary = monthly_salary * (1 + increase)
        
        savings += ( (savings * monthly_int_rate) + (save_rate * monthly_salary))
    
    return savings