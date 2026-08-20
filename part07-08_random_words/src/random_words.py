# Write your solution here
from random import sample

def words(n: int, beginning: str):
    matching = []
    with open("words.txt") as f:
        for line in f:
            word = line.strip()
            if word.startswith(beginning):
                matching.append(word)
    if len(matching) < n:
        raise ValueError
    return sample(matching, n)