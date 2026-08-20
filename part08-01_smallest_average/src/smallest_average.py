# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    people = [person1, person2, person3]
    avg1 = (person1["result1"] + person1["result2"] + person1["result3"])
    avg2 = (person2["result1"] + person2["result2"] + person2["result3"])
    avg3 = (person3["result1"] + person3["result2"] + person3["result3"])
    avgs = [avg1, avg2, avg3]

    return people[avgs.index(min(avgs))]