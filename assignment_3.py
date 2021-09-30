"""
Author: Efrain Gomez Fajardo
Teacher: Comeau, Luc
Purpose: Calculate the total for a meal
"""

# Asking the user for the information
child_meal = float(input("What's the price of a child's meal? "))
adult_meal = float(input("What's the price of an adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
tax_rate = float(input("What's the sales tax rate? "))

# Doing the math
subtotal = (child_meal * children) + (adult_meal * adults)
sale_tax = (subtotal * tax_rate) / 100
total = subtotal + sale_tax
print(f'\nSubtotal: ${subtotal}\nSales Tax: ${sale_tax:.2f}\nTotal: ${total:.2f}')
payment = float(input("\nWhat's the payment amount? "))
change = payment - total
print(f'\nChange: ${change:.2f}')