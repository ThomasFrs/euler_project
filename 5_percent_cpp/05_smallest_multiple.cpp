#include <iostream>
#include <cmath>

using namespace std;

bool is_prime(int number){
  if (number < 2){
    return false;
  }
  for (int i = 2; i < number; i++){
    if (number % i == 0)
      return false;
  }
  return true;
}

int main(){
  int maximum = 20;
  long int product = 1;

  for (int i = 1; i < maximum; i++){ // detect every prime number below maximum since every other number are made of primes
    if (is_prime(i)){
      int power = 1;

      while (pow(i, power+1) < maximum){ // maximum power of prime number as long as below maximum
        power++;
      }
      product *= pow(i, power); // multiplies by that power of prime
    }
  }

  cout << "Smallest product divisble by all numbers below " << maximum << " = " << product << endl;
  return 0;
}