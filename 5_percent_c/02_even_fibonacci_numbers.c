#include <stdio.h>

/* spent too much time on this but i understood a thing
or two more about c so not a complete waste of time */

main(){
  int fiba = 1;
  int fibb = 2;
  int sum = 2;

  int list_size = 2;

  while (fiba < 4000000 && fibb < 4000000) {
    if (list_size % 2 == 0){
      fiba += fibb;
      if (fiba % 2 == 0)
        sum += fiba;
    }
    else{
      fibb += fiba;
      if (fibb % 2 == 0)
        sum += fibb;
    }
    list_size += 1;
  }
  printf("sum is %d\n", sum);
}