import _common_functions as cf

def highly_divisible_triangular_number(nb_factors):
  """
  nb_factors: natural integer
  return: the smallest triangle number with a number of factors exceeding nb_factors
  """
  factors_list = []
  number = 1
  while len(factors_list) <= nb_factors:
    triangular_nb = int((number * (number + 1))/2)
    factors_list = cf.list_factors(triangular_nb) # list factors
    number += 1
  return ("base number : %s, its triangle : %s, number of factors: %s" %(number, triangular_nb, len(factors_list)))

assert highly_divisible_triangular_number(500) == "base number : 12376, its triangle : 76576500, number of factors: 576"
print(cf.average_running_time(10, highly_divisible_triangular_number, 500))
# 1st attempt: 0.17s for 50 factors, 32s for 150 factors (awful lot)
# 2nd attempt: 20s for 500 factors, great success!
# 3rd attempt: 19s for 500 factors.
# 4th attempt: algorithm now uses for loop instead of while, 9s for 500 factors!
# Last attempt: Average running time of highly_divisible_triangular_number for 10 tests: 4.299981045722961 seconds