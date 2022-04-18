// this one took an awfully long time to complete because it runs very slowly
// and i'm all ears for new ways to improve my code
// not to mention the fact that my usual way of calculating factors didn't work at all

#include <iostream>
#include <cmath>
#include <set>

using namespace std;

int is_abundant(int max){
  int sum_factors = 0;

  for (int i = 1; i < (max/2 + 1); i++){
    if (max % i == 0){
      sum_factors += i;
    }
  }
  return (sum_factors > max);
}


bool is_sum_of_two_abundant(int number, set<int> abundants){

  for (auto i:abundants){
    if (i >= number)
      return false;

    for (auto j : abundants)
    {
      if (i + j > number)
        break;
      if (i + j == number)
        return true;
    }
  }
  return false;
}

int main(){
  int sum = 0;
  set<int> abundant_numbers;

  for (int i = 12; i < 28124; i++){
    if (is_abundant(i)){
      abundant_numbers.insert(i);
    }
  }

  for (int i = 1; i < 28124; i++)
  {
    if (!is_sum_of_two_abundant(i, abundant_numbers))
      sum += i;
  }

  cout << "Sum of non-abundant numbers = " << sum << endl;
  return 0;
}