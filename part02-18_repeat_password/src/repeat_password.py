# Write your solution here
password = input("Password: ")
repeat = input("Repeat password: ")
while password != repeat:
    print("They do not match!")
    repeat = input("Repeat password: ")
print("User account created!")