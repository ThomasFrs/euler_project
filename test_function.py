from euler_project import *

def test_function(*args):
        euler = Euler()
        display_all = False
        if "-a" in args:
            display_all = True

        if display_all:
            print("display all mode is on")
            # problem 1
            print("\nProblem 1\nFind the sum of all the multiples of 3 or 5 below 1000:")
            print(euler.sum_of_multipliers_below(1000))

            # problem 2
            print("\nProblem 2\nBy considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms:")
            print(euler.even_fibonacci_numbers(4000000))

            # problem 3
            print("\nProblem 3\nWhat is the largest prime factor of the number 600851475143 ?")
            print(euler.largest_prime_factor(15))

            # problem 4
            print("\nProblem 4\nFind the largest palindrome made from the product of two 3-digit numbers:")
            print(euler.largest_palindrome_product(3))

            # problem 5
            print("\nProblem 5\nWhat is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?")
            print(euler.smallest_multiple(20))

            # problem 6
            print("\nProblem 6\nFind the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum:")
            print(euler.sum_square_difference(100))

            # problem 7
            print("\nProblem 7\nWhat is the 10 001st prime number?")
            print(euler.numberth_prime(1001))

            # problem 8
            print("\nProblem 8\nFind the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?")
            print(euler.largest_product_in_serie(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450, 13))

            # problem 9
            print("\nProblem 9\nThere exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc:")
            print(euler.special_pythagorean_triplet(1000))

            # problem 10
            print("\nProblem 10\nFind the sum of all the primes below two million:")
            print(euler.sieve_of_eratosthenes(2000000))

        else:
            print("display all mode is off")

test_function("-a")