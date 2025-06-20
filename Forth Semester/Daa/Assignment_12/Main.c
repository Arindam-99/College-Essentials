// 12.	Write a program in C to solve the 0/1 knapsack problem using the dynamic programming approach.
#include <stdio.h>

// Max function
int max(int a, int b) {
    return (a > b) ? a : b;
}

// 0/1 Knapsack DP function
int knapsack(int W, int wt[], int val[], int n) {
    int dp[n+1][W+1];

    // Build DP table
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (i == 0 || w == 0)
                dp[i][w] = 0;
            else if (wt[i-1] <= w)
                dp[i][w] = max(val[i-1] + dp[i-1][w - wt[i-1]], dp[i-1][w]);
            else
                dp[i][w] = dp[i-1][w];
        }
    }

    return dp[n][W]; // maximum value in knapsack
}

int main() {
    int n, W;
    printf("Enter number of items: ");
    scanf("%d", &n);

    int wt[n], val[n];

    printf("Enter weights of %d items: ", n);
    for (int i = 0; i < n; i++)
        scanf("%d", &wt[i]);

    printf("Enter values of %d items: ", n);
    for (int i = 0; i < n; i++)
        scanf("%d", &val[i]);

    printf("Enter maximum capacity of knapsack: ");
    scanf("%d", &W);

    int maxValue = knapsack(W, wt, val, n);
    printf("Maximum value in knapsack = %d\n", maxValue);

    return 0;
}
