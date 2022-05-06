#include <iostream>
#include <cmath>
using namespace std;


int main(){
  int fiba, fibb, index;
  fiba = fibb = 1;
  index = 0;

  long int limit = pow(10, 999); // which corresponds to the smallest number of 1000 digits
  printf("%ld\n", limit);

  while (fiba < limit || fibb < limit){
    if (index % 2 == 0)
      fiba += fibb;
    else
      fibb += fiba;
    index++;
  }

  cout << "The first term of the fibonacci sequence to have over 1000 digits is the " << index << "th term" << endl;

  return 0;
}