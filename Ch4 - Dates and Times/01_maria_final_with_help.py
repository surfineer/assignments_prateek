import calendar
import datetime

def count_day_of_week(year, month, day_of_week):
    # convert day of week name to number
    day_num = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
               "Friday": 4, "Saturday": 5, "Sunday": 6}[day_of_week]

    # get total number of days in the given month
    total_days = calendar.monthrange(year, month)[1]

    # get all dates in the given month
    dates = [datetime.date(year, month, day) for day in range(1, total_days + 1)]

    # count occurrences of the day
    count = sum(1 for date in dates if date.weekday() == day_num)

    return count

# repeat until user decides to exit
while True:
    try:
        year = int(input("Enter year (yyyy): "))
        month = int(input("Enter month (mm): "))
        day_of_week = input("Enter day of the week (e.g. Monday): ")

        result = count_day_of_week(year, month, day_of_week)
        print(f"Number of {day_of_week} in {calendar.month_name[month]} {year}: {result}")
        
    except ValueError:
        print("Invalid input. Please enter numbers for year and month.")
    
    except KeyError:
        print("Invalid day of the week. Please enter one of: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.")

    # ask user if they want to continue
    repeat = input("Do you want to continue? (y/n): ")
    if repeat.lower() != "y":
        break

print("Bye!")
