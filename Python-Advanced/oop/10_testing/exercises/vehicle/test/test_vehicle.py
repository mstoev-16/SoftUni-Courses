from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTests(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(125.00, 150.00)

    def test_vehicle_initialization(self):
        fuel = 100.00
        horse_power = 150.00
        vehicle = Vehicle(fuel, horse_power)
        self.assertEqual(fuel, vehicle.fuel)
        self.assertEqual(fuel, vehicle.capacity)
        self.assertEqual(horse_power, vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, vehicle.fuel_consumption)

    def test_vehicle_string_returns_correct_result(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        actual = str(self.vehicle)
        self.assertEqual(expected, actual)

    def test_vehicle_drive_invalid_distance(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(101)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_vehicle_drive_valid_distance(self):
        self.vehicle.drive(100)
        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel_with_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(101)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_increases_fuel_amount_when_given_fuel_is_valid(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(12.5)
        self.assertEqual(125, self.vehicle.fuel)


if __name__ == '__main__':
    main()