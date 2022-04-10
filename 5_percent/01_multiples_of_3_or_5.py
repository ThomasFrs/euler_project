import _common_functions as cf


def sum_of_multipliers_below(max):
    """
    max: max value that contains all mutipliers of 3 and 5
    return: sum of all mutipliers of 3 and 5 below max
    """
    return sum([n for n in range(1, max) if n % 3 == 0 or n % 5 == 0])


print(cf.average_running_time(1000, sum_of_multipliers_below, 1000))
# Average running time of sum_of_multipliers_below for 1000 tests:
# 0.00011975049972534179 seconds
