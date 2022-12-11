# Define Functions
def calculate_savings(salary, down_payment, save_rate, annual_int_rate):
    monthly_int_rate = annual_int_rate / 12
    monthly_salary = salary / 12
    
    savings = 0
    months = 0
    
    ## Until current savings is greater than or equal to the down payment amount
    ## 1. Increment current savings by (1) return on current investment and (2) additional money saved
    ## 2. Increment number of months that have been spent saving money
    while savings < down_payment:
        savings += ( (savings * monthly_int_rate) + (save_rate * monthly_salary) )
        months += 1
    
    return months

# Take in user inputs, cast to floats for later calculations
annual_salary = float(input("Enter your annual salary: $"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: $"))

# Requested constant values
portion_down_payment = 0.25
annual_int_rate = 0.04

# Calculations
down_payment_amount = portion_down_payment * total_cost
months = calculate_savings(annual_salary, down_payment_amount, portion_saved, annual_int_rate)

print("Number of months: ", months)