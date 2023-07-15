class SearchUtils:
    @staticmethod
    def binary_search(array: list[int], value: int):
        return SearchUtils.__binary_search(array, value, 0, len(array) - 1)

    @staticmethod
    def __binary_search(array: list[int], value: int, left: int, right: int):
        if right < left:
            return -1

        middle = (right - left) // 2 + left
        if array[middle] == value:
            return middle
        elif array[middle] < value:
            return SearchUtils.__binary_search(array, value, middle + 1, right)
        else:
            return SearchUtils.__binary_search(array, value, left, middle - 1)
