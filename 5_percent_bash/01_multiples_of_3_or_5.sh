total=0
i=1

while [ $i -lt 1000 ]
do
	if (( $i % 3 == 0 )) || (( $i % 5 == 0 ))
	then
		echo $i
		total=$[ total+i ]
	fi
i=$[ i+1 ]
done

echo "the total of the sum of numbers divisible by 3 or 5 below 1000 is : $total"
