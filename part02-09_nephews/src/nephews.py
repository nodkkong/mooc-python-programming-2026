# Write your solution here
name = input("Please type in youir name: ").capitalize()
dds = ["Huey", "Dewey", "Louie"]
mms = ["Morty", "Ferdie"]
if name in dds:
    print("I think you might be one of Donald Duck's nephews.")
elif name in mms:
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")
