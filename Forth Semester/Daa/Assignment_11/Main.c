//11.	Given a sequence of matrix dimensions as input, write a program in C to calculate the minimum number of scalar multiplications required to multiply those matrices.
#include <stdio.h>
#include <limits.h>

int matrixChainOrder(int p[], int n) {
    int m[n][n]; // m[i][j] stores minimum scalar multiplications
    for (int i = 1; i < n; i++) m[i][i] = 0; // cost is zero for single matrix

    for (int len = 2; len < n; len++) { // chain length
        for (int i = 1; i < n - len + 1; i++) {
            int j = i + len - 1;
            m[i][j] = INT_MAX;
            for (int k = i; k < j; k++) {
                int cost = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j];
                if (cost < m[i][j]) m[i][j] = cost;
            }
        }
    }
    return m[1][n-1]; // minimum cost to multiply matrices A1..An
}

int main() {
    int n;
    printf("Enter number of matrices: ");
    scanf("%d", &n);

    int p[n+1];
    printf("Enter %d dimensions (p0 p1 ... pn): ", n+1);
    for (int i = 0; i <= n; i++) scanf("%d", &p[i]);

    int minCost = matrixChainOrder(p, n+1);
    printf("Minimum number of scalar multiplications: %d\n", minCost);

    return 0;
}
