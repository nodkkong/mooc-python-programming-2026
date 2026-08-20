# Write your solution here
my_list = []
num = 0
while True:
    print(f'The list is now {my_list}')
    choice = input("a(d)d, (r)emove or e(x)it: ")
    if choice == "d":
        num += 1
        my_list.append(num)
    
    elif choice == "r":
        my_list.pop(-1)
        num -= 1
    
    elif choice == "x":
        print("Bye!")
        break