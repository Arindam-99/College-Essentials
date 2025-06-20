//9.	Write a program in C for solving the Job Sequencing problem.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Job {
    char id[5];
    int deadline;
    int profit;
};

// Compare jobs by profit (descending)
int compare(const void *a, const void *b) {
    return ((struct Job*)b)->profit - ((struct Job*)a)->profit;
}

int min(int a, int b) {
    return (a < b) ? a : b;
}

int main() {
    int n;
    printf("Enter number of jobs: ");
    scanf("%d", &n);

    struct Job jobs[n];
    printf("Enter Job ID, Deadline, and Profit:\n");
    for(int i = 0; i < n; i++)
        scanf("%s %d %d", jobs[i].id, &jobs[i].deadline, &jobs[i].profit);

    // Sort jobs by profit in descending order
    qsort(jobs, n, sizeof(struct Job), compare);

    // Find max deadline to define job slots
    int maxDeadline = 0;
    for(int i = 0; i < n; i++)
        if(jobs[i].deadline > maxDeadline)
            maxDeadline = jobs[i].deadline;

    char slot[maxDeadline][5]; // Array to store job IDs in slots
    int filled[maxDeadline];
    memset(filled, 0, sizeof(filled));

    int totalProfit = 0;

    // Assign jobs to slots
    for(int i = 0; i < n; i++) {
        for(int j = min(maxDeadline, jobs[i].deadline) - 1; j >= 0; j--) {
            if(!filled[j]) {
                filled[j] = 1;
                strcpy(slot[j], jobs[i].id);
                totalProfit += jobs[i].profit;
                break;
            }
        }
    }

    // Output result
    printf("Selected Jobs: ");
    for(int i = 0; i < maxDeadline; i++)
        if(filled[i]) printf("%s ", slot[i]);
    printf("\nTotal Profit: %d\n", totalProfit);

    return 0;
}
