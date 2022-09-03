#include <stdio.h>

int getIntLength(int number)
{
	int length = 0;
	while( number >= 1 ) length++, number /= 10;
	return length;
}

int isPalindrome(int number)
{
	int length = getIntLength(number);
	int numberArray[length];
	int temp = number;

	// create an array with every digit of the number
	for( int i = 0; i < length; i++ ) numberArray[i] = temp % 10, temp /= 10;
	// loop through the digits in opposite direction and compare with array element
	for( int i = length-1; i >= 0; i-- )
	{
		if( numberArray[i] == number % 10 ) number /= 10; else return 0;
	}
	return 1;
}

int main()
{
	int max = 0;
	// largest 3 digit number is 999
	for( int i = 999; i > 0; i-- )
	{
		for( int j = 999; j > 0; j-- )
		{
			if( isPalindrome(i*j) && i*j > max ) max = i*j;
		}
	}
	printf("%d\n", max);
	return 0;
}
