from unittest import TestCase, main


class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


class CarTests(TestCase):
    def test_make_is_none(self):
        with self.assertRaises(Exception) as ex:
            Car(None, 'audi', 10, 100)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_is_valid(self):
        car = Car(10, 'audi', 10, 100)
        self.assertEqual(10, car.make)

    def test_model_is_none(self):
        with self.assertRaises(Exception) as ex:
            Car(10, None, 10, 100)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_is_valid(self):
        car = Car(10, 'audi', 10, 100)
        self.assertEqual('audi', car.model)

    def test_fuel_consumption_is_zero(self):
        with self.assertRaises(Exception) as ex:
            Car(10, 'audi', 0, 100)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_is_negative(self):
        with self.assertRaises(Exception) as ex:
            Car(10, 'audi', -1, 100)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_is_valid(self):
        car = Car(10, 'audi', 10, 100)
        self.assertEqual(10, car.fuel_consumption)

    def test_fuel_capacity_is_zero(self):
        with self.assertRaises(Exception) as ex:
            Car(10, 'audi', 10, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_is_negative(self):
        with self.assertRaises(Exception) as ex:
            Car(10, 'audi', 10, -1)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_is_valid(self):
        car = Car(10, 'audi', 10, 100)
        self.assertEqual(100, car.fuel_capacity)

    def test_fuel_amount_is_correctly_initialized(self):
        car = Car(10, 'audi', 10, 100)
        self.assertEqual(0, car.fuel_amount)

    def test_fuel_amount_is_set_with_negative_value(self):
        car = Car(10, 'audi', 10, 100)
        self.assertEqual(0, car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_car_with_zero_fuel(self):
        car = Car(10, 'audi', 10, 100)
        with self.assertRaises(Exception) as ex:
            car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_car_with_negative_fuel(self):
        car = Car(10, 'audi', 10, 100)
        with self.assertRaises(Exception) as ex:
            car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_car_with_positive_fuel(self):
        car = Car(10, 'audi', 10, 20)
        self.assertEqual(0, car.fuel_amount)
        car.refuel(10)
        self.assertEqual(10, car.fuel_amount)
        car.refuel(10)
        self.assertEqual(20, car.fuel_amount)
        car.refuel(10)
        self.assertEqual(20, car.fuel_amount)

    def test_drive_with_insufficient_fuel(self):
        car = Car(10, 'audi', 10, 20)
        self.assertEqual(0, car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_sufficient_fuel(self):
        car = Car(10, 'audi', 10, 20)
        self.assertEqual(0, car.fuel_amount)
        car.refuel(20)
        self.assertEqual(20, car.fuel_amount)
        car.drive(10)
        self.assertEqual(19, car.fuel_amount)


if __name__ == '__main__':
    main()