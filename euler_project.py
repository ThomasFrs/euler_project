from math import *

"""
This is a javadoc style.

@param param1: this is a first param
@param param2: this is a second param
@return: this is a description of what is returned
@raise keyError: raises an exception
"""

class Euler():
    def __init__(self):
        print("\nwelcome to the euler project program")
        self.prime_number_list = []

    # problem 1
    def sum_of_multipliers_below(self, max):
        """
        max: max value that contains all mutipliers of 3 and 5
        return: sum of all mutipliers of 3 and 5 below max
        """
        multipliers = []
        n = 0
        while n < max:
            if n % 3 == 0 or n % 5 == 0:
                multipliers.append(n)
            n += 1
        return sum(multipliers)

    # problem 2
    def even_fibonacci_numbers(self, max):
        """
        max: max value that value list should obtain
        return: sum of even numbers of the fibonacci sequence below max
        """
        value = [1, 2]
        while value[-1] < max:
            value.append(value[-2]+value[-1])
        return sum([elt for elt in value if elt % 2 == 0])

    # problem 3
    def is_prime(self, x):
        """
        x = number to test if it is a prime number (divisible only by 1 and itself)
        return: True if x is a prime number, False if it isn't
        """
        if x <= 1 or any([elt for elt in self.prime_number_list if x % elt == 0]):
            return False
        else:
            self.prime_number_list.append(x)
            return True
                

    def largest_prime_factor(self, number):
        """
        number: number on which is tested factors (prime or not)
        return: list of factors of number and the max factor of that list
        """
        factors = [1]
        for i in range(2, number//2+1):
            if number % i == 0:
                if self.is_prime(i):
                    factors.append(i)
        return max(factors), factors

    # problem 4
    def is_palindrome(self, x):
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

    def largest_palindrome_product(self, digits):
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
                if self.is_palindrome(i*j) and (i*j) > maximum_palindrome:
                    maximum_palindrome = i*j
        return maximum_palindrome

    # problem 5
    def smallest_multiple(self, number):
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

    # problem 6
    def sum_square_difference(self, max):
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

    # problem 7
    def numberth_prime(self, number):
        """
        number: index of all the prime numbers
        return: the numberth prime number and its index, in this case number
        """
        i = 0
        n = 0
        while i < number:
            n += 1
            if self.is_prime(n):
                i += 1
        return n, i

    # problem 8
    def largest_product_in_serie(self, serie, length):
        """
        serie: list of numbers on which to calculate the maximum product in the range of nb_digits
        nb_digits: range of integers taken in serie to calculate its max product
        return: max product in range of nb_digits within serie
        """
        digit_number = [int(i) for i in str(serie)]
        max = 0
        for i in range(len(digit_number)-length+1):
            product = 1
            for j in range(length):
                product *= digit_number[i+j]
            if product > max:
                max = product
        return max

    # problem 9
    def special_pythagorean_triplet(self, number):
        """
        number: number on which is tested if a + b + c = number using pythagore theorem
        return: product of a, b, and c
        """
        for i in range(1,number):
            for j in range(1,number):
                if (i + j + sqrt(i**2 + j**2)) == number:
                    return int(i * j * sqrt(i**2 + j**2))

    # probem 10
    def sieve_of_eratosthenes(self, n):
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
    
    def summation_of_primes(self, max):
        """
        max: number to list all prime numbers below
        return: sum of prime numbers below max
        """
        return sum([i for i in range(max) if self.is_prime(i)])

    # problem 11
    def largest_product_in_grid(self, grid, direction, length):
        number_list = [int(i) for i in grid.split()]
        max = 0
        if direction == "horizontal":
            for i in range(len(number_list) - length + 1):
                product = 1
                for j in range(length):
                    product *= number_list[i+j]
                    if product > max:
                        max = product
        elif direction == "vertical" and length <= sqrt(len(number_list)):
            for i in range(len(number_list) - int(sqrt(len(number_list))*(length-1))):
                product = 1
                for j in range(length):
                    product *= number_list[i + j*length]
                    if product > max:
                        max = product
        elif direction == "diagonaldown" and length <= sqrt(len(number_list)):
            for i in range((int(sqrt(len(number_list)))+ 1 - length)**2):
                product = 1
                for j in range(length):
                    if i > sqrt(len(number_list) - length):
                        i += length
                    product *= number_list[i + (j*length+1)]
                    if product > max:
                        max = product
        return max

    def test_function(self):
        print("\nwelcome to the test function")
        print(self.largest_product_in_grid("08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48", "vertical", 4))
        print(self.largest_product_in_grid("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16", "vertical", 4))
        print(self.largest_product_in_grid("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16", "diagonaldown", 4))

euler = Euler()
euler.test_function()