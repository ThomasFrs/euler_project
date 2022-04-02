def sum_of_multipliers_below(max):
    """
    max: max value that contains all mutipliers of 3 and 5
    return: sum of all mutipliers of 3 and 5 below max
    """
    multipliers = []
    n = 0
    while n < max:
        if n % 3 == 0 or n % 5 == 0:
            multipliers.append(n)
        n += 1
    return sum(multipliers)

assert sum_of_multipliers_below(1000) == 233168, "sum_of_multipliers_below(1000), 233168"