# Define Functions
def calculate_saved_amount(save_rate, months, int_rate, salary, raise_rate):
    monthly_salary = salary / 12
    monthly_int_rate = int_rate / 12
    
    savings = 0
    
    ## For the specified number of months
    ## 1. Every six months, increase salary by a specified percentage (optional)
    ## 2. Increment current savings by (1) return on current investment and (2) additional money saved
    for month in range(1, months + 1, 1):
        if month > 6 and month % 6 == 1:
            monthly_salary = monthly_salary * (1 + raise_rate)
        
        savings += ( (savings * monthly_int_rate) + (save_rate * monthly_salary))
    
    return savings

# Bisection Search
def bisection_search(alist, item, annual_int_rate, annual_salary, semi_annual_raise, tolerance = 0):
    
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
        savings = calculate_saved_amount(check, 36, annual_int_rate, annual_salary, semi_annual_raise)
        
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
        print("Best savings rate:", save_rates[position])
        print("Steps in bisection search:", iterations)
    else:
        print("It is not possible to pay the down payment in three years.")

# Define Variables
annual_salary = float(input("Enter the starting salary: $"))

# Define Constants
total_cost = 1e6
semi_annual_raise = 0.07
portion_down_payment = 0.25
annual_int_rate = 0.04
tolerance = 100

down_payment_amount = total_cost * portion_down_payment
save_rates = [( (i + 1) / 10000 ) for i in range(10000)]

# Calculations
bisection_search(save_rates, down_payment_amount, annual_int_rate, annual_salary, semi_annual_raise, tolerance)