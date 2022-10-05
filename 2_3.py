# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
#  и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

my_list = list(map(int, input("Введите числа в строку через пробел: ").split()))


def mult_list(ent_list):
    len_list = len(ent_list)
    new_list = [(ent_list[i] * ent_list[len_list - i - 1]) for i in range(len_list//2)]
    if len_list % 2 == 1:
        add = ent_list[len_list//2]**2
        new_list.append(add)
    return new_list


print(f'{my_list} => {mult_list(my_list)}')