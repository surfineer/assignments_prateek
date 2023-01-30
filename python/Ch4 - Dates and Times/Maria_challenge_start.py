# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar

def count_day_of_week(year, month, day_of_week):
    # convert day of week name to number
    day_num = calendar.weekday(year, month, 1)

    # get total number of days in the given month
    total_days = calendar.monthrange(year, month)[1]

    # count occurrences of the day
    count = sum(1 for i in range(1, total_days+1) if calendar.weekday(year, month, i) == day_num)

    return count

# example usage
year = 2022
month = 7
day_of_week = "Monday"
print(f"Number of {day_of_week} in {calendar.month_name[month]} {year}: {count_day_of_week(year, month, day_of_week)}")