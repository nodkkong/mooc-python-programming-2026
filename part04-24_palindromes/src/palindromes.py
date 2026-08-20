# Write your solution here
def palindromes(user_input):
    return user_input == user_input[::-1]

while True:
    user_input = input("Please type in a palindrome: ")
    if palindromes(user_input):
        print(f'{user_input} is a palindrome!')
        break
    else:
        print("that wasn't a palindrome")



# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
