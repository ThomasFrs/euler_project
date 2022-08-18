#!/bin/bash

function cycleLength()
{
	remainder=10
	cycles=0
	while [ $remainder != 10 ] || [ $cycles -lt 1 ]
	do
		remainder=$(( (remainder % $1) * 10 ))
		cycles=$(( cycles + 1 ))
	done
	echo "$1 has a recurring cycle of $cycles"
}

for (( i=2; i<1000; i++ ))
do
	if (( $i % 2 != 0 )) && (( $i % 5 != 0 ))
	then
		cycleLength $i
	fi
done
