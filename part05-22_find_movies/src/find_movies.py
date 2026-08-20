# Write your solution here
def find_movies(database: list, search_term: str):
    new_list = []
    for item in database:
        if search_term.lower() in item["name"].lower():
            new_list.append(item)

    return new_list