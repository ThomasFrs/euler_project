import _common_functions as cf

def largest_prime_factor(number):
  """
  number: number on which is tested factors (prime or not)
  return: list of factors of number and the max factor of that list
  """
  factors = [1]
  for i in range(2, number//2+1):
      if number % i == 0:
          if cf.is_prime(i):
              factors.append(i)
  return max(factors), factors

# i solved this one using pure mathematics since
# i couldn't make an efficient enough program to
# find the correct answer without waiting ten years
assert largest_prime_factor(600851475143) == 6857, "largest_prime_factor(600851475143), 6857"