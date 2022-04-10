import _common_functions as cf


def factorial_digit_sum(number):
    """
    number: positive integer
    return: the sum of all digits of the factorial of number
    """
    # i dont know what could be improved in this very function
    # the only thing i can think of would be the factorial function itself
    return sum([int(digit) for digit in str(cf.factorial(number))])


print(cf.average_running_time(100000, factorial_digit_sum, 100))
# Average running time of factorial_digit_sum(100,) for 100000 tests:
# 3.218750476837158e-05 seconds
