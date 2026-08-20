# Write your solution here
def find_words(search_term: str):
    words = []
    with open("words.txt") as f:
        for line in f:
            words.append(line.strip())
    
    found = []
    for word in words:
        if search_term.startswith("*"):
            if word.endswith(search_term[1:]):
                found.append(word)
        elif search_term.endswith("*"):
            if word.startswith(search_term[:-1]):
                found.append(word)
        elif "." in search_term:
            if len(word) == len(search_term):
                match = True
                for i in range(len(search_term)):
                    if search_term[i] != "." and search_term[i] != word[i]:
                        match = False
                        break
                if match:
                    found.append(word)
        else:
            if word == search_term:
                found.append(word)
    
    return found
