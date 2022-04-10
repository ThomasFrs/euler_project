import _common_functions as cf

def largest_prime_factor(number):
  """
  number: number on which is tested factors (prime or not)
  return: list of factors of number and the max factor of that list
  """
  factors = []
  for elt in cf.list_factors(number):
    if cf.is_prime(elt):
      factors.append(elt)
  return max(factors)

# 1st attempt: i solved this one using pure mathematics since
# i couldn't make an efficient enough program to
# find the correct answer without waiting ten years
# 2nd attempt: used my list_factors algorithm, the problem is now solved in 0.0812s
assert largest_prime_factor(600851475143) == 6857, "largest_prime_factor(600851475143), 6857"
print(cf.average_running_time(10, largest_prime_factor, 600851475143))