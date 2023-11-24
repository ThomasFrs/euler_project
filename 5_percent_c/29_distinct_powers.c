#include <stdio.h>
#include <math.h>

// flawed solution
// tests if a**b < base_power**maximum but doesn't test
// if a**b < power_below**maximum therefore counting too many numbers
int isPowerOfOtherNumber(int number, int* base)
{
	for( int i = 2; i < number ; i++ )
	{
		int divisor = i;
		while( divisor < number ) divisor *= i;
		if( number == divisor )
		{
			*base = i;
			return 1;
		}
	}
	return 0;
}

int main()
{
	int sum = 0;
	int maximum;
	scanf("%d", &maximum);

	int base;

	for( int a = 2; a <= maximum ; a++ )
	{
		for( int b = 2; b <= maximum ; b++ )
		{
			if ( !(isPowerOfOtherNumber(a, &base) && (pow(a, b) < pow(base, maximum))) ) printf("%d, %d\t%f\n", a, b, pow(a,b)), sum++;
		}
	}

	printf("%d\n", sum);
	//while( scanf("%d", &test) != EOF ) printf("%d\n", isPowerOfOtherNumber(test));
	return 0;
}
