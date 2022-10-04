# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 => 101101
# 3 => 11
# 2 => 10

num = int(input("Введите целое число: "))


def bynary_code(number):
    result_str = ''
    while number != 0:
        num2 = number % 2
        result_str = str(num2) + result_str
        number //= 2
    return result_str


print(f'{num} => {bynary_code(num)}')