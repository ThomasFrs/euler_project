def special_pythagorean_triplet(number):
  """
  number: number on which is tested if a + b + c = number using pythagore theorem
  return: product of a, b, and c
  """
  for i in range(1,number):
      for j in range(1,number):
          if (i + j + (i**2 + j**2)**0.5) == number:
              return int(i * j * (i**2 + j**2)**0.5)

assert special_pythagorean_triplet(1000) == 31875000, "special_pythagorean_triplet(1000), 31875000"