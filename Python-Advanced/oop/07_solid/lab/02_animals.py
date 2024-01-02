from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return 'woof-woof'


class Cat(Animal):
    def make_sound(self):
        return 'meow'


class Turtle(Animal):
    def make_sound(self):
        return '...'


def get_animal_sound(animals: list[Animal]) -> None:
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat(), Turtle()]
get_animal_sound(animals)