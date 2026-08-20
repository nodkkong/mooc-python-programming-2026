# Write your solution here

def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    new_dict = {"name": name, "director": director, "year": year, "runtime": runtime}
    database.append(new_dict)

    