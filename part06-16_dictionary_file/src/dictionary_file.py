# Write your solution here
words = {}
with open("dictionary.txt") as f:
    for line in f:
        parts = line.strip().split(";")
        words[parts[0]] = parts[1]

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = int(input("Function: "))
    if function == 1:
        with open("dictionary.txt", "a") as f:
            finnish = input("The word in Finnish: ")
            english = input("The word in English: ")
            words[finnish] = english
            f.write(f'{finnish};{english}\n')
            print("Dictionary entry added")
    elif function == 2:
        search_term = input("Search term: ")
        for finnish, english in words.items():
            if search_term in finnish or search_term in english:
                print(f"{finnish} - {english}")
    else:
        print("Bye!")
        break