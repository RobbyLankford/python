# Define Variables
annual_salary = float(input("Enter the starting salary: $"))

# Define Constants
total_cost = 1e6
semi_annual_raise = 0.07
portion_down_payment = 0.25
annual_int_rate = 0.04
tolerance = 100

monthly_int_rate = annual_int_rate / 12
down_payment_amount = total_cost * portion_down_payment
save_rates = [( (i + 1) / 10000 ) for i in range(10000)]

# Bisection Search
left = 0
right = len(save_rates) - 1
found = False
iterations = 0
position = None

while left <= right and not found:
    monthly_salary = annual_salary / 12
    
    iterations += 1
    midpoint = (left + right) // 2
    check = save_rates[midpoint]
    
    ## Calculate Savings
    savings = 0
    for month in range(1, 37):
        if (month > 6) and (month % 6 == 1):
            monthly_salary = monthly_salary * (1 + semi_annual_raise)
        
        savings += ( (savings * monthly_int_rate) + (check * monthly_salary))
    
    ## Check List of Savings Rate
    if savings >= (down_payment_amount - tolerance) and savings <= (down_payment_amount + tolerance):
        position = midpoint
        found = True
    elif savings > (down_payment_amount - tolerance):
        right = midpoint - 1
    elif savings < (down_payment_amount + tolerance):
        left = midpoint + 1
    else:
        break

# Print Results
if found:
    print("Best savings rate:", save_rates[position])
    print("Steps in bisection search:", iterations)
else:
    print("It is not possible to pay the down payment in three years.")