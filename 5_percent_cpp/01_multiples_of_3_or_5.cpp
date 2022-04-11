#include <iostream>

using namespace std;

int main(){
  int sum;
  sum = 0;

  for (int n = 0; n < 1000; n++){
    if (n % 3 == 0 || n % 5 == 0)
      sum += n;
  }

  cout << "The sum of all numbers divisible by 3 or 5 and below 1000 is " << sum << endl;
}