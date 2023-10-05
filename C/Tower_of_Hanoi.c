#include <stdio.h>
void hanoi(int n, char from, char by, char to);

int main()
{
    int n;

    printf("Enter the Number of Rings: ");
    scanf("%d", &n);

    hanoi(n, 'A', 'B', 'C');

    return 0;
}

void hanoi(int n, char from, char by, char to)
{
    if (n == 1)
    {
        static int i=1;
        printf("%d. Move top ring from %c to %c.\n", i, from, to);
        i++;
    }

    else
    {
        hanoi(n-1, from, to, by);
        hanoi(1, from, by, to);
        hanoi(n-1, by, from, to);
    }
}