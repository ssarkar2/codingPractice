



#include <stdio.h>
#include <assert.h>


int numdig(int value){
  int cnt = 1;
  while(true){
    value /= 10;
    if (value == 0)
      break;
    cnt += 1;
  }
  return cnt;
}


int myPow(int x, unsigned int p)
{
  if (p == 0) return 1;
  if (p == 1) return x;
  
  int tmp = myPow(x, p/2);
  if (p%2 == 0) return tmp * tmp;
  else return x * tmp * tmp;
}

bool narcissistic( int value ){
  //Code away
  int numdigits = numdig(value);
  int sum = 0;
  int term = 0;
  int pow10;
  //printf("numdigits %d\n", numdigits);
  for (int i = 0; i < numdigits; i++){
    pow10 = myPow(10,i);
    term = myPow(((value / pow10) % 10) , numdigits);
    //printf("term %d %d, %d %d\n", term, (value/ pow10), ((value/ pow10) % 10), pow10);
    sum += term;
  }
  //printf("sum %d\n", sum);
  return sum == value;
}

int main() {
  assert(narcissistic(153)); 
  assert(narcissistic(7));
  assert(!narcissistic(1652));
  return 0;
}
