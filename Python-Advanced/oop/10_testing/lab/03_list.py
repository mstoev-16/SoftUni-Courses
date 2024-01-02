from unittest import TestCase, main


class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


class IntegerListTests(TestCase):
    def test_list_initialized_correctly_without_data(self):
        int_list = IntegerList()
        self.assertEqual([], int_list._IntegerList__data)

    def test_list_initialized_correctly_with_mixed_data(self):
        int_list = IntegerList(1, 2.0, 5, 4, 2.2, 0, 'a', False, 16)
        self.assertEqual([1, 5, 4, 0, 16], int_list._IntegerList__data)

    def test_list_initialized_with_wrong_data(self):
        int_list = IntegerList(2.0, 4.5, False, [1.2], 'asd')
        self.assertEqual([], int_list._IntegerList__data)

    def test_get_data(self):
        int_list = IntegerList(1, 2.0, 5, 4, 2.2, 0, 'a', False, 16)
        self.assertEqual([1, 5, 4, 0, 16], int_list._IntegerList__data)
        result = int_list.get_data()
        self.assertEqual([1, 5, 4, 0, 16], result)

    def test_add_invalid_element(self):
        int_list = IntegerList(1, 2.0, 5, 4, 2.2, 0, 'a', False, 16)
        with self.assertRaises(ValueError) as ex:
            int_list.add('a')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_add_valid_element(self):
        int_list = IntegerList(1, 2.0, 5, 4, 2.2, 0, 'a', False, 16)
        self.assertEqual([1, 5, 4, 0, 16], int_list._IntegerList__data)
        int_list.add(5)
        self.assertEqual([1, 5, 4, 0, 16, 5], int_list.get_data())

    def test_remove_with_invalid_index(self):
        int_list = IntegerList(1, 2.0, 5, 4, 2.2, 0, 'a', False, 16)
        with self.assertRaises(IndexError) as ex:
            int_list.remove_index(8)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_with_valid_index(self):
        int_list = IntegerList(1, 2.0, 5, 4, 2.2, 0, 'a', False, 16)
        self.assertEqual([1, 5, 4, 0, 16], int_list._IntegerList__data)
        result = int_list.remove_index(1)
        self.assertEqual(5, result)
        self.assertEqual([1, 4, 0, 16], int_list.get_data())

    def test_get_invalid_index(self):
        int_list = IntegerList(1, 2.0, 5, 4, 2.2, 0, 'a', False, 16)
        with self.assertRaises(IndexError) as ex:
            int_list.get(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_valid_index(self):
        int_list = IntegerList(1, 2.0, 5, 4, 2.2, 0, 'a', False, 16)
        result = int_list.get(1)
        self.assertEqual(5, result)

    def test_insert_invalid_index(self):
        int_list = IntegerList(1, 2.0, 5, 4, 2.2, 0, 'a', False, 16)
        with self.assertRaises(IndexError) as ex:
            int_list.insert(5, 24)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_valid_index_invalid_element(self):
        int_list = IntegerList(1, 2.0, 5, 4, 2.2, 0, 'a', False, 16)
        with self.assertRaises(ValueError) as ex:
            int_list.insert(4, 'test')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_insert_valid_index_valid_element(self):
        int_list = IntegerList(1, 2.0, 5, 4, 2.2, 0, 'a', False, 16)
        int_list.insert(4, 4)
        self.assertEqual([1, 5, 4, 0, 4, 16], int_list.get_data())

    def test_get_biggest(self):
        int_list = IntegerList(1, 2.0, 5, 4, 2.2, 0, 'a', False, 16)
        result = int_list.get_biggest()
        self.assertEqual(16, result)

    def test_get_index(self):
        int_list = IntegerList(1, 2.0, 5, 4, 2.2, 0, 'a', False, 16)
        result = int_list.get_index(4)
        self.assertEqual(2, result)


if __name__ == '__main__':
    main()
