#!/bin/bash

max=0

function isPrime()
{
	primes=$primes
	number=$1
	if [ $number -lt 2 ]
	then
		return 1
	else
		for (( i=2; i<$(( number / 2 )); i++ ))
		do
			if (( $number % $i == 0 ))
			then
				return 1
			fi
		done
		return 0
	fi
}

function main()
{
	for (( a=-1000; a<1000; a++ ))
	do
		for (( b=-1000; b<1001; b++ ))
		do
			number=0
			while ( isPrime $(( (number*number) + (a*number) + b )) )
			do
				number=$(( number + 1 ))
			done
			if (( $number > $max ))
			then
				max=$number
				product=$(( a*b ))
				echo "$a $b Total of $max consecutive primes for a product of $product"
			fi
		done
		echo $a
	done
}

main
