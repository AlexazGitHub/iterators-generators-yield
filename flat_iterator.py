class FlatIterator:
    """Итератор, преобразующий список списков в последовательность элементов (плоское представление).
        Пример:
        list_of_lists = [[1, 2], [3], [4, 5, 6]]
        flat = FlatIterator(list_of_lists)
        list(flat)  # -> [1, 2, 3, 4, 5, 6]
    """

    def __init__(self, list_of_list):
        """Инициализирует итератор.
        Args:
            list_of_list (list of list): Список, содержащий вложенные списки.
            Может включать пустые подсписки и элементы любых типов.
        Attributes:
            list_of_list (list of list): Сохраняемый входной список списков.
            outer_index (int): Индекс текущего подсписка (внешнего уровня).
            inner_index (int): Индекс текущего элемента внутри подсписка.
        """
        self.list_of_list = list_of_list
        self.outer_index = 0
        self.inner_index = 0

    def __iter__(self):
        """Возвращает сам объект итератора.
        Returns:
            FlatIterator: Экземпляр итератора (self).
        """
        return self

    def __next__(self):
        """Возвращает следующий элемент из вложенных списков по порядку.
        Перебирает подсписки последовательно.
        Когда текущий подсписок исчерпан, переходит к следующему.
        Если все элементы обработаны, поднимает StopIteration.
        Returns:
            Any: Следующий элемент из вложенных списков.
        Raises:
            StopIteration: Если все элементы всех подсписков уже возвращены.
        """
        while self.outer_index < len(self.list_of_list):
            current_sublist = self.list_of_list[self.outer_index]
            if self.inner_index >= len(current_sublist):
                # Текущий подсписок исчерпан — переходим к следующему
                self.outer_index += 1
                self.inner_index = 0
                continue

            item = current_sublist[self.inner_index]
            self.inner_index += 1
            return item

        # Все подсписки обработаны
        raise StopIteration


def test_1():
    """Тест базового сценария: проверка соответствия ожидаемой последовательности.
    Использует zip для попарного сравнения элементов итератора с эталонным списком.
    Также проверяет преобразование итератора в список.
    """
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_1),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None
    ]

    print("Тесты пройдены.")


if __name__ == '__main__':
    test_1()