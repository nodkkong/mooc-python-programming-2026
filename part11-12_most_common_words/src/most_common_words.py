# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    words = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                words.append(word.strip(",.?!:;"))
    return {word: words.count(word) for word in words if words.count(word) >= lower_limit}