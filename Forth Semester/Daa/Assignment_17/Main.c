// 17.	Write a program in C to find the shortest path from a given node to all other nodes in a graph using the Bellman Ford algorithm and demonstrate how it performs for a graph having negative edges.
#include <stdio.h>
#include <limits.h>

#define MAX 100
#define INF 1000000

struct Edge {
    int src, dest, weight;
};

int main() {
    int V, E, src;
    struct Edge edges[MAX];

    printf("Enter number of vertices and edges: ");
    scanf("%d %d", &V, &E);

    printf("Enter edges (src dest weight):\n");
    for (int i = 0; i < E; i++) {
        scanf("%d %d %d", &edges[i].src, &edges[i].dest, &edges[i].weight);
    }

    printf("Enter source vertex: ");
    scanf("%d", &src);

    int dist[V];
    for (int i = 0; i < V; i++)
        dist[i] = INF;
    dist[src] = 0;

    // Bellman-Ford algorithm
    for (int i = 1; i <= V - 1; i++) {
        for (int j = 0; j < E; j++) {
            int u = edges[j].src;
            int v = edges[j].dest;
            int w = edges[j].weight;

            if (dist[u] != INF && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }

    // Check for negative-weight cycles
    int hasNegativeCycle = 0;
    for (int j = 0; j < E; j++) {
        int u = edges[j].src;
        int v = edges[j].dest;
        int w = edges[j].weight;
        if (dist[u] != INF && dist[u] + w < dist[v]) {
            hasNegativeCycle = 1;
            break;
        }
    }

    if (hasNegativeCycle) {
        printf("Graph contains a negative weight cycle!\n");
    } else {
        printf("Vertex\tDistance from Source %d\n", src);
        for (int i = 0; i < V; i++) {
            if (dist[i] == INF)
                printf("%d\tINF\n", i);
            else
                printf("%d\t%d\n", i, dist[i]);
        }
    }

    return 0;
}
