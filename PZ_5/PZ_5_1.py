# Составить функцию решения задачи: из заданного числа вычли сумму его цифр.
# Из результата вновь вычли сумму его цифр и т.д. Через сколько таких действий получится нуль?
def subtract_digit_sum():
 try:
    count = 0 # кол-во действий
    a = int(input("Введите любое целое число: "))   # заданное число
    if a > 0:
      while a > 0:
        sum_digits = sum(int(digit) for digit in str(a)) # суммирование цифр в числе
        a -= sum_digits # вычитание
        count += 1
      print("Число обнулится через ",count," действий")
    else: print("Число не должно быть отрицательным")
 except ValueError:
    print('Данные введены неверно')

subtract_digit_sum() # вызов функции







