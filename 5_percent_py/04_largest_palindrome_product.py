import _common_functions as cf

def largest_palindrome_product(digits):
  """
  digits: number of digits desired to calculate the largest palindrome product in
  return: max palindromme of product of numbers from digits
  """
  nines = 0
  for i in range(0, digits):
      tens = 10**i
      nines = nines * 10 + 9
  maximum_palindrome = 0
  for i in range(tens, nines):
      for j in range(tens, nines):
          if cf.is_palindrome(i*j) and (i*j) > maximum_palindrome:
              maximum_palindrome = i*j
  return maximum_palindrome

assert largest_palindrome_product(3) == 906609, "largest_palindrome_product(3), 906609"