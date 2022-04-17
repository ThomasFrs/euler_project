#include <iostream>
#include <cmath>

using namespace std;

int sum_factors_below(int max){
  int sum_factors = 0;

  for (int i = 1; i < (pow(max, 0.5) + 1); i++){
    if (max % i == 0){
      if (i == pow(max, 0.5))
        sum_factors += i;
      else
        sum_factors += i + max/i;
    }
  }
  sum_factors -= max;
  return sum_factors;
}

bool is_amicable(int a){
  int b = sum_factors_below(a);
  return (a == sum_factors_below(b) && a != b);
}

int main(){
  int max = 10000;
  int sum = 0;

  for (int i = 220; i < max; i++){
    if (is_amicable(i)){
      sum += i;
      printf("%d\n", i);
    }
  }

  cout << "Sum of amicable numbers below " << max << " = " << sum << endl;
  return 0;
}