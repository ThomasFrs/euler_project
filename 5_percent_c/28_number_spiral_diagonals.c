#include <stdio.h>

int main()
{
	int spiral_size;
	printf("Enter spiral size : ");
	scanf("%d", &spiral_size);

	long long sum = 1;
	int coefficient = 0;
	int number = 1;

	for( int i = 0; i < (spiral_size-1)/2 ; i++ )
	{
		coefficient += 2;

		for( int j = 0; j < 4 ; j++)
		{
			number += coefficient;
			sum += number;
		}

	}

	printf("%lld\n", sum);

	return 0;
}
