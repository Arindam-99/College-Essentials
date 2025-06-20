// 19.	Write a program in C to implement the n-queens problem.
#include <stdio.h>
#include <stdlib.h>

#define MAX 20
int board[MAX];

int isSafe(int row, int col) {
    for (int i = 0; i < row; i++)
        if (board[i] == col || abs(board[i] - col) == abs(i - row))
            return 0;
    return 1;
}

void solve(int n, int row) {
    if (row == n) {
        for (int i = 0; i < n; i++)
            printf("(%d, %d) ", i + 1, board[i] + 1);
        printf("\n");
        return;
    }
    for (int col = 0; col < n; col++) {
        if (isSafe(row, col)) {
            board[row] = col;
            solve(n, row + 1);
        }
    }
}

int main() {
    int n;
    printf("Enter number of queens: ");
    scanf("%d", &n);
    if (n < 1 || n > MAX) {
        printf("Invalid input\n");
        return 1;
    }
    solve(n, 0);
    return 0;
}
