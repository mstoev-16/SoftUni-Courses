from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([hotel_room.guests for hotel_room in self.rooms])

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for hotel_room in self.rooms:
            if hotel_room.number == room_number:
                return hotel_room.take_room(people)

    def free_room(self, room_number):
        for hotel_room in self.rooms:
            if hotel_room.number == room_number:
                return hotel_room.free_room()

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join([str(hotel_room.number) for hotel_room in self.rooms if not hotel_room.is_taken])}\n" \
               f"Taken rooms: {', '.join([str(hotel_room.number) for hotel_room in self.rooms if hotel_room.is_taken])}"
