from utils import calc

# Объявляем переменную n, которая равна списку значений.
# Значения в виде раскрытого генератора чисел, начинающегося с 4 до 5, не доходящего до 6.
# То есть у range(4,6) = 4;5 два числа в очереди.
n = [*range(4,6)]

# Так как у нас n является списком, то для получения значений надо указать индексы: 0 и 1
# После равенства выводим результат функции calc(*n), причем фукнция должна принимать 2 значения
# (из файла utils.py). Передаем раскрытый список, состоящий из двух элементов, в аргументы функции
print(f'{n[0]} + {n[1]} = {calc(*n)}')