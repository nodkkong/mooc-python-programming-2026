# Write your solution here
def run(program):
    variables = {}
    for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        variables[c] = 0

    def get_value(x):
        if x in variables:
            return variables[x]
        return int(x)

    output = []
    index = 0
    locations = {}

    for i, line in enumerate(program):
        if line.endswith(":"):
            locations[line[:-1]] = i

    while index < len(program):
        line = program[index].split()
        command = line[0]
        if command == "END":
            break
        elif command == "PRINT":
            output.append(get_value(line[1]))
        elif command == "MOV":
            variables[line[1]] = get_value(line[2])
        elif command == "ADD":
            variables[line[1]] += get_value(line[2])
        elif command == "SUB":
            variables[line[1]] -= get_value(line[2])
        elif command == "MUL":
            variables[line[1]] *= get_value(line[2])
        elif command == "JUMP":
            index = locations[line[1]]
            continue
        elif command == "IF":
            left = get_value(line[1])
            op = line[2]
            right = get_value(line[3])
            condition = False
            if op == "==" and left == right:
                condition = True
            elif op == "!=" and left != right:
                condition = True
            elif op == "<" and left < right:
                condition = True
            elif op == "<=" and left <= right:
                condition = True
            elif op == ">" and left > right:
                condition = True
            elif op == ">=" and left >= right:
                condition = True
            if condition:
                index = locations[line[5]]
                continue
        
        index += 1

    return output
        