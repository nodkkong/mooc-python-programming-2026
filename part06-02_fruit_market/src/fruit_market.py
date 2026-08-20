# write your solution here
def read_fruits():
    with open("fruits.csv") as f:
        fruits = {}
        for line in f:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruits[parts[0]] = float(parts[1])
        return fruits