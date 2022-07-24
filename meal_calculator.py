"""
Author: Efrain Gomez Fajardo
Teacher: Comeau, Luc
Purpose: Meal price calculator
"""
print("\nComeau's restaurant\n" + '-' *  40)
# Asking the user for the information
child_meal = float(input("What's the price of a child's meal? "))
adult_meal = float(input("What's the price of an adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
tax_rate = float(input("What's the sales tax rate? "))

# Doing the math and displaying back the result
subtotal = (child_meal * children) + (adult_meal * adults)
sale_tax = (subtotal * tax_rate) / 100
total = sale_tax + subtotal
print(f'\nSubtotal: ${subtotal:.2f}\nSales Tax: ${sale_tax:.2f}\nTotal: ${total:.2f}')
payment = float(input('\nWhat is the payment amount? '))
change = payment - total
print(f'Change: ${change:.2f}')
print('\nThank you for coming today!\nHope to see you again soon!\n' + '-' * 40)