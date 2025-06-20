// 13.	Write a program in C to implement BFS and DFS algorithms for traversing through a graph. 
#include <stdio.h>
#include <stdlib.h>

#define MAX 100

int adj[MAX][MAX], visited[MAX], n;

// DFS Function
void DFS(int v) {
    visited[v] = 1;
    printf("%d ", v);
    for (int i = 0; i < n; i++) {
        if (adj[v][i] && !visited[i])
            DFS(i);
    }
}

// BFS Function
void BFS(int start) {
    int queue[MAX], front = 0, rear = 0;
    visited[start] = 1;
    queue[rear++] = start;

    while (front < rear) {
        int v = queue[front++];
        printf("%d ", v);
        for (int i = 0; i < n; i++) {
            if (adj[v][i] && !visited[i]) {
                visited[i] = 1;
                queue[rear++] = i;
            }
        }
    }
}

int main() {
    int e, src, dest, i, start;

    printf("Enter number of vertices: ");
    scanf("%d", &n);
    printf("Enter number of edges: ");
    scanf("%d", &e);

    // Initialize adjacency matrix
    for (i = 0; i < e; i++) {
        printf("Enter edge (source destination): ");
        scanf("%d %d", &src, &dest);
        adj[src][dest] = 1;
        adj[dest][src] = 1; // For undirected graph
    }

    printf("Enter starting vertex for DFS: ");
    scanf("%d", &start);
    for (i = 0; i < n; i++) visited[i] = 0;
    printf("DFS Traversal: ");
    DFS(start);

    printf("\nEnter starting vertex for BFS: ");
    scanf("%d", &start);
    for (i = 0; i < n; i++) visited[i] = 0;
    printf("BFS Traversal: ");
    BFS(start);

    return 0;
}
