import _common_functions as cf


def lexicographic_permutations(element: list) -> list:
    """
    element: list of integers to list the permutations of
    return: the 1000000th lexicographic (ascending) permutation of element
    """
    permutations = sorted([elt for elt in cf.list_permutations(element)])
    return permutations[999999]


print(cf.average_running_time(
    10, lexicographic_permutations, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
