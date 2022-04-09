# how to solve this problem:
# if you follow any sequence of 20 Right move and 20 Down move,
# you will reach the bottom right of the grid
# so you need to calculate every possible permutation of those moves
# which is the same as calculating the binomial coefficent of 20 in 40
# as 20 represents the possible permutations of Right or Down in 
# all the possible moves of right and down (in this case 40)

import _common_functions as cf

print(cf.binomial_coefficient(40, 20))

print(cf.average_running_time(10000, cf.binomial_coefficient, 4,2))
# Average running time of binomial_coefficient for 10000 tests: 2.2353649139404297e-06 seconds