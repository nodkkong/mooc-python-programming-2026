# Write your solution here
string = input("Please type in a string: ")
sub = input("Please type in a substring: ")
count = 0
position = 0
while sub in string[position:]:
    index = string[position:].find(sub)
    position += index + len(sub)
    count += 1
    if count == 2:
        print(f'The second occurrence of the substring is at index {position - len(sub)}.')
        break
if count < 2:
        print("The substring does not occur twice in the string.")