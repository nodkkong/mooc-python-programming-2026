# Write your solution here
word = input("Word: ")
print("*" * 30)
print("*" + " " * ((28 - len(word)) // 2) + word + " " * (28 - len(word) - (28 - len(word)) // 2) + "*")
print("*" * 30)
