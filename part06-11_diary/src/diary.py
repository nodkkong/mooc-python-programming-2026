# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    entries = []
    with open("diary.txt") as f:
        for line in f:
            entries.append(line.strip())
    
    function = int(input("Function: "))
    if function == 1:
        with open("diary.txt", "a") as f:
            f.write(f'{input("Diary entry: ")}\n')
            print("Diary saved\n")
    elif function == 2:
        print("Entries:")
        for entry in entries:
            print(entry)
    else:
        print("Bye now!")
        break