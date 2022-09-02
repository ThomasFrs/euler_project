#include <stdio.h>
#include <math.h>

int isPrime(long long number, long long big_number)
{
	if (big_number % number == 0)
	{
		for(int i = 2; i<number; i++)
		{
			if (number % i == 0)
				return 0;
		}
		return 1;
	}
	return 0;
}

int main()
{
	long long big_number = 600851475143;
	long long factor = 775147;

	while(!(isPrime(factor, big_number)))
		factor--;
	printf("%lld is the largest prime factor of %lld\n", factor, big_number);
	return 0;	
}
