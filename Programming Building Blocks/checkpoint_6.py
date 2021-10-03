"""
Loan thingy
"""
print('Please evaluate the following questions from 1=10:\n')
loan = int(input('How large is the loan? '))
credit_history = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? '))

if loan >= 5:
    if credit_history >= 7 and income >= 7:
        decision = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            decision = True
        else:
            decision = False
    else:
        decision = False
else:
    if credit_history < 4:
        decision = False
    else:
        if down_payment >= 7 or income >= 7:
            decision = True
        if down_payment >= 4 and income >= 4:
            decision = True
        else:
            decision = False

if decision:
    print('You have been approved')
else:
    print('Not happening bro')
