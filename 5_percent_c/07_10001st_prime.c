#include <stdio.h>

int isPrime(int number)
{
	for(int i = 2; i<(number/2)+1; i++)
	{
		if (number % i == 0)
			return 0;
	}
	return 1;
}

int main()
{
	int number = 1;
	int prime_count = 0;
	while(prime_count < 10001)
	{
		number++;
		prime_count += isPrime(number);
	}
	printf("the 10001st prime is %d\n", number);

	return 0;
}
