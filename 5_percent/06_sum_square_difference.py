def sum_square_difference(max):
  """
  max: max number of the list ranging from 1 to max
  return: difference between the sum of the square of the range 1 to max, and the square of the sum of the range 1 to max 
  """
  square_sum_list = []
  sum_list = []
  for i in range(1, max+1):
      square_sum_list.append(i**2)
      sum_list.append(i)
  return abs(sum(square_sum_list) - sum(sum_list)**2)

assert sum_square_difference(100) == 25164150, "sum_square_difference(100), 25164150"