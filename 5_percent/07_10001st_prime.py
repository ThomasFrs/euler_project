import _common_functions as cf

def numberth_prime(number):
  """
  number: index of all the prime numbers
  return: the numberth prime number and its index, in this case number
  """
  i = 0
  n = 0
  while i < number:
      n += 1
      if cf.is_prime(n):
          i += 1
  return n, i

assert numberth_prime(100001) == 104743