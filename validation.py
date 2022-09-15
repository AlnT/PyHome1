import sys

def corr_oper(ch):
    vsym = ['+', '-', '/', '*', '=']
    for i in vsym:
        if i == ch:
            return 1
    return 0

def val_num():
    try:
        num = input('Please, provide number and press enter:\n')
        return float(num)
    except ValueError:
        if 'X' in num:
            print('Bye!')
            sys.exit()
        else:
            print('Invalid value provided. Please, provide correct number or press X to exit.')
            return(val_num())


def val_operator():
    str = input('Please, provide allowed operation (+ - = / *) and press enter:\n')
    if (corr_oper(str)):
        return str
    elif('X' in str):
        print('Bye!')
        sys.exit()
    else:
        print('Invalid value provided. Please, provide correct operation (+ - = / *) or press X to exit.')
        return(val_operator())

