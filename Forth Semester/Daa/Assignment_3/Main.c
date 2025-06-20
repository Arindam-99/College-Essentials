//3.	Write a program in C to search an element from a sorted array having n elements using an algorithm whose complexity is O(log(log(n))).
#include <stdio.h>

int binarySearch(int a[], int l, int r, int key) {
    while (l <= r) {
        int mid = (l + r) / 2;
        if (a[mid] == key) return mid;
        else if (a[mid] < key) l = mid + 1;
        else r = mid - 1;
    }
    return -1;
}

int main() {
    int n, key, i;
    printf("Enter number of sorted elements: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d sorted elements: ", n);
    for (i = 0; i < n; i++) scanf("%d", &a[i]);
    printf("Enter element to search: ");
    scanf("%d", &key);

    if (a[0] == key) {
        printf("Element found at index 0\n");
        return 0;
    }

    int i_bound = 1;
    while (i_bound < n && a[i_bound] <= key)
        i_bound *= 2;

    int result = binarySearch(a, i_bound / 2, (i_bound < n ? i_bound : n - 1), key);

    if (result != -1) printf("Element found at index %d\n", result);
    else printf("Element not found\n");

    return 0;
}
