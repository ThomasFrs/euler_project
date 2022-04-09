import _common_functions as cf


def power_digit_sum(power):
    """
    power: natural integer
    return: sum of each number of 2^power
    """
    return sum([int(n) for n in str(2**power)])


print(power_digit_sum(1000))  # i honestly have no idea how to improve this
print(cf.average_running_time(1000, power_digit_sum, 1000))
# Average running time of power_digit_sum_easy for 1000 tests:
# 8.186793327331543e-05 seconds
