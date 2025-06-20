// 1.	Write a program in C to search an element from n numbers of an array using an algorithm whose time complexity is O(n).
#include <stdio.h>

int main() {
    int n, key, i, found = 0;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter %d elements: ", n);
    for(i = 0; i < n; i++) scanf("%d", &a[i]);
    printf("Enter element to search: ");
    scanf("%d", &key);
    for(i = 0; i < n; i++) {
        if(a[i] == key) {
            found = 1;
            break;
        }
    }
    if(found) printf("Element found at index %d\n", i);
    else printf("Element not found\n");
    return 0;
}
