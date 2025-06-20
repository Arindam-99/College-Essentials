// 10.	Write programs in C to calculate the Nth fibonacci number recursively using naive approach and the dynamic programming approach. Demonstrate the performance improvement of the DP approach.
#include <stdio.h>
#include <time.h>

int fibNaive(int n) {
    if(n <= 1) return n;
    return fibNaive(n - 1) + fibNaive(n - 2);
}

int fibDP(int n) {
    int fib[n+2];
    fib[0] = 0;
    fib[1] = 1;
    for(int i = 2; i <= n; i++)
        fib[i] = fib[i-1] + fib[i-2];
    return fib[n];
}

int main() {
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);

    clock_t start, end;

    // Naive Recursive
    start = clock();
    int resultNaive = fibNaive(n);
    end = clock();
    double timeNaive = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Naive Recursive Fibonacci(%d) = %d\n", n, resultNaive);
    printf("Time taken (Naive): %.6f sec\n", timeNaive);

    // Dynamic Programming
    start = clock();
    int resultDP = fibDP(n);
    end = clock();
    double timeDP = (double)(end - start) / CLOCKS_PER_SEC;
    printf("DP Fibonacci(%d) = %d\n", n, resultDP);
    printf("Time taken (DP): %.6f sec\n", timeDP);

    return 0;
}
