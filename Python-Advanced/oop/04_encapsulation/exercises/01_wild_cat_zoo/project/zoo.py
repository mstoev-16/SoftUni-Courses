from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for current_worker in self.workers:
            if current_worker.name == worker_name:
                self.workers.remove(current_worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([current_worker.salary for current_worker in self.workers])
        if self.__budget < total_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        tending_cost = sum([current_animal.money_for_care for current_animal in self.animals])
        if self.__budget < tending_cost:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= tending_cost
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = [f'You have {len(self.animals)} animals']
        lions = []
        tigers = []
        cheetahs = []
        for current_animal in self.animals:
            if current_animal.__class__.__name__ == 'Lion':
                lions.append(current_animal)
            elif current_animal.__class__.__name__ == 'Tiger':
                tigers.append(current_animal)
            elif current_animal.__class__.__name__ == 'Cheetah':
                cheetahs.append(current_animal)

        result.append(f"----- {len(lions)} Lions:")
        for lion in lions:
            result.append(repr(lion))
        result.append(f"----- {len(tigers)} Tigers:")
        for tiger in tigers:
            result.append(repr(tiger))
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        for cheetah in cheetahs:
            result.append(repr(cheetah))
        return '\n'.join(result)

    def workers_status(self):
        result = [f'You have {len(self.workers)} workers']
        keepers = []
        caretakers = []
        vets = []
        for current_worker in self.workers:
            if current_worker.__class__.__name__ == 'Keeper':
                keepers.append(current_worker)
            elif current_worker.__class__.__name__ == 'Caretaker':
                caretakers.append(current_worker)
            elif current_worker.__class__.__name__ == 'Vet':
                vets.append(current_worker)

        result.append(f"----- {len(keepers)} Keepers:")
        for keeper in keepers:
            result.append(repr(keeper))
        result.append(f"----- {len(caretakers)} Caretakers:")
        for caretaker in caretakers:
            result.append(repr(caretaker))
        result.append(f"----- {len(vets)} Vets:")
        for vet in vets:
            result.append(repr(vet))
        return '\n'.join(result)


# zoo = Zoo("Zootopia", 3000, 5, 8)
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1),
# Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1),
# Lion("Nala", "Female", 4)]
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95),
# Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140),
# Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
# # Paying keepers
# print(zoo.pay_workers())
# # Fireing worker
# print(zoo.fire_worker("Adam"))
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())

