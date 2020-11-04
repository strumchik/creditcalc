import math
import sys


def calculate():
    argdict = {'type': '', 'principal': 0, 'periods': 0, 'interest': 0, 'payment': 0}
    for arg in args[1:]:
        s1, s2 = arg.split('=')
        argdict[s1[2:]] = s2
    loan = int(argdict['principal'])
    periods = int(argdict['periods'])
    i = float(argdict['interest']) / 1200
    anpay = float(argdict['payment'])
    if argdict['type'] == 'diff' and argdict['principal'] and argdict['periods'] and argdict['interest']:
        paid = 0
        for j in range(1, periods + 1):
            d = math.ceil(loan / periods + i * (loan - loan * (j - 1) / periods))
            paid += d
            print(f'Month {j}: payment is {d}')
        print(f'Overpayment = {paid - loan}')
    elif argdict['type'] == 'annuity' and argdict['payment'] and argdict['periods'] and argdict['interest']:
        loan = math.floor(anpay / (i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1)))
        print(f'Your loan principal = {loan}!\nOverpayment = {anpay * periods - loan}')
    elif argdict['type'] == 'annuity' and argdict['payment'] and argdict['principal'] and argdict['interest']:
        periods = math.ceil(math.log(anpay / (anpay - loan * i), i + 1))
        y, m = divmod(periods, 12)
        print(
            f"It will take {bool(y) and str(y) + ' year'}{bool(y - 1) and 's'} {bool(y) and 'and'} {bool(m) and str(m) + ' month'}{bool(m - 1) and 's'} to repay the loan!")
        print(f'Overpayment = {anpay * periods - loan}')
    elif argdict['type'] == 'annuity' and argdict['periods'] and argdict['principal'] and argdict['interest']:
        anpay = math.ceil(loan * i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1))
        print(f'Your annuity payment = {anpay}!\nOverpayment = {anpay * periods - loan}')
    else:
        print('Incorrect parameters.')


args = sys.argv
calculate()
