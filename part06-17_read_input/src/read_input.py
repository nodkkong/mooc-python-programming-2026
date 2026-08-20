# Write your solution here
def read_input(prompt: int, low: int, high: int):
    while True:
        try:
            user_input = input(prompt)
            number = int(user_input)
            if low <= number <= high:
                return number
            print(f'You must type in an integer between {low} and {high}')
        except ValueError:
            print(f'You must type in an integer between {low} and {high}')