import _common_functions as cf

def summation_of_primes(max):
        """
        max: number to list all prime numbers below
        return: sum of prime numbers below max
        """
        return sum([i for i in range(max) if cf.is_prime(i)])

# not my way but very cool
assert cf.sieve_of_eratosthenes(2000000) == 142913828922, "cf.sieve_of_eratosthenes(2000000), 142913828922"
print(cf.average_running_time(1, cf.sieve_of_eratosthenes, 2000000))
# my way, which sucks because i didn't use enough maths
assert summation_of_primes(2000000) == 142913828922
print(cf.average_running_time(1, summation_of_primes, 2000000))