class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            return f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == 'fish':
            return f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == 'bird':
            return f"Birds in {self.zoo_name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"


the_zoo = Zoo(input())
n = int(input())

for i in range(n):
    command = input().split()
    type = command[0]
    name = command[1]
    the_zoo.add_animals(type, name)

print(the_zoo.get_info(input()))
