import random
from arrayutils import ArrayUtils
from searchutils import SearchUtils
from sortutils import SortUtils
import time


def main():
    print_array = False
    array = ArrayUtils.prepare_array(100000)

    # Сортировка выбором
    # array_direct = array.copy()
    # if print_array:
    #     ArrayUtils.print_array(array, 'Изначальный массив:\n')
    # start_time = time.time()
    # SortUtils.direct_sort(array_direct)
    # timer = time.time() - start_time
    # if print_array:
    #     ArrayUtils.print_array(array_direct, 'Сортировка выбором\n')
    # print(f'Сортировка выбором заняла секунд: {round(timer, 3)}')

    # Быстрая сортировка
    array_quick_sort = array.copy()
    start_time = time.time()
    SortUtils.quick_sort(array_quick_sort)
    timer = time.time() - start_time
    if print_array:
        ArrayUtils.print_array(array_quick_sort, 'Быстрая сортировка\n')
    print(f'Быстрая сортировка заняла секунд: {round(timer, 3)}', end=f'\n{"-" * 80}\n')

    # Системная сортировка
    array_system_sorted = array.copy()
    start_time = time.time()
    array_system_sorted.sort()
    timer = time.time() - start_time
    if print_array:
        ArrayUtils.print_array(array_system_sorted, 'Системная сортировка\n')
    print(f'Системная сортировка заняла секунд: {round(timer, 3)}', end=f'\n{"-" * 80}\n')

    # Бинарный поиск
    # array_binary = [12, -1, -12, 8, 99, 7, 4, 15]
    # array_binary.sort()
    # ArrayUtils.print_array(array_binary, 'Массив:\n')
    # search_value = 12
    # print(f"Искомое значение: {search_value}")
    # res = SearchUtils.binary_search(array_binary, search_value)
    # print(f"Находится на позиции в массиве по индексу: {res}" if res != -1 else "Не найдено", end=f'\n{"-" * 80}\n')

    array_heap_sort = array.copy()
    start_time = time.time()
    SortUtils.heap_sort(array_heap_sort)
    timer = time.time() - start_time
    if print_array:
        ArrayUtils.print_array(array_system_sorted, 'Пирамидальная сортировка\n')
    print(f'Пирамидальная сортировка заняла секунд: {round(timer, 3)}', end=f'\n{"-" * 80}\n')


if __name__ == "__main__":
    main()
