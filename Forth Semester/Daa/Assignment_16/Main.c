//16.	Write a program in C to find the shortest path between two given nodes in a graph using Dijkstra’s algorithm.
#include <stdio.h>
#include <limits.h>

#define MAX 100
#define INF INT_MAX

int n;                  // Number of vertices
int graph[MAX][MAX];    // Adjacency matrix

int minDistance(int dist[], int visited[]) {
    int min = INF, min_index = -1;
    for (int i = 0; i < n; i++)
        if (!visited[i] && dist[i] <= min) {
            min = dist[i];
            min_index = i;
        }
    return min_index;
}

void dijkstra(int src, int target) {
    int dist[n], visited[n], parent[n];

    for (int i = 0; i < n; i++) {
        dist[i] = INF;
        visited[i] = 0;
        parent[i] = -1;
    }
    dist[src] = 0;

    for (int count = 0; count < n - 1; count++) {
        int u = minDistance(dist, visited);
        if (u == -1) break;

        visited[u] = 1;

        for (int v = 0; v < n; v++) {
            if (!visited[v] && graph[u][v] && dist[u] != INF &&
                dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
                parent[v] = u;
            }
        }
    }

    // Print result
    if (dist[target] == INF) {
        printf("No path from %d to %d\n", src, target);
    } else {
        printf("Shortest distance from %d to %d = %d\n", src, target, dist[target]);

        // Print path
        int path[MAX], k = 0;
        for (int v = target; v != -1; v = parent[v])
            path[k++] = v;

        printf("Path: ");
        for (int i = k - 1; i >= 0; i--)
            printf("%d%s", path[i], (i == 0 ? "\n" : " -> "));
    }
}

int main() {
    int edges, u, v, w, src, target;

    printf("Enter number of vertices: ");
    scanf("%d", &n);
    printf("Enter number of edges: ");
    scanf("%d", &edges);

    // Initialize graph
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            graph[i][j] = 0;

    printf("Enter edges (src dest weight):\n");
    for (int i = 0; i < edges; i++) {
        scanf("%d %d %d", &u, &v, &w);
        graph[u][v] = w;
        // graph[v][u] = w; // Uncomment for undirected graph
    }

    printf("Enter source and target nodes: ");
    scanf("%d %d", &src, &target);

    dijkstra(src, target);
    return 0;
}
