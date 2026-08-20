# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")
while char in word:
    index = word.find(char)
    if len(word[index:index+3]) == 3:
        print(word[index:index+3])
        word = word[index+1:]
    else:
        break