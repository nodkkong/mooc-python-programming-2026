# Write your solution here
whom = input("Whom should I sign this to:")
where = input("Where shall I save it:")

with open(where, "w") as f:
    f.write(f"Hi {whom}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")