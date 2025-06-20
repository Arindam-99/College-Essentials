// 4.	Write programs in C to solve the following problems using recursion:
// c.	Convert a given decimal number to binary
#include <stdio.h>

void decToBinary(int n) {
    if(n == 0) return;
    decToBinary(n / 2);
    printf("%d", n % 2);
}

int main() {
    int n;
    printf("Enter a decimal number: ");
    scanf("%d", &n);
    if(n == 0)
        printf("Binary: 0\n");
    else {
        printf("Binary: ");
        decToBinary(n);
        printf("\n");
    }
    return 0;
}
