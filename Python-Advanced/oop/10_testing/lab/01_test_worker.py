import unittest


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(unittest.TestCase):
    def test_worker_is_correctly_initialized(self):
        # Arrange, Act
        worker = Worker('Test', 1000, 50)

        # Assert
        self.assertEqual('Test', worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(50, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_work_with_zero_energy(self):
        # Arrange
        worker = Worker('Test', 1000, 0)

        # Act, Assert
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_work_with_negative_energy(self):
        # Arrange
        worker = Worker('Test', 1000, 0)

        # Act, Assert
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_energy_decreases_after_working(self):
        worker = Worker('Test', 1000, 50)
        self.assertEqual(50, worker.energy)
        worker.work()
        self.assertEqual(49, worker.energy)

    def test_worker_money_is_increased_with_salary(self):
        worker = Worker('Test', 1000, 50)
        worker.work()
        self.assertEqual(1000, worker.money)
        worker.work()
        self.assertEqual(2000, worker.money)

    def test_worker_energy_increases_after_resting(self):
        worker = Worker('Test', 1000, 50)
        worker.rest()
        self.assertEqual(51, worker.energy)

    def test_get_info(self):
        worker = Worker('Test', 1000, 50)
        result = f'{worker.name} has saved {worker.money} money.'
        self.assertEqual(result, worker.get_info())


if __name__ == '__main__':
    unittest.main()
