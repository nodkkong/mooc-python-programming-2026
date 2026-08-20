# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()

    infos = json.loads(data)
    for info in infos:
        print(f'{info["name"]} {info["age"]} years ({", ".join(info["hobbies"])})')