# Simple approach
class Party:
    def __init__(self):
        self.people = []


party_people = Party()

while True:
    name = input()
    if name == 'End':
        break

    party_people.people.append(name)

print(f"Going: {', '.join(party_people.people)}")
print(f'Total: {len(party_people.people)}')


# With a dictionary
class Party:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def get_info(self):
        info = {
            'going': ', '.join(self.people),
            'total': len(self.people)
        }
        result = f"Going: {info['going']}\nTotal: {info['total']}"
        return result


party = Party()
while True:
    command = input()

    if command == 'End':
        break
    party.add_person(command)

print(party.get_info())


# A bit longer but elegant approach
class Party:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def get_going(self):
        return f"Going: {', '.join(party.people)}"

    def get_count_going(self):
        return f'Total: {len(party.people)}'


party = Party()

while True:
    command = input()

    if command == 'End':
        break
    party.add_person(command)

print(party.get_going())
print(party.get_count_going())
