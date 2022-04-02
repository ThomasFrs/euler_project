def smallest_multiple(number):
  """
  number: range to test on the min number divisible by all numbers from that range
  return: min product divisible by all numbers from 1 to number
  """
  mult_list = []
  res = 1
  for i in range(1, number+1):
      current_number = i
      for elt in mult_list:
          if current_number % elt == 0:
              current_number = int(current_number/elt)
      mult_list.append(current_number)
  for mult in mult_list:
      res *= mult
  return res

assert smallest_multiple(20) == 232792560, "smallest_multiple(20), 232792560"