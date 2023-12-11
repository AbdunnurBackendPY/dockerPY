def calc(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/' and b != 0:
        return a / b
    else:
        return


print(calc(5, 3, '+'))
print(calc(5, 3, '-'))
print(calc(5, 3, '*'))
print(calc(5, 3, '/'))
