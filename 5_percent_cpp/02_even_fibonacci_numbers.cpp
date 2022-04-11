// Pretty messy for now and ressembles a lot the C version but
// I'm just learning and I hope to improve soon

#include <iostream>

using namespace std;

int main(){
  int sum, fiba, fibb, list_size, max;
  sum = 2;

  fiba = 1;
  fibb = 2;
  list_size = 2;

  max = 4000000;

  while (fiba < max && fibb < max){
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
    ++list_size;
  }

  cout << "The sum of even fibonacci numbers under " << max << " is " << sum << endl;
}