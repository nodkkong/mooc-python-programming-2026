# Write your solution here
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

if (letter1 < letter2 < letter3) or (letter3 < letter2 < letter1):
    mid = letter2
elif (letter2 < letter1 < letter3) or (letter3 < letter1 < letter2):
    mid = letter1
else:
    mid = letter3
print("The letter in the middle is", mid)