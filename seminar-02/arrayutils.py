import random


class ArrayUtils:

    @staticmethod
    def prepare_array(length: int):
        array = [random.randint(-99, 99) for i in range(length)]
        return array

    @staticmethod
    def print_array(array: list, text=''):
        print(f'{text}' + ', '.join(f'{i}' for i in array))
