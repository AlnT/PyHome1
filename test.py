import sys

def val_num():
    num = input('Please, provide number and press enter:\n')
    try:
        return float(num)
    except ValueError:
        if 'X' in num:
            print('Bye!')
            sys.exit()
        else:
            print('Invalid value provided. Please, provide correct number or press X to exit.')
            return(val_num())

m = val_num()
print(m, type(m))