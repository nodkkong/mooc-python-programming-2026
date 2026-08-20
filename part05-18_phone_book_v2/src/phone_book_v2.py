# Write your solution here
my_dict = {}

while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 3: # quit
        print("quitting...")
        break

    name = input("name: ")

    if command == 1: # search
        if name in my_dict:
            for number in my_dict[name]:
                print(number)
        else:
            print("no number")

    elif command == 2: # add
        number = input("number: ")
        if name not in my_dict:
            my_dict[name] = []
        my_dict[name].append(number)
        print("ok!")
