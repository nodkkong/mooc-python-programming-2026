# Write your solution here
weekly_cafeteria = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
weekly_groceries = float(input("How much money do you spend on groceries in a week? "))
weekly_average = (weekly_cafeteria * lunch_price) + weekly_groceries
daily_average = weekly_average / 7
print(f'Average food expenditure:\nDaily: {daily_average} euros\nWeekly: {weekly_average} euros')