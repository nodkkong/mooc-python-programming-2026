# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []
        self.total_heights = 0

    def add(self, person: Person):
        self.persons.append(person)
        self.total_heights += person.height

    def is_empty(self) -> bool:
        return True if not self.persons else False

    def print_contents(self):
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {self.total_heights} cm")
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")
    
    def shortest(self):
        if not self.persons:
            return None
        else:         
            shortest = self.persons[0]
            for person in self.persons:
                if person.height < shortest.height:
                    shortest = person
            return shortest

    def remove_shortest(self):
        if not self.persons:
            return None
        shortest_person = self.shortest()
        self.persons.remove(shortest_person)
        self.total_heights -= shortest_person.height
        return shortest_person