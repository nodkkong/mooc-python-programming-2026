# Write your solution here
def filter_solutions():
    datas = []
    with open("solutions.csv") as f:
        for line in f:
            datas.append(line.strip().split(";"))
    
    with open("correct.csv", "w") as correct, open("incorrect.csv", "w") as incorrect:
        for data in datas:
            problem = data[1]
            result = int(data[2])
            line = ";".join(data) + "\n"

            if "+" in problem:
                numbers = problem.split("+")
                if int(numbers[0]) + int(numbers[1]) == result:
                    correct.write(line)
                else:
                    incorrect.write(line)

            elif "-" in problem:
                numbers = problem.split("-")
                if int(numbers[0]) - int(numbers[1]) == result:
                    correct.write(line)
                else:
                    incorrect.write(line)