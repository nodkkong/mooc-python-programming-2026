from math import sqrt
# Write your solution here
while True:
    num = int(input("Please type in a number: "))
    if num == 0:
        break
    elif num < 0:
        print("Invalid number")    
        continue
    print(f'{sqrt(num):.1f}')
print("Exiting...")