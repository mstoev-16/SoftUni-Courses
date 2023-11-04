from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if any([x.name == pokemon.name for x in self.pokemons]):
            return f"This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        pokemon_details = [f"- {x.name} with health {x.health}" for x in self.pokemons]
        return result + '\n'.join(pokemon_details)


pokemon_1 = Pokemon("Pikachu", 90)
print(pokemon_1.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon_1))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())

# Pikachu with health 90
# Caught Pikachu with health 90
# Caught Charizard with health 110
# This pokemon is already caught
# You have released Pikachu
# Pokemon is not caught
# Pokemon Trainer Ash
# Pokemon count 1
# - Charizard with health 11
