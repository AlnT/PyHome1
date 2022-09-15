import sys

def calc(res, num, operator):
    if operator == '+':
        return res + num
    elif operator == '-':
        return res - num
    elif operator == '*':
        return res * num
    else:
        try:
            return res / num
        except ZeroDivisionError:
            print('Division by 0 error, result will not be calculated. Bye!')
            sys.exit()





