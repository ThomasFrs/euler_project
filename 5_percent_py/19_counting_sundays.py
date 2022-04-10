from datetime import date
import _common_functions as cf

# computer-based approach, not too fond of that one
# since i had to basically steal the datetime method (i didnt know about it)
# and it also relies heavily on that module instead of using my head


def counting_sundays(start_year, end_year):
    sundays = 0
    for year in range(start_year + 1, end_year + 1):
        for month in range(1, 13):
            if date(year, month, 1).weekday() == 6:
                sundays += 1
    return sundays


# this is a more mathematical approach that i prefer
# though it doesn't seem as efficient and intuitive as the first one
def counting_sundays_math(start_year, end_year, starting_day):
    """
    start_year, end_year: relative integers
    starting_day: positive integer of the first day (monday = 1) of the given starting_year
    return: number of sundays being the first day of the month between start_year and end_year
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31,
                  30, 31, 30, 31]  # days for every month
    day_of_the_week = starting_day  # on which day of the week we're starting
    sundays = 0
    for year in range(start_year + 1, end_year + 1):
        for month in range(12):
            if (year %
                4 == 0 and year %
                100 != 0) or (year %
                              400 == 0):  # if it is a leap year
                month_days[1] == 29
            else:
                month_days[1] == 28
            # first day of the month
            day_of_the_week = (day_of_the_week + month_days[month]) % 7
            if day_of_the_week == 6:  # is the first day of the month a sunday
                sundays += 1
    return sundays


print(cf.average_running_time(10000, counting_sundays, 1900, 2000))
# Average running time of counting_sundays for 10000 tests:
# 0.00034490416049957277 seconds

print(cf.average_running_time(10000, counting_sundays_math, 1900, 2000, 1))
# Average running time of counting_sundays_math for 10000 tests:
# 0.0002927396535873413 seconds
# both method are as efficient as the other with a slight advantage on the
# mathematical approach
