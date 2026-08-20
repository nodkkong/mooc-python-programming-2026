# Write your solution here
from random import choice
def generate_password(number: int):
    password = []
    while len(password) < number:
        password.append(choice("abcdefghijklmnopqrstuvwxyz"))
    return "".join(password)