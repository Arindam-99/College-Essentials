int main() {
    int n, i, a[100];
    printf("Enter number of elements: ");
    scanf("%d", &n);
    printf("Enter %d elements: ", n);
    for(i = 0; i < n; i++) scanf("%d", &a[i]);

    // Call one of the sorting algorithms
    // mergeSort(a, 0, n - 1);
    // quickSort(a, 0, n - 1);
    heapSort(a, n);

    printf("Sorted array: ");
    for(i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
