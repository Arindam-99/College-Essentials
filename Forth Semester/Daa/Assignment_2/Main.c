// 2.	Write a program in C to search an element from a sorted array having n elements using an algorithm whose complexity is O(log(n)).
#include <stdio.h>

int main() {
    int n, key, low = 0, high, mid;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d sorted elements: ", n);
    for(int i = 0; i < n; i++) scanf("%d", &a[i]);
    printf("Enter element to search: ");
    scanf("%d", &key);
    high = n - 1;

    while(low <= high) {
        mid = (low + high) / 2;
        if(a[mid] == key) {
            printf("Element found at index %d\n", mid);
            return 0;
        } else if(a[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    printf("Element not found\n");
    return 0;
}
