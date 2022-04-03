import time

def is_prime(x):
  """
  x = number to test if it is a prime number (divisible only by 1 and itself)
  return: True if x is a prime number, False if it isn't
  """
  if x >= 2:
      for i in range(2, int(x**0.5)+1): # the sqrt of x is very important and drastically decreases running time
          if x % i == 0:
              return False
      return True
  return False

def is_palindrome(x):
  """
  x: number to test if it is a palindrome
  return: True if x can be read in both directions, False if it can't
  """
  temp = x
  rev = 0
  while(x > 0):
      dig = x % 10
      rev = rev*10 + dig
      x = x//10
  return temp == rev

def sieve_of_eratosthenes(n):
  """
  n: number to list all prime numbers below
  return: sum of prime numbers below n
  """
  prime = [True for i in range(n + 1)]
  p = 2
  while (p * p <= n):
      if (prime[p] == True):
          for i in range(p ** 2, n + 1, p):
              prime[i] = False
      p += 1
  prime[0]= False
  prime[1]= False
  return sum([p for p in range(n + 1) if prime[p]])

def list_factors(number):
  """
  number: natural integer
  return: list of all positive factors of number
  """
  factors_list = []
  for i in range(1, int(number**0.5)): # factors can't be higher than the sqrt of a number
    if (number % i == 0): 
      if i == int(number**0.5): # don't duplicate factor if the factor is the sqrt of a number
        factors_list.append(i)
      else:
        if i not in factors_list:
          factors_list.extend([i, int(number/i)]) # list factor and number/factor which significantly decreases the processing time
  return factors_list

def average_running_time(nb_tests, function, *args):
  """
  nb_test: natural integer representing number of time to test function
  function: function to test the average running time of
  args: arguments of function
  return: average running time of function calculated from nb_tests tests
  """
  runnning_time = []
  for i in range(nb_tests):
    start_time = time.time()
    function(*args)
    end_time = time.time()
    runnning_time.append(end_time-start_time)  
  return "Average running time of %s for %s tests: %s seconds" %(function.__name__, nb_tests, (sum(runnning_time))/len(runnning_time))