def isPrime(number: int):
    if (number < 2):
        return False
    else:
        for i in range(2, int(number**0.5) + 1):
            if (number % i == 0):
                return False
        return True

def main():
    max=0
    for a in range(-1000, 1000):
        for b in range(-1000, 1001):
            if (isPrime(b)):
                n=0
                while (isPrime(n**2 + n*a + b)):
                    n+=1
                if (n > max):
                    max=n
                    print(a, b, a*b, max)

main()
