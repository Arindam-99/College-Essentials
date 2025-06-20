// 6.	Write a program in C for sorting an array of n numbers of elements using the following algorithms: 
// b.	Quick Sort.


int partition(int a[], int low, int high) {
    int pivot = a[high], i = low - 1, temp;
    for(int j = low; j < high; j++) {
        if(a[j] < pivot) {
            i++;
            temp = a[i]; a[i] = a[j]; a[j] = temp;
        }
    }
    temp = a[i + 1]; a[i + 1] = a[high]; a[high] = temp;
    return i + 1;
}

void quickSort(int a[], int low, int high) {
    if(low < high) {
        int pi = partition(a, low, high);
        quickSort(a, low, pi - 1);
        quickSort(a, pi + 1, high);
    }
}
