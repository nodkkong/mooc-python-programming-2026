# Write your solution here
def invert(dictionary: dict):
    new_dict = {}
    for k, v in dictionary.items():
        new_dict[v] = k
    dictionary.clear()
    
    for k, v in new_dict.items():
        dictionary[k] = v