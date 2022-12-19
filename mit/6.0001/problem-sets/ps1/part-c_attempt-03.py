# Import custom module
from lib.search import bisection_search

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

# Calculations & Print Answer
bisection_search(save_rates, down_payment_amount, annual_int_rate, annual_salary, semi_annual_raise, tolerance)