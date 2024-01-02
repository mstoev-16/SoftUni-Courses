from unittest import TestCase, main

from project.mammal import Mammal


class MammalTests(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('lion', 'cat', 'roar')

    def test_init(self):
        name = 'lion'
        type = 'cat'
        sound = 'roar'
        mammal = Mammal(name, type, sound)
        self.assertEqual('lion', mammal.name)
        self.assertEqual('cat', mammal.type)
        self.assertEqual('roar', mammal.sound)
        self.assertEqual('animals', mammal._Mammal__kingdom)

    def test_make_sound_returns_correct_result(self):
        expected_result = f"{self.mammal.name} makes {self.mammal.sound}"
        actual_result = self.mammal.make_sound()
        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom_returns_correct_result(self):
        expected_result = self.mammal._Mammal__kingdom
        actual_result = self.mammal.get_kingdom()
        self.assertEqual(expected_result, actual_result)

    def test_info_returns_correct_result(self):
        expected_result = f"{self.mammal.name} is of type {self.mammal.type}"
        actual_result = self.mammal.info()
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
