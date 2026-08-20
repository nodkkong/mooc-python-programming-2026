# Write your solution here
attempts = 0
while (pin := int(input("PIN: "))) != 4321:
    print("Wrong")
    attempts += 1
attempts += 1
if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f'Correct! It took you {attempts} attempts')