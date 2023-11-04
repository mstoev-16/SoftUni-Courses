class Player:
    DEFAULT_GUILD = "Unaffiliated"

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = Player.DEFAULT_GUILD

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        result = f"Name: {self.name}\n" \
                 f"Guild: {self.guild}\n" \
                 f"HP: {self.hp}\n" \
                 f"MP: {self.mp}\n"
        for current_skill, current_cost in self.skills.items():
            result += f"==={current_skill} - {current_cost}\n"
        return result
