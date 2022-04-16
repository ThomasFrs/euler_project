/* this problem is solved rather easily when using mathematics rather than brute-forcing your
way out (which is still easy), basically, every number below a maximum is made of primes,
if you calculate the maximum power of these primes below a maximum and multiply them altogether,
you obtain the smallest number that can be divided by all numbers below a maximum.
I found this solution on stack overflow since i had a hard time figuring out how to solve this
not using brute-force (which I hate) */

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