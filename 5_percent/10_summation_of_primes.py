import _common_functions as cf

def summation_of_primes(max):
        """
        max: number to list all prime numbers below
        return: sum of prime numbers below max
        """
        return sum([i for i in range(max) if cf.is_prime(i)])

assert cf.sieve_of_eratosthenes(2000000) == 142913828922, "cf.sieve_of_eratosthenes(2000000), 142913828922"
#assert summation_of_primes(2000000) == 142913828922