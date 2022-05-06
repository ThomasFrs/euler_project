import _common_functions as cf


def nth_digits_fibonacci_number(digits: int) -> int:
    """
    digits: integer of number of minimum digits of a fibonacci term
    return: the nth term of the fibonacci sequence with more than digits digit
    """
    fibonacci = [1, 1]
    while fibonacci[-1] <= 10**(digits-1):
        fibonacci.append(fibonacci[-1]+fibonacci[-2])
    return len(fibonacci)


print(cf.average_running_time(100, nth_digits_fibonacci_number, 1000))
# Average running time of nth_digits_fibonacci_number(1000,) for 100 tests:
# 0.02183619499206543 seconds
