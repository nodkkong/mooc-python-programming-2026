# Write your solution here
from difflib import get_close_matches

wordlist = []
with open("wordlist.txt") as f:
    for line in f:
        wordlist.append(line.strip())

text = input("write text: ")
for word in text.split():
    if word.lower() in wordlist:
        print(word, end=" ")
    else:
        print(f'*{word}*', end=" ")
print()

misspelled = {}
for word in text.split():
    if word.lower() not in misspelled:
        misspelled[word] = get_close_matches(word.lower(), wordlist)

print("suggestions:")
for word, suggestions in misspelled.items():
    print(f"{word}: {', '.join(suggestions)}")