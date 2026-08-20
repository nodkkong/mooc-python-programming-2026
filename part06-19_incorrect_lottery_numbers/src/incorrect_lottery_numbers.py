# Write your solution here
def filter_incorrect():
    lottery_numbers = {}
    with open("lottery_numbers.csv") as f:
        for line in f:
            parts = line.strip().split(";")
            week = parts[0]
            numbers = parts[1]
            lottery_numbers[week] = numbers

    with open("correct_numbers.csv", "w") as out:
        for week, numbers in lottery_numbers.items():
            try:
                int(week.split()[1])
                nums = numbers.split(",")
                int_nums = []
                for num in nums:
                    int_nums.append(int(num))
            except ValueError:
                continue

            if len(nums) != 7:
                continue
            elif min(int_nums) < 1 or max(int_nums) > 39:
                continue
            
            duplicate = False
            for i in range(len(int_nums)):
                if int_nums[i] in int_nums[i+1:]:
                    duplicate = True
                    break
            if duplicate:
                continue
            
            out.write(f'{week};{numbers}\n')