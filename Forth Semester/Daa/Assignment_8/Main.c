#include <stdio.h>

struct Item {
    int weight;
    int value;
};

void swap(struct Item *a, struct Item *b) {
    struct Item temp = *a;
    *a = *b;
    *b = temp;
}

// Sort items by value/weight ratio in descending order
void sortItems(struct Item arr[], int n) {
    for(int i = 0; i < n-1; i++) {
        for(int j = 0; j < n-i-1; j++) {
            double r1 = (double)arr[j].value / arr[j].weight;
            double r2 = (double)arr[j+1].value / arr[j+1].weight;
            if(r1 < r2)
                swap(&arr[j], &arr[j+1]);
        }
    }
}

double fractionalKnapsack(int W, struct Item arr[], int n) {
    sortItems(arr, n);
    double totalValue = 0.0;

    for(int i = 0; i < n; i++) {
        if(W >= arr[i].weight) {
            W -= arr[i].weight;
            totalValue += arr[i].value;
        } else {
            totalValue += (double)W * arr[i].value / arr[i].weight;
            break;
        }
    }
    return totalValue;
}

int main() {
    int n, W;
    printf("Enter number of items: ");
    scanf("%d", &n);
    struct Item items[n];

    printf("Enter value and weight of each item (value weight):\n");
    for(int i = 0; i < n; i++)
        scanf("%d %d", &items[i].value, &items[i].weight);

    printf("Enter maximum capacity of knapsack: ");
    scanf("%d", &W);

    double maxValue = fractionalKnapsack(W, items, n);
    printf("Maximum value in knapsack = %.2f\n", maxValue);
    return 0;
}
