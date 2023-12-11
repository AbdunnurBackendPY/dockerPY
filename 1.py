a = int(input('Введите число'))
b = int(input('Введите число'))
c = int(input('Введите число'))


sum_result = a + b + c
product_result = a * b * c


if sum_result % 2 == 0 and product_result % 2 == 0:
    print("Всё хорошо")
else:
    print("Мы не можем показать вам результат. Приходите позже!")