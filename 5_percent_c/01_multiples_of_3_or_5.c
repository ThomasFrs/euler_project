#include <stdio.h>

main(){
  int maximum, sum;

  maximum = 1000;
  sum = 0;

  for (int n = 0; n < maximum; n++){
    if (n % 3 == 0 || n%5 == 0){
      sum += n;
    }
  }
  printf("sum_of_multipliers below 1000 is %d\n", sum);
}