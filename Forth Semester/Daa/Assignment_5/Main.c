// 5.	Write a program in C for sorting an array of n numbers of elements using any algorithm having best case time complexity of O(n^2).

#include <stdio.h>

void bubbleSort(int a[], int n) {
    int i, j, temp, swapped;
    for(i = 0; i < n - 1; i++) {
        swapped = 0;
        for(j = 0; j < n - i - 1; j++) {
            if(a[j] > a[j + 1]) {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
                swapped = 1;
            }
        }
        if(swapped == 0) break; // Array already sorted
    }
}

int main() {
    int n;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d elements: ", n);
    for(int i = 0; i < n; i++) scanf("%d", &a[i]);

    bubbleSort(a, n);

    printf("Sorted array: ");
    for(int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");

    return 0;
}
