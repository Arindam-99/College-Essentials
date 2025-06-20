// 4.	Write programs in C to solve the following problems using recursion:

// b.	Calculate the sum of digits of a number.

#include <stdio.h>

int sumDigits(int n) {
    if(n == 0) return 0;
    return (n % 10) + sumDigits(n / 10);
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Sum of digits of %d is %d\n", n, sumDigits(n));
    return 0;
}
