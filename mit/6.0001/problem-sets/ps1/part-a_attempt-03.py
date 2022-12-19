# Import custom module
from lib.calculate import calculate_months

# Take in user inputs, cast to floats for later calculations
annual_salary = float(input("Enter your annual salary: $"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: $"))

# Requested constant values
portion_down_payment = 0.25
annual_int_rate = 0.04

# Calculations
down_payment_amount = portion_down_payment * total_cost
months = calculate_months(annual_salary, down_payment_amount, portion_saved, annual_int_rate)

# Print Answer
print("Number of months:", months)