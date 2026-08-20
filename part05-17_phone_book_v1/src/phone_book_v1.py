# Write your solution here
my_dict = {}

while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 3:
        print("quitting...")
        break
    name = input("name: ")
    if command == 1:
        if name in my_dict:
            print(my_dict[name])
        else:
            print("no number")
    elif command == 2:
        number = input("number: ")
        my_dict[name] = number
        print("ok!")    
    
        

