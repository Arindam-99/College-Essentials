// 6.	Write a program in C for sorting an array of n numbers of elements using the following algorithms: 

// c.	Heap Sort.

void heapify(int a[], int n, int i) {
    int largest = i, left = 2*i + 1, right = 2*i + 2, temp;

    if(left < n && a[left] > a[largest]) largest = left;
    if(right < n && a[right] > a[largest]) largest = right;

    if(largest != i) {
        temp = a[i]; a[i] = a[largest]; a[largest] = temp;
        heapify(a, n, largest);
    }
}

void heapSort(int a[], int n) {
    for(int i = n/2 - 1; i >= 0; i--) heapify(a, n, i);
    for(int i = n - 1; i >= 0; i--) {
        int temp = a[0]; a[0] = a[i]; a[i] = temp;
        heapify(a, i, 0);
    }
}
