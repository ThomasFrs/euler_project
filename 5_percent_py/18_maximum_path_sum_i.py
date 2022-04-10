# basically how this works is that it calculates the sum of the max from
# the numbers (following the adjacent number rule) of the first row up to
# the top, which gives the maximum path when looking at the top element

import _common_functions as cf


def maximum_path_sum(triangle):
    """
    triangle: string of integers split by spaces and arranged in rows containing + 1 element that the upper one
    return: sum of the maximum path from the top number to the bottom following an adjacent route
    """
    giga_list = [sub_list.split(" ") for sub_list in triangle.split("\n")]
    for i in reversed(
        range(
            len(giga_list) -
            1)):  # starts from the bottom row-1 of the pyramid
        for j in range(len(giga_list[i])):
            # every element is the sum of the max between the two bottom
            # adjacent elements
            giga_list[i][j] = int(giga_list[i][j]) + \
                int(max(giga_list[i + 1][j:j + 2]))
    return giga_list[0]


triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


print(maximum_path_sum(triangle))
print(cf.average_running_time(10000, maximum_path_sum, triangle))
# Average running time of maximum_path_sum for 10000 tests:
# 8.364677429199218e-05 seconds
