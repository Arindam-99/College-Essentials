// 14.	Write a program in C to construct the minimum spanning tree from any directed or undirected graph using Prim’s algorithm.
#include <stdio.h>
#include <limits.h>

#define MAX 100

int n; // number of vertices
int cost[MAX][MAX]; // adjacency matrix

int primMST() {
    int visited[MAX] = {0};
    int minCost = 0;

    visited[0] = 1; // start from vertex 0

    int edges = 0;
    while (edges < n - 1) {
        int u = -1, v = -1, min = INT_MAX;

        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                for (int j = 0; j < n; j++) {
                    if (!visited[j] && cost[i][j] && cost[i][j] < min) {
                        min = cost[i][j];
                        u = i;
                        v = j;
                    }
                }
            }
        }

        if (u != -1 && v != -1) {
            printf("Edge %d: (%d - %d) cost = %d\n", edges + 1, u, v, cost[u][v]);
            minCost += cost[u][v];
            visited[v] = 1;
            edges++;
        }
    }

    return minCost;
}

int main() {
    int i, j;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter the cost adjacency matrix (use 0 for no edge):\n");
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            scanf("%d", &cost[i][j]);

    int totalCost = primMST();
    printf("Total cost of Minimum Spanning Tree: %d\n", totalCost);

    return 0;
}
