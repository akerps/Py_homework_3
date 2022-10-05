# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] (Негафибоначчи)

num = int(input('Введите целое число: '))

def fibonacci(n):
    fib_list = [1, 1]
    negof_list = [1, -1]
    result_list = []
    for i in range(2, n):
        add_fib = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(add_fib)
    for j in range(2, n):
        add_negof = negof_list[j - 2] - negof_list[j - 1]
        negof_list.append(add_negof)
    negof_list.reverse()
    negof_list.append(0)
    result_list = negof_list + fib_list
    
    return result_list

print(f'Для k = {num} список => {fibonacci(num)}')