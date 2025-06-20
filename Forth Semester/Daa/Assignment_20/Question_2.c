// 20.	Write programs in C to compare string matching using the
// and KMP algorithm.

#include <stdio.h>
#include <string.h>

void computeLPSArray(char* pattern, int m, int* lps) {
    int len = 0; // length of the previous longest prefix suffix
    lps[0] = 0;
    int i = 1;

    while (i < m) {
        if (pattern[i] == pattern[len]) {
            len++;
            lps[i++] = len;
        } else {
            if (len != 0) {
                len = lps[len - 1];
            } else {
                lps[i++] = 0;
            }
        }
    }
}

void KMPSearch(char* pattern, char* text) {
    int m = strlen(pattern);
    int n = strlen(text);
    int lps[m];
    int found = 0;

    computeLPSArray(pattern, m, lps);

    int i = 0; // index for text
    int j = 0; // index for pattern
    while (i < n) {
        if (pattern[j] == text[i]) {
            i++; j++;
        }

        if (j == m) {
            printf("Pattern found at index %d\n", i - j);
            found = 1;
            j = lps[j - 1];
        } else if (i < n && pattern[j] != text[i]) {
            if (j != 0)
                j = lps[j - 1];
            else
                i++;
        }
    }

    if (!found)
        printf("Pattern not found\n");
}

int main() {
    char text[100], pattern[100];

    printf("Enter the text: ");
    gets(text);
    printf("Enter the pattern: ");
    gets(pattern);

    printf("\nKMP Pattern Matching:\n");
    KMPSearch(pattern, text);

    return 0;
}
