// 15.	Write a program in C to construct the minimum spanning tree from any directed or undirected graph using Kruskal’s algorithm.
#include <stdio.h>
#include <stdlib.h>

#define MAX 100

// Structure to represent an edge
struct Edge {
    int src, dest, weight;
};

// Structure for disjoint set (Union-Find)
int parent[MAX];

int find(int i) {
    while (i != parent[i])
        i = parent[i];
    return i;
}

void unionSets(int i, int j) {
    int a = find(i);
    int b = find(j);
    parent[a] = b;
}

// Comparator for qsort
int compare(const void *a, const void *b) {
    return ((struct Edge*)a)->weight - ((struct Edge*)b)->weight;
}

int main() {
    int V, E;
    printf("Enter number of vertices and edges: ");
    scanf("%d %d", &V, &E);

    struct Edge edges[E];
    printf("Enter edges (src dest weight):\n");
    for (int i = 0; i < E; i++)
        scanf("%d %d %d", &edges[i].src, &edges[i].dest, &edges[i].weight);

    // Initialize disjoint sets
    for (int i = 0; i < V; i++)
        parent[i] = i;

    // Sort edges by weight
    qsort(edges, E, sizeof(struct Edge), compare);

    int mstWeight = 0, count = 0;
    printf("Edges in the Minimum Spanning Tree:\n");

    for (int i = 0; i < E && count < V - 1; i++) {
        int u = edges[i].src;
        int v = edges[i].dest;
        int setU = find(u);
        int setV = find(v);

        if (setU != setV) {
            printf("(%d - %d) = %d\n", u, v, edges[i].weight);
            mstWeight += edges[i].weight;
            unionSets(setU, setV);
            count++;
        }
    }

    printf("Total cost of Minimum Spanning Tree: %d\n", mstWeight);
    return 0;
}
