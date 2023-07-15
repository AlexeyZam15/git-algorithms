class SortUtils:
    """Сортировка выбором"""

    @staticmethod
    def direct_sort(array: list[int]):
        for i in range(len(array) - 1):
            save_index = i
            for j in range(i + 1, len(array)):
                if array[j] < array[save_index]:
                    save_index = j
            if save_index != i:
                array[i], array[save_index] = array[save_index], array[i]
                """array[i] += array[save_index]
                   array[save_index] = array[i] - array[save_index]
                   array[i] -= array[save_index]
                """

    @staticmethod
    def quick_sort(array: list[int]):
        SortUtils.__quick_sort(array, 0, len(array) - 1)

    @staticmethod
    def __quick_sort(array: list[int], start: int, end: int):
        left = start
        right = end
        middle = array[(start + end) // 2]
        while left <= right:
            while array[left] < middle:
                left += 1
            while array[right] > middle:
                right -= 1
            if left <= right:
                if left < right:
                    array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        if left < end:
            SortUtils.__quick_sort(array, left, end)
        if start < right:
            SortUtils.__quick_sort(array, start, right)

    @staticmethod
    def heap_sort(array: list[int]):
        # Построение кучи (перегруппируем массив)
        for i in range(len(array) // 2 - 1, -1, -1):
            SortUtils.__heapify(array, len(array), i)
        # Один за другим извлекаем элементы из кучи
        for i in range(len(array) - 1, -1, -1):
            # Перемещаем текущий корень в конец
            array[0], array[i] = array[i], array[0]
            # Вызываем процедуру heapify на уменьшенной куче
            SortUtils.__heapify(array, i, 0)

    @staticmethod
    def __heapify(array: list[int], heap_size: int, root_index: int):
        largest = root_index  # Инициализируем наибольший элемент как корень
        left_child = 2 * root_index + 1
        right_child = 2 * root_index + 2
        # Если левый дочерний элемент больше, чем самый большой элемент на данный момент
        if left_child < heap_size and array[left_child] > array[largest]:
            largest = left_child
        # Если правый дочерний элемент больше, чем самый большой элемент на данный момент
        if right_child < heap_size and array[right_child] > array[largest]:
            largest = right_child
        # Если самый большой элемент не корень
        if largest != root_index:
            array[root_index], array[largest] = array[largest], array[root_index]
            # Рекурсивно преобразуем в двоичную кучу затронутое поддерево
            SortUtils.__heapify(array, heap_size, largest)
