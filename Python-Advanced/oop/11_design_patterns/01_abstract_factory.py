from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass


class Chair:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Table:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Sofa:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class VictorianFactory(AbstractFactory):
    TYPE = 'Victorian'

    def create_chair(self):
        return Chair(f'{self.TYPE} chair')

    def create_table(self):
        return Table(f'{self.TYPE} table')

    def create_sofa(self):
        return Sofa(f'{self.TYPE} Sofa')


class ModernFactory(AbstractFactory):
    TYPE = 'Modern'

    def create_chair(self):
        return Chair(f'{self.TYPE} chair')

    def create_table(self):
        return Table(f'{self.TYPE} table')

    def create_sofa(self):
        return Sofa(f'{self.TYPE} Sofa')


class FuturisticFactory(AbstractFactory):
    TYPE = 'Futuristic'

    def create_chair(self):
        return Chair(f'{self.TYPE} chair')

    def create_table(self):
        return Table(f'{self.TYPE} table')

    def create_sofa(self):
        return Sofa(f'{self.TYPE} Sofa')


