/* Pretty proud of that one, I've learned the basics of function calling
on my own, which means it must be terrible from an outside perspective
but I'm still glad I managed to do it */

#include <iostream>
#include <cmath>

using namespace std;

bool is_prime(long int number){

  if (number > 2){
    for (int i = 2; i < (pow(number, 0.5) + 1); i++){
      if (number % i == 0)
        return false;
    }
  }
  return true;
}

int largest_prime_factor(long int number){

  int largest_prime_factor = 0;

  for (int i = 1; i < (pow(number, 0.5) + 1); i++){
    if (number % i == 0){

      if (i == (pow(number, 0.5) + 1) and is_prime(i))
        largest_prime_factor = i;

      else if (is_prime(i) and i > largest_prime_factor)
        largest_prime_factor = i;

      else if (is_prime(number/i) and (number/i) > largest_prime_factor)
        largest_prime_factor = i;
    }
  }

  return largest_prime_factor;
}

int main(){
  long int number = 600851475143;
  int prime = largest_prime_factor(number);

  cout << "The largest prime factor of " << number << " is " << prime << endl;
  
  return 0;
}