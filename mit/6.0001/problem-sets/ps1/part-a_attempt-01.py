# Take in user inputs, cast to floats for later calculations
annual_salary = float(input("Enter your annual salary: $"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: $"))

# Requested constant values
portion_down_payment = 0.25
annual_int_rate = 0.04

# Calculations
down_payment_amount = portion_down_payment * total_cost
monthly_int_rate = annual_int_rate / 12
monthly_salary = annual_salary / 12

# Initial values for iteration
current_savings = 0
months = 0

while current_savings < down_payment_amount:
    # Until current savings is greater than or equal to the down payment amount
    # 1. Increment current savings by (1) return on current investment and (2) additional money saved
    # 2. Increment number of months that have been spent saving money
    current_savings += ( (current_savings * monthly_int_rate) + (portion_saved * monthly_salary) )
    months += 1

print("Number of months: ", months)
