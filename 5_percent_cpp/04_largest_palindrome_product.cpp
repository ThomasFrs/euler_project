/* I'm proud of that one because I didn't expect to solve it in C++ anytime soon
but it eventually worked though I probably have issues with number types (int/float) */

#include <iostream>
#include <cmath>

using namespace std;

bool is_palindrome(int number){
  int temp_nb = 0;
  int size = trunc(log10(number)) + 1;
  int nb_of_loop = floor(size / 2.0);

  // number is now half its length, temp_nb is the other half
  for (int i = 0; i < nb_of_loop; i++){
    temp_nb += (number % 10) * pow(10, (nb_of_loop - i - 1));
    number /= 10;
  }

  // if number is an even palindrome
  if (size % 2 == 0){
    if (number == temp_nb)
      return true;
  }
  // if number is an odd palindrome and compares by removing its last value
  // which makes it an even palindrome
  else{
    if (floor(number / 10) == temp_nb)
      return true;
  }
  return false;
}

int main(){
  int maximum = 0;

  for (int i = 0; i <= 1000; i++){
    for (int j = 0; j <= 1000; j++){
      if (i*j > maximum and is_palindrome(i*j))
        maximum = i * j;
    }
  }
  cout << "Largest palindrome product is " << maximum << endl;
  return 0;
}