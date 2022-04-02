def even_fibonacci_numbers(max):
    """
    max: max value that value list should obtain
    return: sum of even numbers of the fibonacci sequence below max
    """
    value = [1, 2]
    while value[-1] < max:
        value.append(value[-2]+value[-1])
    return sum([elt for elt in value if elt % 2 == 0])

assert even_fibonacci_numbers(4000000) == 4613732, "even_fibonacci_numbers(4000000), 4613732"