import types


def flat_generator(list_of_lists):
    """Генератор для преобразования списка списков в плоскую последовательность.
    Args:
        list_of_lists (list): Список, содержащий вложенные списки.
    Yields:
        Элементы из вложенных списков по порядку.
    """
    for sublist in list_of_lists:
        for item in sublist:
            yield item


def test_2():
    """Тестовая функция для проверки flat_generator.
    Проверяет:
    - Поэлементное соответствие генератора эталонным значениям.
    - Полное совпадение списка из генератора с ожидаемым результатом.
    - Тип возвращаемого объекта (генератор).
    """
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
        flat_generator(list_of_lists_1),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None
    ]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

    print("Тесты пройдены.")


if __name__ == '__main__':
    test_2()
