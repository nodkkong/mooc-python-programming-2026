# write your solution here
wordlist = []
with open("wordlist.txt") as f:
    for line in f:
        wordlist.append(line.strip())

text = input("Write text: ")
for word in text.split():
    if word.lower() in wordlist:
        print(word, end=" ")
    else:
        print(f'*{word}*', end=" ")
print()