# Write your solution here
from random import randint, choice, shuffle
def generate_strong_password(number: int, numbers: bool, special: bool):
    password = []
    if numbers:
        password.append(str(randint(0,9)))
    if special:
        password.append(choice("!?=+-()#"))
    while len(password) < number:
        password.append(choice("abcdefghijklmnopqrstuvwxyz"))
    shuffle(password)
    return "".join(password)