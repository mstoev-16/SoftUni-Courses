import unittest


class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


class CatTests(unittest.TestCase):
    def test_cat_is_initialized_correctly(self):
        cat = Cat('Tom')
        self.assertEqual('Tom', cat.name)
        self.assertEqual(False, cat.fed)
        self.assertEqual(False, cat.sleepy)
        self.assertEqual(0, cat.size)

    def test_a_fed_cat_eating(self):
        cat = Cat('Tom')
        cat.eat()

        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_is_fed_after_eating(self):
        cat = Cat('Tom')
        self.assertFalse(cat.fed)
        cat.eat()
        self.assertTrue(cat.fed)

    def test_cat_size_is_increased_after_eating(self):
        cat = Cat('Tom')
        self.assertEqual(0, cat.size)
        cat.eat()
        self.assertEqual(1, cat.size)

    def test_cat_is_sleepy_after_eating(self):
        cat = Cat('Tom')
        cat.eat()
        self.assertTrue(cat.sleepy)

    def test_cat_sleeping_without_eating(self):
        cat = Cat('Tom')
        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):
        cat = Cat('Tom')
        self.assertFalse(cat.sleepy)
        self.assertFalse(cat.fed)
        cat.eat()
        self.assertTrue(cat.sleepy)
        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    unittest.main()


