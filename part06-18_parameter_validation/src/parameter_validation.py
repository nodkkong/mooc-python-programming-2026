# Write your solution here
def new_person(name: str, age: int):
    if not name:
        raise ValueError
    elif len(name.split()) < 2 or len(name) > 40:
        raise ValueError
    elif age < 0 or age > 150:
        raise ValueError
    else:
        return name, age

