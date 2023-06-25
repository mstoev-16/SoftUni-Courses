class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return 2 * Circle.__pi * self.diameter / 2

    def calculate_area(self):
        return Circle.__pi * ((self.diameter / 2) ** 2)

    def calculate_area_of_sector(self, angle):
        return (angle / 360) * self.calculate_area()
