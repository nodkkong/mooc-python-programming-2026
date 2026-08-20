# Write your solution here
def read_recipes(filename: str):
    recipes = []
    with open(filename) as f:
        lines = []
        for line in f:
            lines.append(line.strip())
    current = {}
    for line in lines:
        if line == "":
            recipes.append(current)
            current = {}
        elif "name" not in current:
            current["name"] = line
        elif "time" not in current:
            current["time"] = int(line)
        else:
            if "ingredients" not in current:
                current["ingredients"] = []
            current["ingredients"].append(line)
    if current:
        recipes.append(current)
    return recipes


def search_by_name(filename: str, word: str):
    recipes = read_recipes(filename)
    found = []
    for recipe in recipes:
        if word.lower() in recipe["name"].lower():
            found.append(recipe["name"])
    return found


def search_by_time(filename: str, prep_time: int):
    recipes = read_recipes(filename)
    found = []
    for recipe in recipes:
        if prep_time >= recipe["time"]:
            found.append(f'{recipe["name"]}, preparation time {recipe["time"]} min')
    return found


def search_by_ingredient(filename: str, ingredient: str):
    recipes = read_recipes(filename)
    found = []
    for recipe in recipes:
        for ing in recipe["ingredients"]:
            if ingredient.lower() in ing.lower():
                found.append(f'{recipe["name"]}, preparation time {recipe["time"]} min')
                break
    return found
