import operations
import validation

res = 0
operator = num = None

print('Welcome to mini calculator! Provide values to calculate or print X to exit.')

while operator != '=':
    if (res == 0):
        res = validation.val_num()

    operator = validation.val_operator()
    if (operator != '='):
        num = validation.val_num()
        res = operations.calc(res, num, operator)
    print('Result:', res)

