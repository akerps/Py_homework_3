# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] => на нечётных позициях элементы 3 и 9, ответ: 12

import random

new_arr = [random.randint(0, 9) for i in range(random.randint(3, 12))]
# sum = 0
# for i in range(len(new_arr)):
#     if i % 2 != 0:
#         sum += new_arr[i]

odd_list = [new_arr[i] for i in range(len(new_arr)) if i%2 != 0]

print(f'{new_arr} => сумма элементов на нечетных позициях равна {sum(odd_list)}')
