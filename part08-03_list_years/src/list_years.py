# Write your solution here
# Remember the import statement
# from datetime import date

from datetime import date
def list_years(dates: list):
    sorted_dates = sorted(dates)
    years = []
    for d in sorted_dates:
        years.append(d.year)
    return years